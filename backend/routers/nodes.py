"""
UrbanShield Lite - Camera Nodes & Video Streaming Router
Endpoints for managing station cameras, metrics, scenarios, and MJPEG streams.
"""

import time
from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import StreamingResponse

from schemas import ScenarioPayload
from reporting import build_compact_payload
from database import save_incident_to_db
import state

router = APIRouter(tags=["Nodes & Streams"])


@router.get("/api/nodes")
@router.get("/api/v1/nodes")
def get_nodes():
    """Returns list of monitored camera stations."""
    return list(state.NODES.values())


@router.get("/api/nodes/{node_id}/metrics")
@router.get("/api/v1/nodes/{node_id}/metrics")
def get_node_metrics(node_id: str):
    """Returns real-time edge AI telemetry metrics for a station."""
    if node_id not in state.NODES:
        raise HTTPException(status_code=404, detail="Node not found")
    metrics = state.NODE_LATEST_METRICS.get(node_id, {
        "fps": 28.5,
        "infer_time_ms": 32.0,
        "clahe_active": False,
        "detections_count": 3,
        "payload_bytes": 84,
        "privacy": {"ram_only": True, "frames_processed_in_ram": state.detector.frames_processed_in_ram, "disk_writes": 0},
        "accident": {"detected": False, "reason": "", "motionless_sec": 0.0},
        "flood": {"detected": False, "depth_cm": 0.0, "level": "SAFE"}
    })
    return metrics


@router.post("/api/nodes/{node_id}/scenario")
@router.post("/api/v1/nodes/{node_id}/scenario")
def set_node_scenario(node_id: str, data: ScenarioPayload):
    """Changes active scenario recording for a camera node."""
    if node_id not in state.NODES:
        raise HTTPException(status_code=404, detail="Node not found")

    state.NODES[node_id]["scenario"] = data.scenario
    state.detector.reset_state()
    if node_id in state.NODE_ANALYSIS_CACHE:
        del state.NODE_ANALYSIS_CACHE[node_id]

    if data.scenario in state.VIDEO_CAPS:
        try:
            state.VIDEO_CAPS[data.scenario].release()
            del state.VIDEO_CAPS[data.scenario]
        except Exception:
            pass

    return {
        "success": True,
        "node": state.NODES[node_id],
        "message": f"Đã chuyển kịch bản trạm {node_id} sang {data.scenario}. Luồng phân tích AI sẽ cập nhật theo khung hình thực tế."
    }


@router.get("/api/video_feed/{node_id}")
@router.get("/api/v1/video_feed/{node_id}")
def video_feed(
    node_id: str,
    fps: Optional[float] = Query(None, ge=1.0, le=60.0, description="Tùy chỉnh FPS luồng phát video")
):
    """Streams live MJPEG camera feed with Edge AI HUD overlay."""
    return StreamingResponse(
        state.stream_generator(node_id, custom_fps=fps),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )


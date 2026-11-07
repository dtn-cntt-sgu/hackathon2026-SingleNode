import React from 'react';
import { Cpu, AlertTriangle, CheckCircle2, ShieldAlert, Clock, AlertOctagon, Info } from 'lucide-react';

export default function VideoMonitor({
  activeNode,
  backendConnected,
  streamError,
  setStreamError,
  apiBase,
  metrics
}) {
  const vehiclesCount = metrics?.vehicles_count ?? (metrics?.flood?.has_reference ? 1 : 0);
  const hasRefObject = Boolean(vehiclesCount > 0 && metrics?.flood?.has_reference === true);
  const depthValue = (hasRefObject && metrics?.flood?.detected) ? metrics.flood.depth_cm : 0;
  const lastRefDepth = metrics?.flood?.last_ref_depth_cm || 0;
  const depthPercent = Math.min(100, Math.max(0, (depthValue / 50) * 100));
  
  // Accident / Fall telemetry
  const isAccident = Boolean(metrics?.accident?.detected);
  const motionlessSec = Number(metrics?.accident?.motionless_sec || 0);
  const isCandidateFalling = motionlessSec > 0 && !isAccident;
  const fallProgress = Math.min(100, Math.max(0, (motionlessSec / 5.0) * 100));

  // Determine dynamic gradient color for the flood gauge fill
  let gaugeGradient = 'linear-gradient(90deg, #10b981 0%, #34d399 100%)'; // Green (Safe <10cm)
  if (depthValue >= 20.0) {
    gaugeGradient = 'linear-gradient(90deg, #10b981 0%, #f59e0b 35%, #ef4444 80%)'; // Red (Danger >=20cm)
  } else if (depthValue >= 10.0) {
    gaugeGradient = 'linear-gradient(90deg, #10b981 0%, #f59e0b 100%)'; // Amber (Warning 10-20cm)
  }

  return (
    <div className="video-monitor-container">
      {/* 1. Video Feed Screen */}
      <div className="video-feed-wrapper">
        {backendConnected && !streamError ? (
          <img
            key={`${activeNode.id}-${activeNode.scenario}`}
            src={`${apiBase}/api/video_feed/${activeNode.id}`}
            alt="Live Camera Feed"
            className="video-stream-img"
            onError={() => setStreamError(true)}
          />
        ) : (
          <div className="video-placeholder">
            <Cpu size={40} className="placeholder-icon" />
            <h3>{activeNode.name}</h3>
            <p>Đang kết nối luồng camera khu phố...</p>
          </div>
        )}

        <div className="hud-overlay">
          <div className="live-badge">
            <div className="live-indicator" />
            <span>{activeNode.name}</span>
          </div>
        </div>
      </div>

      {/* 2. Automated AI Fall & Road Accident Monitor Card */}
      <div className={`fall-monitor-card ${isAccident ? 'accident-danger' : isCandidateFalling ? 'accident-tracking' : 'accident-safe'}`}>
        <div className="fall-monitor-header">
          <div className="fall-title-group">
            {isAccident ? (
              <AlertOctagon size={16} className="fall-icon text-danger pulse-icon" />
            ) : isCandidateFalling ? (
              <Clock size={16} className="fall-icon text-warning spin-slow" />
            ) : (
              <CheckCircle2 size={16} className="fall-icon text-safe" />
            )}
            <span className="fall-title">GIÁM SÁT NGÃ XE TỰ ĐỘNG</span>
          </div>

          <span className={`fall-status-pill ${isAccident ? 'danger' : isCandidateFalling ? 'warning' : 'safe'}`}>
            {isAccident
              ? '🚨 PHÁT HIỆN SỰ CỐ NGÃ XE'
              : isCandidateFalling
              ? `⏱️ ĐANG THEO DÕI BẤT ĐỘNG: ${motionlessSec.toFixed(1)}s / 5.0s`
              : '🟢 AN TOÀN (LƯU THÔNG BÌNH THƯỜNG)'}
          </span>
        </div>

        {/* Fall Countdown Progress Bar (Active when fall candidate is detected) */}
        {isCandidateFalling && (
          <div className="fall-countdown-track">
            <div
              className="fall-countdown-fill"
              style={{ width: `${fallProgress}%` }}
            />
          </div>
        )}

        <div className="fall-monitor-desc">
          {isAccident ? (
            <div className="fall-desc-content danger">
              <strong>Sự cố:</strong> Người ngã nằm bất động <strong>{motionlessSec > 0 ? motionlessSec.toFixed(1) : '5.0'} giây</strong> (vượt ngưỡng 5 giây). Hệ thống đã tự động gửi tin nhắn cảnh báo tới Telegram Dân quân / Khu phố.
            </div>
          ) : isCandidateFalling ? (
            <div className="fall-desc-content warning">
              <strong>Bộ lọc chống báo giả:</strong> AI đang theo dõi liên tục 5 giây. Nếu người dân tự đứng dậy hoặc cúi nhặt đồ trước 5 giây, AI sẽ tự động hủy cảnh báo.
            </div>
          ) : (
            <div className="fall-desc-content safe">
              Không phát hiện tư thế ngã nằm đường. Người và phương tiện lưu thông bình thường qua khu vực ngõ hẻm.
            </div>
          )}
        </div>
      </div>

      {/* 3. Geometric 50cm Wheel Flood Depth Gauge */}
      <div className="telemetry-gauge-card">
        <div className="gauge-calibrator">
          <div className="gauge-header">
            <div className="gauge-label-group">
              <span className="gauge-title">ĐO NGẬP HÌNH HỌC (BÁNH XE MÁY 50CM)</span>
              <span className={`gauge-status-text ${(hasRefObject && metrics?.flood?.level === 'DANGER') ? 'text-danger' : 'text-warning'}`}>
                {(hasRefObject && metrics?.flood?.detected) ? (
                  <>
                    {metrics.flood.level === 'DANGER'
                      ? '⚠️ Ngập nguy hiểm (Vượt nửa bánh xe)'
                      : '⚡ Ngập mức chú ý (Mấp mé ống xả)'}
                  </>
                ) : !hasRefObject && metrics?.flood?.water_surface_present ? (
                  <>💧 Có nước ngập — Chờ xe máy đi qua để đo{lastRefDepth > 0 ? ` (Lần đo trước: ${lastRefDepth}cm)` : ''}</>
                ) : (
                  <>✅ Mặt đường thông thoáng, không ngập nước</>
                )}
              </span>
            </div>

            <div className="gauge-val-box">
              {hasRefObject ? (
                <div className="gauge-val-number">
                  <span className="val-large">{depthValue.toFixed(1)}</span>
                  <span className="val-unit">cm / 50cm</span>
                </div>
              ) : metrics?.flood?.water_surface_present ? (
                <span className="gauge-val-waiting">Chờ xe máy làm mốc</span>
              ) : (
                <span className="gauge-val-dry">Đường khô ráo</span>
              )}
            </div>
          </div>

          {/* Progress Bar with 3 Visual Danger Zones */}
          <div className="gauge-track">
            <div className="track-marker safe-mark" style={{ left: '20%' }}>
              <span className="mark-label">10cm (Ống xả)</span>
            </div>
            <div className="track-marker danger-mark" style={{ left: '50%' }}>
              <span className="mark-label">25cm (Nửa bánh)</span>
            </div>
            <div className="track-marker full-mark" style={{ left: '100%' }}>
              <span className="mark-label">50cm</span>
            </div>

            <div
              className="gauge-fill"
              style={{
                width: `${depthPercent}%`,
                background: gaugeGradient,
                boxShadow: depthValue >= 20 ? '0 0 10px rgba(239, 68, 68, 0.5)' : 'none'
              }}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

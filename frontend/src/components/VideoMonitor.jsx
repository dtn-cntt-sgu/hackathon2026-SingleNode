import React from 'react';
import { Cpu, Droplets, AlertOctagon, Clock, CheckCircle2, Waves } from 'lucide-react';

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
  let floodLevelClass = 'safe';
  let floodLevelText = '✅ Mặt đường thông thoáng';

  if (depthValue >= 20.0) {
    gaugeGradient = 'linear-gradient(90deg, #10b981 0%, #f59e0b 35%, #ef4444 80%)'; // Red (Danger >=20cm)
    floodLevelClass = 'danger';
    floodLevelText = '⚠️ Ngập sâu (Vượt nửa bánh xe)';
  } else if (depthValue >= 10.0) {
    gaugeGradient = 'linear-gradient(90deg, #10b981 0%, #f59e0b 100%)'; // Amber (Warning 10-20cm)
    floodLevelClass = 'warning';
    floodLevelText = '⚡ Ngập chú ý (Mấp mé ống xả)';
  } else if (!hasRefObject && metrics?.flood?.water_surface_present) {
    floodLevelClass = 'waiting';
    floodLevelText = `💧 Có nước ngập (Chờ xe máy làm mốc${lastRefDepth > 0 ? ` - Lần đo trước: ${lastRefDepth}cm` : ''})`;
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

      {/* 2. Side-by-Side Dual Status Cards (50% - 50%) */}
      <div className="dual-monitor-grid">
        {/* Card 1: Giám sát ngập nước qua bánh xe máy 50cm */}
        <div className={`dual-status-card flood-card ${floodLevelClass}`}>
          <div className="dual-card-header">
            <div className="dual-card-title-group">
              <Droplets size={15} className={`dual-card-icon ${floodLevelClass}`} />
              <span className="dual-card-title">1. MỰC NƯỚC NGẬP</span>
            </div>
            <div className="dual-card-badge-wrap">
              {hasRefObject ? (
                <div className="dual-val-badge">
                  <span className="val-number">{depthValue.toFixed(1)}</span>
                  <span className="val-unit">cm / 50cm</span>
                </div>
              ) : metrics?.flood?.water_surface_present ? (
                <span className="dual-val-text waiting">Chờ xe máy mốc</span>
              ) : (
                <span className="dual-val-text dry">0 cm (Khô ráo)</span>
              )}
            </div>
          </div>

          <div className="dual-card-status-line">
            <span className={`status-label ${floodLevelClass}`}>{floodLevelText}</span>
          </div>

          {/* Calibrated 50cm Gauge Track */}
          <div className="gauge-track mini-track">
            <div className="track-marker safe-mark" style={{ left: '20%' }}>
              <span className="mark-label">10cm</span>
            </div>
            <div className="track-marker danger-mark" style={{ left: '50%' }}>
              <span className="mark-label">25cm</span>
            </div>
            <div className="track-marker full-mark" style={{ left: '100%' }}>
              <span className="mark-label">50cm</span>
            </div>

            <div
              className="gauge-fill"
              style={{
                width: `${depthPercent}%`,
                background: gaugeGradient,
                boxShadow: depthValue >= 20 ? '0 0 8px rgba(239, 68, 68, 0.45)' : 'none'
              }}
            />
          </div>
        </div>

        {/* Card 2: Giám sát sự cố ngã xe tự động (Bộ đếm 5s) */}
        <div className={`dual-status-card fall-card ${isAccident ? 'accident-danger' : isCandidateFalling ? 'accident-tracking' : 'accident-safe'}`}>
          <div className="dual-card-header">
            <div className="dual-card-title-group">
              {isAccident ? (
                <AlertOctagon size={15} className="dual-card-icon danger pulse-icon" />
              ) : isCandidateFalling ? (
                <Clock size={15} className="dual-card-icon warning spin-slow" />
              ) : (
                <CheckCircle2 size={15} className="dual-card-icon safe" />
              )}
              <span className="dual-card-title">2. SỰ CỐ NGÃ XE</span>
            </div>

            <div className="dual-card-badge-wrap">
              <span className={`dual-status-pill ${isAccident ? 'danger' : isCandidateFalling ? 'warning' : 'safe'}`}>
                {isAccident
                  ? '🚨 SỰ CỐ NGÃ XE'
                  : isCandidateFalling
                  ? `${motionlessSec.toFixed(1)}s / 5.0s`
                  : '🟢 AN TOÀN'}
              </span>
            </div>
          </div>

          {/* Fall Progress Bar (Active when candidate detected) */}
          <div className="dual-card-status-line">
            {isAccident ? (
              <span className="status-label danger">
                Ngã bất động <strong>{motionlessSec > 0 ? motionlessSec.toFixed(1) : '5.0'}s</strong> — Đã báo Telegram
              </span>
            ) : isCandidateFalling ? (
              <span className="status-label warning">
                Đang theo dõi: Tự động hủy nếu người dân đứng dậy &lt; 5s
              </span>
            ) : (
              <span className="status-label safe">
                Không phát hiện người ngã — Lưu thông bình thường
              </span>
            )}
          </div>

          <div className="gauge-track mini-track fall-track">
            {isAccident ? (
              <div
                className="gauge-fill danger"
                style={{ width: '100%', background: 'linear-gradient(90deg, #f59e0b, #ef4444)' }}
              />
            ) : isCandidateFalling ? (
              <div
                className="gauge-fill warning"
                style={{
                  width: `${fallProgress}%`,
                  background: 'linear-gradient(90deg, #3b82f6, #f59e0b)'
                }}
              />
            ) : (
              <div
                className="gauge-fill safe"
                style={{ width: '100%', background: '#dcfce7' }}
              />
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

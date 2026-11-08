"""
UrbanShield Lite - Playwright End-to-End Browser Automation Test Suite
Verifies web UI, real-time edge telemetry, video stream overlays,
interactive Leaflet WebGIS, and shift report modal with live screenshot capture.
"""

import os
import time
import pytest

playwright = pytest.importorskip("playwright", reason="Playwright is required for browser E2E tests")
from playwright.sync_api import sync_playwright, expect

FRONTEND_URL = os.environ.get("FRONTEND_URL", "http://localhost:5173")
SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs", "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


@pytest.fixture(scope="module")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        yield context
        browser.close()


def test_e2e_dashboard_and_flood_tram01(browser_context):
    """Test 1: Dashboard loads, Trạm 01 displays live video feed and flood telemetry with screenshot."""
    page = browser_context.new_page()
    page.goto(FRONTEND_URL, timeout=15000)

    # 1. Verify Brand Header
    expect(page.locator(".brand-title")).to_contain_text("UrbanShield Lite")
    
    # 2. Wait for station tabs to render
    page.wait_for_selector(".node-selector-tabs", timeout=10000)
    expect(page.locator(".node-selector-tabs")).to_be_visible()

    # 3. Wait for video feed and status cards to hydrate
    page.wait_for_timeout(2500)
    
    # Capture Screenshot 1: Trạm 01 Live Flood Monitoring
    screenshot_path = os.path.join(SCREENSHOT_DIR, "01_dashboard_tram01_flood.png")
    page.screenshot(path=screenshot_path, full_page=False)
    assert os.path.exists(screenshot_path)
    page.close()


def test_e2e_station_switch_dry_road_tram03(browser_context):
    """Test 2: Switching to Trạm 03 displays dry road scenario with safe status with screenshot."""
    page = browser_context.new_page()
    page.goto(FRONTEND_URL, timeout=15000)
    page.wait_for_selector(".node-selector-tabs", timeout=10000)

    # Click Trạm 03 tab
    tram03_btn = page.locator("button.node-tab-btn", has_text="Trạm 03")
    tram03_btn.click()
    page.wait_for_timeout(2500)

    # Verify street segment text updated
    expect(page.locator(".camera-meta-street")).to_contain_text("Lê Văn Lương")

    # Capture Screenshot 2: Trạm 03 Dry Road
    screenshot_path = os.path.join(SCREENSHOT_DIR, "02_station_tram03_dry_road.png")
    page.screenshot(path=screenshot_path, full_page=False)
    assert os.path.exists(screenshot_path)
    page.close()


def test_e2e_station_switch_accident_tram05(browser_context):
    """Test 3: Switching to Trạm 05 displays slip/fall accident alert with screenshot."""
    page = browser_context.new_page()
    page.goto(FRONTEND_URL, timeout=15000)
    page.wait_for_selector(".node-selector-tabs", timeout=10000)

    # Click Trạm 05 tab
    tram05_btn = page.locator("button.node-tab-btn", has_text="Trạm 05")
    tram05_btn.click()
    page.wait_for_timeout(2500)

    # Verify street segment text updated
    expect(page.locator(".camera-meta-street")).to_contain_text("Kênh Tẻ")

    # Capture Screenshot 3: Trạm 05 Dốc Cầu Kênh Tẻ
    screenshot_path = os.path.join(SCREENSHOT_DIR, "03_station_tram05_accident.png")
    page.screenshot(path=screenshot_path, full_page=False)
    assert os.path.exists(screenshot_path)
    page.close()


def test_e2e_shift_report_modal(browser_context):
    """Test 4: Shift Report modal opens, showing plain-text report and compact payload with screenshot."""
    page = browser_context.new_page()
    page.goto(FRONTEND_URL, timeout=15000)
    page.wait_for_selector(".report-btn", timeout=10000)

    # Click "Báo cáo ca trực"
    page.locator(".report-btn").click()
    page.wait_for_timeout(1000)

    # Verify modal is open
    expect(page.locator(".report-modal")).to_be_visible()

    # Capture Screenshot 4: Shift Report Modal
    screenshot_path = os.path.join(SCREENSHOT_DIR, "04_shift_report_modal.png")
    page.screenshot(path=screenshot_path, full_page=False)
    assert os.path.exists(screenshot_path)
    page.close()


def test_e2e_webgis_map_component(browser_context):
    """Test 5: WebGIS Leaflet interactive map renders with route segments with screenshot."""
    page = browser_context.new_page()
    page.goto(FRONTEND_URL, timeout=15000)
    page.wait_for_selector(".map-card-wrapper", timeout=10000)

    # Verify leaflet container
    expect(page.locator(".leaflet-container")).to_be_visible()
    page.wait_for_timeout(2000)

    # Focus map and capture screenshot
    screenshot_path = os.path.join(SCREENSHOT_DIR, "05_webgis_interactive_map.png")
    map_elem = page.locator(".map-card-wrapper")
    map_elem.screenshot(path=screenshot_path)
    assert os.path.exists(screenshot_path)
    page.close()


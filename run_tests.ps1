Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  URBANSHIELD LITE - CHAY TOAN BO 24 BAI KIEM THU QA" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan

& ".\backend\venv\Scripts\pytest.exe" tests/ -v


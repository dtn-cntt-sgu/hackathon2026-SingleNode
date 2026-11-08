Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  URBANSHIELD LITE - KHOI DONG BACKEND VA FRONTEND" -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Cyan

Start-Process powershell -ArgumentList "-NoExit", "-Command", "backend\venv\Scripts\python.exe -m uvicorn main:app --app-dir backend --host 127.0.0.1 --port 8000"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location frontend; npm run dev"

Write-Host "`n[V] Da khoi dong Backend tai:  http://127.0.0.1:8000" -ForegroundColor Green
Write-Host "[V] Da khoi dong Frontend tai: http://localhost:5173`n" -ForegroundColor Green


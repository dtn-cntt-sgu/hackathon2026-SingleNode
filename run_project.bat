@echo off
title UrbanShield Lite - Startup
echo ========================================================
echo   URBANSHIELD LITE - KHOI DONG BACKEND VA FRONTEND
echo ========================================================
echo.
echo [*] Dang khoi dong Backend FastAPI tai http://127.0.0.1:8000...
start "UrbanShield Backend" cmd /k "backend\venv\Scripts\python.exe -m uvicorn main:app --app-dir backend --host 127.0.0.1 --port 8000"

echo [*] Dang khoi dong Frontend Vite tai http://localhost:5173...
start "UrbanShield Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo [V] Da khoi dong ca 2 phan he thanh cong!
echo     - Giao dien Web: http://localhost:5173/
echo     - Tai lieu API:  http://127.0.0.1:8000/docs
echo ========================================================


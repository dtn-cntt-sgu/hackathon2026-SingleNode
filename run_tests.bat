@echo off
echo ========================================================
echo   URBANSHIELD LITE - CHAY TOAN BO 24 BAI KIEM THU QA
echo ========================================================
backend\venv\Scripts\pytest.exe tests/ -v
pause


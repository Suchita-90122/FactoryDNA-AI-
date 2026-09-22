@echo off
title FactoryDNA AI - Starting Services

echo ==========================================
echo       FACTORYDNA AI
echo       Starting all services...
echo ==========================================

start "AI Prediction" cmd /k "cd /d C:\Users\suchi\OneDrive\Desktop\FactoryDNA-AI\ml && venv\Scripts\activate && python app.py"

start "IoT Service" cmd /k "cd /d C:\Users\suchi\OneDrive\Desktop\FactoryDNA-AI\iot-service && python app.py"

start "Processing Service" cmd /k "cd /d C:\Users\suchi\OneDrive\Desktop\FactoryDNA-AI\processing-service && python app.py"

start "Integration Service" cmd /k "cd /d C:\Users\suchi\OneDrive\Desktop\FactoryDNA-AI\integration && python app.py"

start "Optimization Service" cmd /k "cd /d C:\Users\suchi\OneDrive\Desktop\FactoryDNA-AI\optimization-service && python app.py"

start "FactoryDNA Dashboard" cmd /k "cd /d C:\Users\suchi\OneDrive\Desktop\FactoryDNA-AI\frontend && python -m http.server 8000"

timeout /t 5 /nobreak >nul

start http://127.0.0.1:8000

echo.
echo FactoryDNA AI is starting...
echo Dashboard: http://127.0.0.1:8000
echo.
pause
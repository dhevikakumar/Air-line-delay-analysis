@echo off
echo Starting Airline Delay Analysis Dashboard...
echo.
echo Server will start at: http://localhost:8000
echo.
echo Press Ctrl+C to stop the server when you're done viewing.
echo.
start http://localhost:8000
python -m http.server 8000

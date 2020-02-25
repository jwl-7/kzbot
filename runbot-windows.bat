@echo off
echo.
echo Starting kzbot.py...
echo.
:loop
    python kzbot.py
    echo.
    echo Restarting kzbot.py...
    echo.
    timeout 5 > nul
goto loop
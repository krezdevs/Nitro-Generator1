@echo off
echo Installing required Python modules...

pip install requests
pip install colorama
pip install discord_webhook
py -3 -m pip install numpy

if %errorlevel% equ 0 (
    echo All modules installed successfully.
) else (
    echo There was an error installing some modules. Please check the output above.
)

pause

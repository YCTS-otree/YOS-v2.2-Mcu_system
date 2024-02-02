%Code written by OCR%

@echo off
set /p com= Enter the port number (e.g., COM8):

echo.
echo Attempting to connect to the development board
echo Files in the development board:
ampy --port %com% ls

echo.
echo Scanning the current directory...
echo Files available for upload:
for %%i in (*.py) do ( 
    echo ^|--%%i %Use '^' to escape special characters%
)
echo Would you like to upload the above files to %com%?
set /p yn=(y/n)
echo.
if '%yn%' == 'y' (
    for %%i in (*.py) do ( 
        echo Uploading %%i
        echo Executing ampy^ --port^ %com%^ put^ %~dp0%%i
        ampy --port %com% put "%~dp0%%i"
        echo Done!
        echo.
    )
    echo Upload completed!!!
)

echo ¡¾Press any key to exit¡¿
pause > nul
exit

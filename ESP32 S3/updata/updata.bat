%Code written by OCR%

@echo off
set /p com= ������˿ںţ��磺COM8����

echo.
echo ���ڳ������ӿ�����
echo ���������ļ�����
ampy --port %com% ls

echo.
echo ����ɨ�豾�ļ�Ŀ¼...
echo ���ϴ��ļ����£�
for %%i in (*.py) do ( 
    echo ^|--%%i %��'^'ת������ִ�з���%
)
echo �Ƿ��ϴ������ļ���%com%?
set /p yn=(y/n)
echo.
if '%yn%' == 'y' (
    for %%i in (*.py) do ( 
        echo �����ϴ�%%i
        echo ִ��ampy^ --port^ %com%^ put^ %~dp0%%i
        ampy --port %com% put "%~dp0%%i"
        echo dome!
        echo.
    )
    echo �ϴ���ɣ�����
)

echo ����������˳���
pause > nul
exit


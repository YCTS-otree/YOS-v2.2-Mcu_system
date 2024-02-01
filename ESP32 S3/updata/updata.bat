%Code written by OCR%

@echo off
set /p com= 请输入端口号（如：COM8）：

echo.
echo 正在尝试连接开发板
echo 开发板内文件如下
ampy --port %com% ls

echo.
echo 正在扫描本文件目录...
echo 可上传文件如下：
for %%i in (*.py) do ( 
    echo ^|--%%i %用'^'转译特殊执行符号%
)
echo 是否上传以上文件至%com%?
set /p yn=(y/n)
echo.
if '%yn%' == 'y' (
    for %%i in (*.py) do ( 
        echo 正在上传%%i
        echo 执行ampy^ --port^ %com%^ put^ %~dp0%%i
        ampy --port %com% put "%~dp0%%i"
        echo dome!
        echo.
    )
    echo 上传完成！！！
)

echo 【按任意键退出】
pause > nul
exit


powercfg -list > power.txt
for /f "delims=" %%i in ('find "Balanced" power.txt') do set BALANCED=%%i
for /f "delims=" %%i in ('echo %BALANCED:~19,37%') do set BALANCED_GUID=%%i
del power.txt
powercfg /setactive %BALANCED_GUID%
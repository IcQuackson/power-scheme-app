
powercfg -list > power.txt
for /f "delims=" %%i in ('find "NEW" power.txt') do set CORTEX=%%i
for /f "delims=" %%i in ('echo %CORTEX:~19,37%') do set CORTEX_GUID=%%i
del power.txt
powercfg /setactive %CORTEX_GUID%
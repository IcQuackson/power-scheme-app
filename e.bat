@echo off 
if "%~z1" == "" ( 
    echo File doesnt exist. 
) else if "%~z1" == "0" ( 
    echo File is empty
) else ( 
    echo File is not empty
)
@echo off

IF EXIST Main.class (
    del Main.class
)

cd table_generation\tables
FOR /f %%i IN ('dir /b /ad ^| find /c /v ""') DO (set a=%%i)
cd ..\..

IF %a% GTR 0 (
    IF NOT "%1" == "-f" (
        ECHO Tables already exist. Use '-f' to force re-generation.
        GOTO END
    )
    rd /S /Q table_generation\tables
    md table_generation\tables
)

ECHO Compiling Choosing program in java...
javac Main.java
ECHO Running Choosing program...
java Main

IF EXIST Main.class (
    del Main.class
)
IF EXIST src\LinesSelector.class (
    del src\LinesSelector.class
)

ECHO.

SET "file=chosen.txt"
FOR %%A IN ("%file%") DO (
    IF %%~zA equ 0 (
        ECHO Choosing failed. Check the program in Main.java.
    ) ELSE (
        ECHO Choosing successful. Check the result in chosen.txt.
        ECHO.
        ECHO Now running table_generation program in python...
        cd table_generation
        venv\Scripts\python.exe main.py
        cd ..
    )
)
:END
pause
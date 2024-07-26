@echo off

@REM This script reads a file named .env, which is expected to contain lines in the 
@REM format `VARIABLE_NAME=VARIABLE_VALUE`, and sets each of these as environment variables in t
@REM he current session.

@REM `for /f "tokens=1,2 delims==" %%a in (.env) do (...)`: This is a for loop that reads the 
@REM contents of the .env file.

@REM    - `tokens=1,2`: This specifies that we want to split each line into two parts.
@REM    - `delims==`: This sets the delimiter to the equals sign (=).
@REM    - `%%a`: This represents the first token (before the =).
@REM    - `%%b`: This represents the second token (after the =).

@REM `set %%a=%%b`: Inside the loop, this command sets an environment variable. 
@REM The variable name is whatever comes before the = in each line of the .env file, 
@REM and the value is whatever comes after.

for /f "tokens=1,2 delims==" %%a in (.env) do (
    set %%a=%%b
)

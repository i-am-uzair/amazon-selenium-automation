@echo off
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Running Amazon tests in PARALLEL...
pytest test_amazon.py -v -s -n auto --no-header

echo.
echo ========================================
echo TEST RESULTS (Product Prices):
echo ========================================
if exist test_output.txt (
    type test_output.txt
) else (
    echo No output file found.
)
echo ========================================

echo.
echo Tests completed!
pause
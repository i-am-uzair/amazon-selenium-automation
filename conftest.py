import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session", autouse=True)
def clear_output_file():
    """Clear the output file before test session starts"""
    output_file = os.path.join(os.path.dirname(__file__), "test_output.txt")
    # Clear the file by writing empty content (avoids race conditions)
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("")
    except Exception:
        pass
    yield

def pytest_sessionfinish(session, exitstatus):
    """Display test output file contents after all tests complete"""
    output_file = os.path.join(session.config.rootpath, "test_output.txt")
    if os.path.exists(output_file):
        print("\n" + "="*60)
        print("TEST RESULTS - PRODUCT PRICES")
        print("="*60)
        with open(output_file, "r", encoding="utf-8") as f:
            content = f.read()
            print(content)
        print("="*60)

@pytest.fixture(scope="function")
def setup_browser():
    """Setup and teardown for each test"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()
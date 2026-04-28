# Amazon Product Search & Price Display - Automated Tests

Automated test cases for Amazon.com that search for products, add them to cart, and display prices - running in parallel execution.

## 📋 Assignment Requirements

✅ **Test Case 1:** Navigate to Amazon.com, search for an iPhone, add it to the cart, and print the device price to the console.

✅ **Test Case 2:** Navigate to Amazon.com, search for a Galaxy device, add it to the cart, and print the device price to the console.

✅ **Parallel Execution:** Both test cases run simultaneously using pytest-xdist.

## 🛠️ Technologies Used

- **Python 3.x**
- **Selenium WebDriver** - Browser automation
- **pytest** - Testing framework
- **pytest-xdist** - Parallel test execution
- **Chrome WebDriver** - Browser driver

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- Google Chrome browser installed
- Git installed

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd assignment
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

   Or install manually:
   ```bash
   pip install selenium==4.15.2 pytest==7.4.3 pytest-xdist==3.5.0 webdriver-manager==4.0.1
   ```

## 🚀 Running the Tests

### Option 1: Run Tests in Parallel (Recommended)

```bash
pytest test_amazon.py -v -s -n 2
```

**Parameters explained:**
- `-v` : Verbose output
- `-s` : Show print statements
- `-n 2` : Run 2 tests in parallel

### Option 2: Using the Batch File (Windows)

```bash
.\run_tests.bat
```

### Option 3: Run Tests Sequentially

```bash
pytest test_amazon.py -v -s
```

## 📊 Expected Output

When tests complete, you'll see the product prices displayed:

```
============================================================
TEST RESULTS - PRODUCT PRICES
============================================================

============================================================
[TEST RESULT] IPHONE
============================================================
Product: iPhone
Price: $XXX.XX
Status: Added to Cart Successfully
============================================================

============================================================
[TEST RESULT] GALAXY
============================================================
Product: Galaxy
Price: $XXX.XX
Status: Added to Cart Successfully
============================================================
```

## 📁 Project Structure

```
assignment/
├── test_amazon.py      # Test cases
├── conftest.py         # Pytest fixtures (browser setup)
├── pytest.ini          # Pytest configuration
├── requirement.txt     # Python dependencies
├── run_tests.bat       # Windows batch file for easy execution
├── README.md           # This file
└── test_output.txt     # Generated output file (created during test run)
```

## 🔧 Configuration

### pytest.ini

The pytest configuration file ensures consistent test execution:
- Automatically enables verbose mode
- Sets test discovery patterns
- Configures test paths

### conftest.py

Contains pytest fixtures:
- Browser setup and teardown
- Chrome WebDriver configuration
- Session-level output file management

## 🌐 Running on LambdaTest Cloud (Bonus)

### Step 1: Sign up for LambdaTest

1. Visit [https://www.lambdatest.com](https://www.lambdatest.com)
2. Click **"Sign Up Free"**
3. Create an account using email, Google, or GitHub

### Step 2: Get Your Credentials

1. Log in to your LambdaTest dashboard
2. Navigate to **Profile Settings** or **Automation** section
3. Find your:
   - **Username**
   - **Access Key** (click "Show Key")

### Step 3: Install LambdaTest Package

```bash
pip install lambdatest-selenium
```

### Step 4: Update conftest.py for LambdaTest

Create a new file `conftest_lambdatest.py`:

```python
import pytest
from selenium import webdriver
import os

@pytest.fixture(scope="function")
def setup_browser():
    """Setup LambdaTest remote browser"""
    
    # Get credentials from environment variables
    username = os.getenv("LT_USERNAME", "YOUR_LAMBDATEST_USERNAME")
    access_key = os.getenv("LT_ACCESS_KEY", "YOUR_LAMBDATEST_ACCESS_KEY")
    
    # LambdaTest Hub URL
    hub_url = f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub"
    
    # Desired capabilities
    capabilities = {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "platformName": "Windows 11",
        "build": "Amazon Product Tests",
        "name": "Parallel Amazon Test",
        "network": True,
        "visual": True,
        "video": True,
        "console": True,
    }
    
    driver = webdriver.Remote(
        command_executor=hub_url,
        desired_capabilities=capabilities
    )
    
    yield driver
    driver.quit()
```

### Step 5: Set Environment Variables

```bash
# Windows (PowerShell)
$env:LT_USERNAME="your_username"
$env:LT_ACCESS_KEY="your_access_key"

# Windows (CMD)
set LT_USERNAME=your_username
set LT_ACCESS_KEY=your_access_key

# Mac/Linux
export LT_USERNAME="your_username"
export LT_ACCESS_KEY="your_access_key"
```

### Step 6: Run Tests on LambdaTest

```bash
pytest test_amazon.py -v -s -n 2 --basetemp=pytest-temp
```

### Step 7: View Results

1. Go to your LambdaTest Dashboard
2. Navigate to **Automation** → **Build**
3. View test execution, screenshots, videos, and logs

## 📝 Test Details

### Test Case 1: iPhone Search
- Navigates to Amazon.com
- Searches for "iPhone"
- Clicks on the first relevant product
- Extracts and prints the price
- Adds product to cart

### Test Case 2: Galaxy Search
- Navigates to Amazon.com
- Searches for "Galaxy phone"
- Clicks on the first relevant product
- Extracts and prints the price
- Adds product to cart

## ⚠️ Important Notes

1. **Amazon Website Changes:** Amazon frequently updates their UI. If tests fail due to element not found, the CSS selectors may need updating.

2. **Parallel Execution:** Tests run in parallel using pytest-xdist. Output is captured in `test_output.txt` and displayed after completion.

3. **Implicit Waits:** Tests include wait times for page loads and element visibility. Slow internet connections may require increasing timeout values.

4. **Rate Limiting:** Running tests too frequently may trigger Amazon's anti-bot mechanisms. Add delays if needed.

## 🐛 Troubleshooting

### Issue: Tests fail with "Element not found"
**Solution:** Amazon's UI may have changed. Update CSS selectors in `test_amazon.py`.

### Issue: ChromeDriver version mismatch
**Solution:** webdriver-manager automatically handles this. If issues persist, update:
```bash
pip install --upgrade webdriver-manager
```

### Issue: Parallel tests not showing output
**Solution:** The test results are saved to `test_output.txt` and displayed at the end via pytest hook.

### Issue: Tests too slow
**Solution:** Increase parallel workers:
```bash
pytest test_amazon.py -v -s -n 4
```

## 📞 Support

For any issues or questions, please create an issue in this repository.

## 📄 License

This project is for educational purposes.

---

**Happy Testing! 🎉**

# 🧪 QA Automation Framework — Selenium + Python

A beginner-friendly end-to-end UI test automation project built with **Selenium WebDriver**, **Python**, **Pytest**, and **Page Object Model (POM)** design pattern.

## 📁 Project Structure

```
qa_automation_project/
├── config/
│   └── config.py            # Browser & URL configurations
├── pages/
│   ├── base_page.py         # Base class with common methods
│   ├── login_page.py        # Login page object
│   └── dashboard_page.py    # Dashboard page object
├── tests/
│   ├── conftest.py          # Pytest fixtures (setup/teardown)
│   ├── test_login.py        # Login test cases
│   └── test_navigation.py   # Navigation test cases
├── utils/
│   ├── logger.py            # Custom logging utility
│   └── screenshot.py        # Screenshot on failure utility
├── reports/                 # HTML test reports go here
├── requirements.txt         # Python dependencies
└── pytest.ini               # Pytest configuration
```

## 🚀 Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Programming language |
| Selenium WebDriver | Browser automation |
| Pytest | Test framework |
| pytest-html | HTML test reports |
| Page Object Model | Design pattern |

## ⚙️ Setup & Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/qa-automation-framework.git
cd qa-automation-framework

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run all tests
pytest tests/ --html=reports/report.html --self-contained-html

# 5. Run a specific test file
pytest tests/test_login.py -v

# 6. Run tests with logging
pytest tests/ -v --tb=short
```

## 🧩 Key Concepts Demonstrated

- ✅ **Page Object Model (POM)** — Separates test logic from UI interactions
- ✅ **Fixtures** — Reusable setup/teardown with `conftest.py`
- ✅ **Explicit Waits** — Reliable element synchronization
- ✅ **Screenshot on Failure** — Auto-captures failed test screenshots
- ✅ **HTML Reports** — Clean test execution reports
- ✅ **Config Management** — Centralized browser/URL settings
- ✅ **Logging** — Custom logger for debugging

## 🌐 Test Site

Tests run against [https://the-internet.herokuapp.com](https://the-internet.herokuapp.com) — a free, public site built for automation practice.

## 📊 Sample Test Cases

| Test ID | Test Name | Status |
|---------|-----------|--------|
| TC_001 | Valid Login | ✅ Pass |
| TC_002 | Invalid Login - Wrong Password | ✅ Pass |
| TC_003 | Login with Empty Fields | ✅ Pass |
| TC_004 | Logout Functionality | ✅ Pass |
| TC_005 | Page Title Verification | ✅ Pass |

## 👤 Author

**Your Name**  
QA Automation Engineer  
[LinkedIn](https://linkedin.com) | [GitHub](https://github.com)

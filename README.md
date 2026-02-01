# Banking-Application-Automation-Testing-Framework
📌 Project Overview

This project is a Selenium Automation Testing Framework built using Python, PyTest, and Page Object Model (POM) to validate core functionalities of a banking web application.
It simulates real-world banking scenarios such as login validation and fund transfer flow validation, with professional reporting using Allure HTML Reports.

The framework is designed to be scalable, maintainable, and recruiter-ready, following industry best practices used in enterprise QA teams.

🎯 Objectives

Automate functional and regression testing for a banking application

Validate critical user flows like authentication and dashboard access

Generate interactive and detailed test execution reports

Demonstrate real-world QA automation skills for interviews

🛠️ Tech Stack

Language: Python 3.13

Automation Tool: Selenium WebDriver

Test Framework: PyTest

Design Pattern: Page Object Model (POM)

Reporting: Allure HTML Reports

Browser: Google Chrome

Driver Management: WebDriver Manager

📂 Project Structure
Automation_Banking_Project/
│
├── pages/
│   ├── login_page.py
│   └── dashboard_page.py
│
├── tests/
│   ├── test_login.py
│   └── test_fund_transfer.py
│
├── allure-results/
├── screenshots/
├── venv/
├── requirements.txt
└── README.md

🧩 Framework Design (POM)

Each web page is represented as a separate Python class

Locators and actions are isolated from test logic

Improves maintainability and reusability

Reduces test failure impact when UI changes

✅ Test Scenarios Covered
🔐 Login Validation

Verify successful login with valid credentials

Confirm dashboard loads after authentication

💰 Fund Transfer Simulation

Validate post-login dashboard availability

Simulate fund transfer flow (demo application)

Ensure page integrity and navigation

⏱️ Synchronization Strategy

Explicit waits using WebDriverWait

Handles dynamic page loading

Prevents flaky test execution

📊 Reporting with Allure

Generates interactive HTML reports

Displays:

Test status (Pass/Fail)

Execution time

Test steps and severity

Useful for QA teams and stakeholders

Run tests with Allure:
pytest -v --alluredir=allure-results

View Allure report:
allure serve allure-results

🔁 Regression Testing

This framework supports regression testing, ensuring that existing functionalities remain unaffected after new changes or enhancements.

🚀 How to Run the Project
1️⃣ Clone or copy the project
git clone <repository-url>

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Execute tests
pytest -v

📈 Why This Project Is Recruiter-Attractive

Uses industry-standard automation tools

Implements Page Object Model

Includes reporting with Allure

Handles real-world issues like waits and imports

Suitable for banking and enterprise applications

🧠 Interview Talking Point

“I developed a Selenium-PyTest automation framework using Page Object Model for a banking application and integrated Allure reporting to generate detailed HTML reports for regression testing.”

👩‍💻 Author

Gopika
Automation Testing | Selenium | PyTest | QA Engineer
<img width="1917" height="948" alt="image" src="https://github.com/user-attachments/assets/817b98f8-17bb-4364-9e3e-a1132c05f03d" />


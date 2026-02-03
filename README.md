# Banking Automation Testing Framework

## 🚀 Project Overview

This project is a **professional automation testing framework** for a digital banking application.  
It covers **UI automation, API testing, and database validation**, providing **end-to-end test coverage** with modern CI/CD practices.  

---

## 🎯 Objectives

- Automate **login, account management, fund transfer, and transaction history**.
- Validate **fund transfer logic** through **UI + DB integration**.
- Ensure **data consistency** between front-end and database.
- Implement **insufficient balance checks**.
- Integrate with **CI/CD pipelines** and **Allure reporting**.

---

## 🏦 Application Modules Automated

1. **Login & Security Testing**
   - Valid / Invalid login
   - OTP simulation
   - Session timeout handling
   - CAPTCHA simulation

2. **Account Dashboard Validation**
   - Balance display
   - Recent transactions
   - Account number masking

3. **Fund Transfer Module**
   - Add beneficiary
   - Transfer funds
   - Validate success message
   - Database validation

4. **Transaction History**
   - UI vs DB comparison
   - Date-range filtering
   - Export report testing

5. **API Testing**
   - Login API
   - Transfer API
   - Balance API
   - Transaction API

6. **Database Testing**
   - Validate transactions stored correctly
   - Validate balance updates
   - Insufficient balance scenarios

---

## 🛠 Tech Stack

| Area | Tools / Framework |
|------|------------------|
| UI Automation | Selenium + Python |
| API Testing | PyTest + Requests |
| Database | MySQL / PostgreSQL |
| Framework | Hybrid (POM + Data-Driven) |
| Reporting | Allure / Extent Reports |
| CI/CD | GitHub Actions / Azure DevOps |
| Version Control | Git |

---

## 💾 Database Setup

1. Install **MySQL Community Server**  
2. Open **MySQL Workbench**  
3. Create **Test Database:**

```sql
CREATE DATABASE banking_test;
USE banking_test;
Create customers table:

CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    balance DECIMAL(10,2)
);
Insert test users:

INSERT INTO customers (name, email, balance) VALUES 
('Test User','testuser@gmail.com',5000.00),
('Receiver','receiver@gmail.com',2000.00);
⚙️ How to Run
1️⃣ Setup Python Environment
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
2️⃣ Run Tests
a) Database Tests
pytest tests/test_db_fund_transfer.py -v
pytest tests/test_db_insufficient_balance.py -v
b) UI + DB Integration Tests
pytest tests/test_ui_db_fund_transfer.py -v
3️⃣ Generate Allure Reports
pytest --alluredir=reports
allure serve reports
📁 Project Structure
Automation_Banking_Project/
│
├─ db/                  # DB utilities and connectors
├─ tests/               # Test scripts (UI, DB, API)
├─ pages/               # POM classes for Selenium
├─ reports/             # Allure reports
├─ .github/workflows/   # CI/CD GitHub Actions
├─ requirements.txt
├─ README.md
🔧 CI/CD Integration
GitHub Actions configured to:

Run DB & UI tests on push / pull request

Generate Allure reports

Fail build if any critical test fails

🧠 Key Learning Outcomes
Full-stack automation: UI + API + DB

Hybrid framework design (POM + Data-driven)

Transaction-level DB testing with MySQL

Insufficient balance handling

CI/CD with GitHub Actions

Allure reporting for professional dashboards

“I designed a professional automation framework for digital banking, integrating Selenium, PyTest, MySQL, API testing, and CI/CD pipelines.
It validates end-to-end business scenarios including fund transfer, account management, and transaction history, ensuring consistency between UI and database, while providing Allure reports for actionable insights.”



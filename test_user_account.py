from seleniumbase import BaseCase
from datetime import datetime

class UserAccountTests (BaseCase):
    def test_register_new_user(self):
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        email = f"testuser{now}@example.com"
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='signup-name']", "Test User")
        self.type("input[data-qa='signup-email']", "testuser12345@example.com")
        self.click("button[data-qa='signup-button']")
        self.assert_text("ENTER ACCOUNT INFORMATION", "h2")
        
    def test_register_existing_email(self):
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='signup-name']", "Test User")
        self.type("input[data-qa='signup-email']", "testuser12345@example.com")  # email đã dùng ở Test 1
        self.click("button[data-qa='signup-button']")
        self.assert_text("Email Address already exist!", "form")

    def test_login_valid(self):
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='login-email']", "testuser12345@example.com")
        self.type("input[data-qa='login-password']", "123456")
        self.click("button[data-qa='login-button']")
        self.assert_text("Logged in as Test User", "li:nth-of-type(10)")

    def test_login_invalid_password(self):
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='login-email']", "testuser12345@example.com")
        self.type("input[data-qa='login-password']", "saimatkhau")
        self.click("button[data-qa='login-button']")
        self.assert_text("Your email or password is incorrect!", "form")

    def test_logout(self):
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='login-email']", "testuser12345@example.com")
        self.type("input[data-qa='login-password']", "123456")
        self.click("button[data-qa='login-button']")
        self.click("a[href='/logout']")
        self.assert_element("a[href='/login']") 

    def test_display_username_after_login(self):
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='login-email']", "testuser12345@example.com")
        self.type("input[data-qa='login-password']", "123456")
        self.click("button[data-qa='login-button']")
        self.assert_text("Logged in as Test User", "li:nth-of-type(10)")

    def test_login_multiple_invalid_attempts(self):
        self.open("https://automationexercise.com")
        for i in range(3):
            self.click("a[href='/login']")
            self.type("input[data-qa='login-email']", "testuser12345@example.com")
            self.type("input[data-qa='login-password']", f"wrongpass{i}")
            self.click("button[data-qa='login-button']")
            self.assert_text("Your email or password is incorrect!", "form")
            self.go_back()

    def test_invalid_email_format(self):
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='signup-name']", "Tester")
        self.type("input[data-qa='signup-email']", "email-sai-dinh-dang")  
        self.click("button[data-qa='signup-button']")
        self.assert_text("Signup", "h2")  

    def test_empty_fields_registration(self):
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.click("button[data-qa='signup-button']")  
        self.assert_text("Signup", "h2")  

    def test_delete_account(self):
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='login-email']", "testuser12345@example.com")
        self.type("input[data-qa='login-password']", "123456")
        self.click("button[data-qa='login-button']")
        self.click("a[href='/delete_account']")
        self.assert_text("ACCOUNT DELETED!", "h2")

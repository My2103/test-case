from seleniumbase import BaseCase
from datetime import datetime

class UserAccountTests (BaseCase):
    def test_register_new_user(self):
        # Test 1: New user registration successful
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        email = f"testuser{now}@example.com"
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='signup-name']", "Diem My")
        self.type("input[data-qa='signup-email']", "diemmy123@gmail.com")
        self.click("button[data-qa='signup-button']")
        self.assert_text("ENTER ACCOUNT INFORMATION", "h2")
        
    def test_register_existing_email(self):
        # Test 2: Sign up with an existing email
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='signup-name']", "Diem My")
        self.type("input[data-qa='signup-email']", "diemmy123@gmail.com")  
        self.click("button[data-qa='signup-button']")
        self.assert_text("Email Address already exist!", "form")

    def test_login_valid(self):
        # Test 3: Login with valid information
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='login-email']", "diemmy123@gmail.com")
        self.type("input[data-qa='login-password']", "21032004")
        self.click("button[data-qa='login-button']")
        self.assert_text("Logged in as Test User", "li:nth-of-type(10)")

    def test_login_invalid_password(self):
        # Test 4: Login with wrong password
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='login-email']", "diemmy123@gmail.com")
        self.type("input[data-qa='login-password']", "12345")
        self.click("button[data-qa='login-button']")
        self.assert_text("Your email or password is incorrect!", "form")

    def test_logout(self):
        # Test 5: Log out
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='login-email']", "diemmy123@gmail.com")
        self.type("input[data-qa='login-password']", "21032004")
        self.click("button[data-qa='login-button']")
        self.click("a[href='/logout']")
        self.assert_element("a[href='/login']") 

    def test_display_username_after_login(self):
        # Test 6: Check username display after login
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='login-email']", "diemmy123@gmail.com")
        self.type("input[data-qa='login-password']", "21032004")
        self.click("button[data-qa='login-button']")
        self.assert_text("Logged in as Test User", "li:nth-of-type(10)")

    def test_login_multiple_invalid_attempts(self):
        # Test 7: Check when logging in incorrectly multiple times in a row 
        self.open("https://automationexercise.com")
        for i in range(3):
            self.click("a[href='/login']")
            self.type("input[data-qa='login-email']", "diemmy123@gmail.com")
            self.type("input[data-qa='login-password']", f"wrongpass{i}")
            self.click("button[data-qa='login-button']")
            self.assert_text("Your email or password is incorrect!", "form")
            self.go_back()

    def test_invalid_email_format(self):
        # Test 8: Check for errors when entering email in wrong format
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='signup-name']", "Diem My")
        self.type("input[data-qa='signup-email']", "diemmy_@-gmail.com")  
        self.click("button[data-qa='signup-button']")
        self.assert_text("Signup", "h2")  

    def test_empty_fields_registration(self):
        # Test 9: Check when leaving information field blank
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.click("button[data-qa='signup-button']")  
        self.assert_text("Signup", "h2")  

    def test_delete_account(self):
        # Test 10: Test account deletion function
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='login-email']", "diemmy123@gmail.com")
        self.type("input[data-qa='login-password']", "21032004")
        self.click("button[data-qa='login-button']")
        self.click("a[href='/delete_account']")
        self.assert_text("ACCOUNT DELETED!", "h2")

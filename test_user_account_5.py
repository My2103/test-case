from seleniumbase import BaseCase
from datetime import datetime

class UserAccountTests(BaseCase):
    def register_user_if_needed(self, name, email, password, force_create=False):
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='signup-name']", name)
        self.type("input[data-qa='signup-email']", email)
        self.click("button[data-qa='signup-button']")

        if self.is_text_visible("Email Address already exist!") and not force_create:
            print("Account already exists. Skipping creation.")
            return

        # Enter form create account
        self.click("input[id='id_gender2']")
        self.type("input[id='password']", password)
        self.select_option_by_text("select[id='days']", "9")
        self.select_option_by_text("select[id='months']", "May")
        self.select_option_by_text("select[id='years']", "2000")
        self.type("input[id='first_name']", "Diem")
        self.type("input[id='last_name']", "My")
        self.type("input[id='company']", "MyCompany")
        self.type("input[id='address1']", "123 Street")
        self.type("input[id='address2']", "Ward 1")
        self.select_option_by_text("select[id='country']", "India")
        self.type("input[id='state']", "HCM")
        self.type("input[id='city']", "Ho Chi Minh")
        self.type("input[id='zipcode']", "700000")
        self.type("input[id='mobile_number']", "0987654321")
        self.click("button[data-qa='create-account']")
        self.assert_text("ACCOUNT CREATED!", "h2")
        self.click("a[data-qa='continue-button']")


    def test_register_new_user(self):
        # Test 1: New user registration successful with full form
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        email = f"testuser{now}@example.com"
        password = "Test@1234"
        self.register_user_if_needed("Diem My", email, password, force_create=True)
        self.assert_element("a[href='/logout']")  

    def test_register_existing_email(self):
        # Test 2: Sign up with an existing email
        self.register_user_if_needed("Diem My", "diemmy123@gmail.com", "21032004")
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='signup-name']", "Diem My")
        self.type("input[data-qa='signup-email']", "diemmy123@gmail.com")  
        self.click("button[data-qa='signup-button']")
        self.assert_text_visible("Email Address already exist!")

    def test_login_valid(self):
        # Test 3: Login with valid information
        self.register_user_if_needed("Diem My", "diemmy123@gmail.com", "21032004")
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='login-email']", "diemmy123@gmail.com")
        self.type("input[data-qa='login-password']", "21032004")
        self.click("button[data-qa='login-button']")
        self.assert_text("Logged in as Diem My", "li:nth-of-type(10)")

    def test_login_invalid_password(self):
        # Test 4: Login with wrong password
        self.register_user_if_needed("Diem My", "diemmy123@gmail.com", "21032004")
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='login-email']", "diemmy123@gmail.com")
        self.type("input[data-qa='login-password']", "12345")
        self.click("button[data-qa='login-button']")
        self.assert_text("Your email or password is incorrect!", "form")

    def test_logout(self):
        # Test 5: Log out
        self.register_user_if_needed("Diem My", "diemmy123@gmail.com", "21032004")
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='login-email']", "diemmy123@gmail.com")
        self.type("input[data-qa='login-password']", "21032004")
        self.click("button[data-qa='login-button']")
        self.assert_text("Logged in as Diem My")
        self.click("a[href='/logout']")
        self.assert_element("a[href='/login']")

    def test_display_username_after_login(self):
        # Test 6: Check username display after login
        self.register_user_if_needed("Diem My", "diemmy123@gmail.com", "21032004")
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='login-email']", "diemmy123@gmail.com")
        self.type("input[data-qa='login-password']", "21032004")
        self.click("button[data-qa='login-button']")
        
        self.assert_text("Logged in as Diem My", "li:nth-of-type(10)")

    def test_login_multiple_invalid_attempts(self):
        # Test 7: Check when logging in incorrectly multiple times in a row 
        self.register_user_if_needed("Diem My", "diemmy123@gmail.com", "21032004")
        self.open("https://automationexercise.com")
        for i in range(3):
            self.click("a[href='/login']")
            self.type("input[data-qa='login-email']", "diemmy123@gmail.com")
            self.type("input[data-qa='login-password']", f"wrongpass{i}")
            self.click("button[data-qa='login-button']")
            self.assert_text("Your email or password is incorrect!", "form")
            self.go_back()

    def test_account_lock_after_multiple_failed_logins(self):
        # Test 8: Check account lock after after multiple failed logins 
        email = "diemmy123@gmail.com"
        correct_password = "21032004"

        # Make sure account was created
        self.register_user_if_needed("Diem My", email, correct_password)

        self.open("https://automationexercise.com")

        # Enter wrong password 5 times
        for i in range(5):
            self.click("a[href='/login']")
            self.type("input[data-qa='login-email']", email)
            self.type("input[data-qa='login-password']", f"wrongpass{i}")
            self.click("button[data-qa='login-button']")
            self.assert_text("Your email or password is incorrect!", "form")
            self.go_back()

        # After 5 times, check if the account locked or not
        self.click("a[href='/login']")
        self.type("input[data-qa='login-email']", email)
        self.type("input[data-qa='login-password']", correct_password)
        self.click("button[data-qa='login-button']")

        # Expected account was locked wil display "Your account has been locked due to multiple failed attempts"
        self.assert_text_contains("locked", "form")

    def test_invalid_email_format(self):
        # Test 9: Check for errors when entering email in wrong format
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        invalid_emails = ["diemmy_@-gmail.com", "diemmy@", "@gmail.com"]
        self.type("input[data-qa='signup-name']", "Diem My")
        self.type("input[data-qa='signup-email']", "diemmy_@-gmail.com")  
        self.click("button[data-qa='signup-button']")
        is_valid = self.execute_script(
            "return document.querySelector('input[data-qa=\"signup-email\"]').checkValidity();"
        )
        self.assert_false(is_valid)

        self.assert_equal(self.get_current_url(), "https://automationexercise.com/login")
        

    def test_empty_fields_registration(self):
        # Test 10: Check when leaving information field blank
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.click("button[data-qa='signup-button']")
        is_name_valid = self.execute_script(
            "return document.querySelector('input[data-qa=\"signup-name\"]').checkValidity();"
        )
        is_email_valid = self.execute_script(
            "return document.querySelector('input[data-qa=\"signup-email\"]').checkValidity();"
        )
        self.assert_false(is_name_valid)
        self.assert_false(is_email_valid)

        # Kiểm tra không chuyển trang
        self.assert_equal(self.get_current_url(), "https://automationexercise.com/login")
        

    def test_delete_account(self):
        # Test 11: Test account deletion function
        self.register_user_if_needed("Diem My", "diemmy123@gmail.com", "21032004")
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='login-email']", "diemmy123@gmail.com")
        self.type("input[data-qa='login-password']", "21032004")
        self.click("button[data-qa='login-button']")
        self.click("a[href='/delete_account']")
        self.assert_text("ACCOUNT DELETED!", "h2")
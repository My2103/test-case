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
            return

        # Fill account info form
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

    def login_user(self, email, password):
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='login-email']", email)
        self.type("input[data-qa='login-password']", password)
        self.click("button[data-qa='login-button']")

    def test_register_new_user(self):
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        email = f"testuser{now}@example.com"
        self.register_user_if_needed("Diem My", email, "Test@1234", force_create=True)
        self.assert_element("a[href='/logout']")

    def test_register_existing_email(self):
        # Test 2: Sign up with an existing email
        self.register_user_if_needed("Diem My", "diemmy123@gmail.com", "21032004")
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='signup-name']", "Diem My")
        self.type("input[data-qa='signup-email']", "diemmy123@gmail.com")  
        self.click("button[data-qa='signup-button']")
        self.assert_text("Email Address already exist!")

    def test_login_valid(self):
        self.register_user_if_needed("Diem My", "diemmy123@gmail.com", "21032004")
        self.login_user("diemmy123@gmail.com", "21032004")
        self.assert_text("Logged in as Diem My", "li:nth-of-type(10)")

    def test_login_invalid_password(self):
        self.register_user_if_needed("Diem My", "diemmy123@gmail.com", "21032004")
        self.login_user("diemmy123@gmail.com", "wrongpass")
        self.assert_text("Your email or password is incorrect!", "form")

    def test_logout(self):
        self.register_user_if_needed("Diem My", "diemmy123@gmail.com", "21032004")
        self.login_user("diemmy123@gmail.com", "21032004")
        self.click("a[href='/logout']")
        self.assert_element("a[href='/login']") 

    def test_display_username_after_login(self):
        # Test 6: Check username display after login
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        email = f"displayuser{now}@example.com"
        self.register_user_if_needed("Diem My", email, "21032004", force_create=True)
        self.login_user(email, "21032004")
        self.wait_for_text("Logged in as")

    def test_login_multiple_invalid_attempts(self):
        self.register_user_if_needed("Diem My", "diemmy123@gmail.com", "21032004")
        for i in range(3):
            self.login_user("diemmy123@gmail.com", f"wrongpass{i}")
            self.assert_text("Your email or password is incorrect!", "form")

    def test_invalid_email_format(self):
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.type("input[data-qa='signup-name']", "Diem My")
        self.type("input[data-qa='signup-email']", "invalid-email-format")
        self.click("button[data-qa='signup-button']")
        self.assert_element("input[data-qa='signup-email']:invalid")

    def test_empty_fields_registration(self):
        self.open("https://automationexercise.com")
        self.click("a[href='/login']")
        self.click("button[data-qa='signup-button']")
        self.assert_element("input[data-qa='signup-name']:invalid")

    def test_delete_account(self):
        self.register_user_if_needed("Diem My", "diemmy123@gmail.com", "21032004")
        self.login_user("diemmy123@gmail.com", "21032004")
        self.click("a[href='/delete_account']")
        self.assert_text("ACCOUNT DELETED!", "h2")

from seleniumbase import BaseCase

class NavigationMenuTest(BaseCase):
    def test_navigation_menu(self):
        # List of screen sizes to check
        viewports = [
            {"name": "Desktop 1920x1080", "width": 1920, "height": 1080},
            {"name": "Tablet 768x1024", "width": 768, "height": 1024},
            {"name": "Mobile 414x896", "width": 414, "height": 896},
        ]

        # Menu items to test with their expected URLs
        menu_items = [
            {"name": "Home", "selector": "a[href='/']", "expected_url": "https://automationexercise.com/"},
            {"name": "Products", "selector": "a[href='/products']", "expected_url": "https://automationexercise.com/products"},
            {"name": "Cart", "selector": "a[href='/view_cart']", "expected_url": "https://automationexercise.com/view_cart"},
            {"name": "Signup/Login", "selector": "a[href='/login']", "expected_url": "https://automationexercise.com/login"},
        ]

        # Visit website
        self.open("https://automationexercise.com")

        # Handle pop-up if present (e.g., subscription or ad pop-up)
        self.click_if_visible(".close-modal", timeout=5)  # Adjust selector if needed

        for viewport in viewports:
            print(f"Checking navigation menu on: {viewport['name']}")
            
            # Set screen size
            self.set_window_size(viewport["width"], viewport["height"])

            # On mobile, click hamburger menu if present
            if viewport["width"] <= 414:  # Mobile viewport
                if self.is_element_visible(".fa.fa-bars"):  # Hamburger menu icon
                    self.click(".fa.fa-bars")
                    self.wait_for_element_visible(".navbar-nav", timeout=5)

            # Check if navigation menu is visible
            self.assert_element_visible(".navbar-nav", timeout=10)

            for item in menu_items:
                print(f"Testing menu item: {item['name']} on {viewport['name']}")

                # Check if menu item is visible and clickable
                self.assert_element_visible(item["selector"], timeout=5)
                self.assert_true(self.is_element_clickable(item["selector"]), 
                               f"Menu item {item['name']} is not clickable on {viewport['name']}")

                # Click menu item and verify URL
                self.click(item["selector"])
                self.assert_equal(self.get_current_url(), item["expected_url"],
                                f"Menu item {item['name']} did not navigate to {item['expected_url']} on {viewport['name']}")

                # Navigate back to home page for next test
                self.open("https://automationexercise.com")
                if viewport["width"] <= 414 and self.is_element_visible(".fa.fa-bars"):
                    self.click(".fa.fa-bars")  # Re-open hamburger menu if needed

            # (Optional) Take a screenshot for visual inspection
            self.save_screenshot(f"nav_menu_{viewport['name'].replace(' ', '_')}.png")
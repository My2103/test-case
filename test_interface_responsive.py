from seleniumbase import BaseCase

class ResponsiveTest(BaseCase):
    def test_responsive_display(self):
        # List of screen sizes to check
        viewports = [
            {"name": "Desktop 1920x1080", "width": 1920, "height": 1080},
            {"name": "Desktop 1366x768", "width": 1366, "height": 768},
            {"name": "Tablet 768x1024", "width": 768, "height": 1024},
            {"name": "Tablet 1024x768", "width": 1024, "height": 768},
            {"name": "Mobile 375x667", "width": 375, "height": 667},
            {"name": "Mobile 414x896", "width": 414, "height": 896},
        ]

        # Visit website
        self.open("https://automationexercise.com")

        for viewport in viewports:
            print(f"Checking: {viewport['name']}")
            
            # Set screen size
            self.set_window_size(viewport["width"], viewport["height"])
            
            # Check the display header
            self.assert_element_visible("header")
            
            # Check the navigation menu
            self.assert_element_visible(".navbar-nav")
            
            # Check the "Add to Cart" button (for example, select the first button)
            self.assert_element_visible(".btn.btn-default.add-to-cart")
            self.assert_true(self.is_element_clickable(".btn.btn-default.add-to-cart"))
            
            # Check footer when scrolling down to the bottom of the page
            self.scroll_to_bottom()
            self.assert_element_visible("footer")
            
            # (Optional) Take a screenshot for visual inspection
            self.save_screenshot(f"responsive_{viewport['name'].replace(' ', '_')}.png")
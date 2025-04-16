from seleniumbase import BaseCase

class BannerTest(BaseCase):
    def test_banner_display(self):
        # List of screen sizes to check
        viewports = [
            {"name": "Desktop 1920x1080", "width": 1920, "height": 1080},
            {"name": "Tablet 768x1024", "width": 768, "height": 1024},
            {"name": "Mobile 414x896", "width": 414, "height": 896},
        ]

        # Visit website
        self.open("https://automationexercise.com")

        # Handle pop-up if present (e.g., subscription or ad pop-up)
        self.click_if_visible(".close-modal", timeout=5)  # Adjust selector if needed

        for viewport in viewports:
            print(f"Checking banner on: {viewport['name']}")
            
            # Set screen size
            self.set_window_size(viewport["width"], viewport["height"])
            
            # Check if banner container is visible
            self.assert_element_visible("#slider-carousel", timeout=10)
            
            # Check if at least one banner image is visible and loaded
            self.assert_element_visible(".carousel-inner .item img", timeout=10)
            
            # Verify banner image is loaded (check naturalWidth to ensure image is not broken)
            self.assert_true(
                self.execute_script("return document.querySelector('.carousel-inner .item img').naturalWidth > 0"),
                f"Banner image failed to load on {viewport['name']}"
            )
            
            # Check if navigation buttons (next/prev) exist and are clickable (optional)
            if self.is_element_visible(".carousel-control.right"):
                self.assert_element_visible(".carousel-control.right", timeout=5)
                self.assert_true(self.is_element_clickable(".carousel-control.right"))
                # Test navigation by clicking next button and verifying new slide
                self.click(".carousel-control.right")
                self.wait_for_element_visible(".carousel-inner .item.active", timeout=5)
            else:
                print(f"No next button (.carousel-control.right) found on {viewport['name']}")

            if self.is_element_visible(".carousel-control.left"):
                self.assert_element_visible(".carousel-control.left", timeout=5)
                self.assert_true(self.is_element_clickable(".carousel-control.left"))
            else:
                print(f"No prev button (.carousel-control.left) found on {viewport['name']}")
            
            # (Optional) Take a screenshot for visual inspection
            self.save_screenshot(f"banner_{viewport['name'].replace(' ', '_')}.png")
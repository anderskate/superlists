from .base import FunctionalTest

from selenium.webdriver.common.keys import Keys

from unittest import skip


class LayoutAndStylingTest(FunctionalTest):
    """Test for template and style."""

    @skip
    def test_layout_and_styling(self):
        """Layout and Style Test."""
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            273,
            delta=10,
        )

        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            273,
            delta=10,
        )

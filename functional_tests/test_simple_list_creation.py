from .base import FunctionalTest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):
    """Test new visitor."""

    def test_can_start_a_list_for_one_user(self):
        """Check that you can create a list with tasks and get it later."""
        self.browser.get(self.live_server_url)

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Buy a peals')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy a peals')

        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy a pen')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy a peals')
        self.wait_for_row_in_list_table('2: Buy a pen')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        """Multiple users can start lists at different urls."""
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy peals')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peals')

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peals', page_text)
        self.assertNotIn('Buy a pen', page_text)

        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peals', page_text)
        self.assertIn('Buy milk', page_text)

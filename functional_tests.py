from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    """Test new visitor."""

    def setUp(self):
        """Install."""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """After tests."""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Check that you can create a list with tasks and get it later."""
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Buy a peals')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy a peals', [row.text for row in rows])

        self.fail('The end of test')


if __name__ == '__main__':
    unittest.main()

from selenium import webdriver
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
        self.fail('The end of test')


if __name__ == '__main__':
    unittest.main()

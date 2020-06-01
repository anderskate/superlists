from selenium.webdriver.common.keys import Keys

from unittest import skip

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    """Test validation list items."""

    @skip
    def test_cannot_add_empty_list_items(self):
        """Test that cannot add empty list items."""

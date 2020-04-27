from django.urls import resolve
from django.test import TestCase
from lists.views import home_page


class HomePageTest(TestCase):
    """Test home page."""

    def test_root_url_resolves_to_home_page_view(self):
        """Check that main url convert to main page view."""
        found = resolve('/')
        self.assertEqual(found.func, home_page)



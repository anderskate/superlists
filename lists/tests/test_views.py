from django.test import TestCase
from lists.models import Item, List


class HomePageTest(TestCase):
    """Test home page."""

    def test_home_page_returns_correct_html(self):
        """The home page return a correct html"""
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')


class ListViewTest(TestCase):
    """Test representation a list"""

    def test_uses_list_template(self):
        """Check that is used list template."""
        list_ = List.objects.create()
        response = self.client.get(f'/lists/{list_.id}/')
        self.assertTemplateUsed(response, 'list.html')

    def test_passes_correct_list_to_template(self):
        """Test: Pass the correct list to template."""
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get(f'/lists/{correct_list.id}/')
        self.assertEqual(response.context['list'], correct_list)

    def test_displays_all_items(self):
        """Check that all list items displays."""
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=correct_list)
        Item.objects.create(text='itemey 2', list=correct_list)
        other_list = List.objects.create()
        Item.objects.create(text='Different element 1', list=other_list)
        Item.objects.create(text='Different element 2', list=other_list)

        response = self.client.get(f'/lists/{correct_list.id}/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'Different element 1')
        self.assertNotContains(response, 'Different element 2')

    def test_can_save_a_post_request_to_an_existing_list(self):
        """Test that can save post-request in existing list."""
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(
            f'/lists/{correct_list.id}/',
            data={'item_text': 'A new item for an existing list'}
        )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_post_redirects_to_list_view(self):
        """Test: redirect in list view."""
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
            f'/lists/{correct_list.id}/',
            data={'item_text': 'A new item for an existing list'},
        )
        self.assertRedirects(response, f'/lists/{correct_list.id}/')

    def test_validation_errors_end_up_on_lists_page(self):
        """Test validation error in list page."""
        list_ = List.objects.create()
        response = self.client.post(
            f'/lists/{list_.id}/',
            data={'item_text': ''}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')
        expected_error = 'You cant have an empty list item'
        self.assertContains(response, expected_error)

class NewListTest(TestCase):
    """Test new list"""

    def test_can_save_a_post_request(self):
        """Check that you can save post request."""
        self.client.post('/lists/new', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_post(self):
        """Check that after post request redirect is successful."""
        response = self.client.post(
            '/lists/new',
            data={'item_text': 'A new list item'},
        )
        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}/')

    def test_validation_errors_are_sent_back_to_home_page_template(self):
        """Test that template home page gets validation errors."""
        response = self.client.post('/lists/new', data={'item_text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        expected_error = 'You cant have an empty list item'
        self.assertContains(response, expected_error)

    def test_invalid_list_items_arent_saved(self):
        """Test that invalid list items aren't save."""
        self.client.post('/lists/new', data={'item_text': ''})
        self.assertEqual(List.objects.count(), 0)
        self.assertEqual(Item.objects.count(), 0)

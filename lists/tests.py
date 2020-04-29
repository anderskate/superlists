from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item

from lists.views import home_page


class HomePageTest(TestCase):
    """Test home page."""

    def test_home_page_returns_correct_html(self):
        """The home page return a correct html"""
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):
    """Test element list in model."""

    def test_saving_and_retrieving_items(self):
        """Check that list elements can save and get."""
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')


class ListViewSet(TestCase):
    """Test representation a list"""

    def test_uses_list_template(self):
        """Check that is used list template."""
        response = self.client.get('/lists/one_list_in_the_world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        """Check that all list items displays."""
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/one_list_in_the_world/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')


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

        self.assertRedirects(response, '/lists/one_list_in_the_world/')



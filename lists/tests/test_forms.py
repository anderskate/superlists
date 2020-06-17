from django.test import TestCase
from lists.forms import EMPTY_ITEM_ERROR, ItemForm


class ItemFormTest(TestCase):
    """Test form to list element."""

    def test_form_renders_item_text_input(self):
        """Test: Form represent text input field."""
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        """Test form validation for empty elements."""
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERROR])

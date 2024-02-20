from django.test import TestCase
from django.contrib.auth.models import User
from notes_app.models import Note

class NoteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create_user(username='testuser', password='12345')
        Note.objects.create(title='Test Note', content='Just a test note.', owner=User.objects.get(id=1))

    def test_note_content(self):
        note = Note.objects.get(id=1)
        expected_object_name = f'{note.content}'
        self.assertEquals(expected_object_name, 'Just a test note.')

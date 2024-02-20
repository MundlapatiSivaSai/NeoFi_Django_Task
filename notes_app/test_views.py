from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from notes_app.models import Note
from notes_app.serializers import NoteSerializer

class NoteAPIViewTest(TestCase):
    """ Test module for GET all notes API """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.note = Note.objects.create(title='Test Note', content='Just a test note.', owner=self.user)
        self.url = reverse('note-list')

    def test_get_all_notes(self):
        # Get API response
        response = self.client.get(self.url)
        # Get data from db
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

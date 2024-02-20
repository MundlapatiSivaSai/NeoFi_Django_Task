from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, NoteSerializer, NoteVersionSerializer
from .models import Note, NoteVersion

# Home view
def home(request):
    return HttpResponse("Welcome to the Notes App by SivaSai Mundlapati !")

def api_overview(request):
    return HttpResponse("API Overview")


@api_view(['POST'])
def signup_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_note_view(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def share_note_view(request):
    note_id = request.data.get('note_id')
    shared_with_emails = request.data.get('shared_with', [])
    note = Note.objects.filter(id=note_id, owner=request.user).first()
    
    if note:
        shared_users = User.objects.filter(email__in=shared_with_emails)
        for user in shared_users:
            # Assuming you have a method or process to share notes
            # This might need adjustment based on your actual model relationships
            note.shared_with.add(user)
        return Response({'message': 'Note shared successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid note ID or you are not the owner'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_note_version_history(request, id):
    note = Note.objects.filter(id=id, owner=request.user).first()
    if note:
        versions = NoteVersion.objects.filter(note=note)
        serializer = NoteVersionSerializer(versions, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)

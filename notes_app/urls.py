from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('signup', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('notes/create', views.create_note_view, name='create_note'),
    path('notes/share', views.share_note_view, name='share_note'),
    path('notes/version-history/<int:id>', views.get_note_version_history, name='note_version_history'),
]

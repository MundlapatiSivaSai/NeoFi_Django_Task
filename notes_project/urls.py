from django.urls import path, include
from django.contrib import admin
from notes_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('notes_app.urls')),
    path('', home, name='home'),
]

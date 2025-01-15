from django.urls import path
from . import views

urlpatterns = [
    path('api/notes', views.get_notes, name='get_notes'),
    path('api/notes/save', views.save_all_notes, name='save_all_notes'),
    path('api/notes/update', views.update_all_notes, name='update_all_notes'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_user, name='logout'),
    path('label', views.label, name='label'),
    path('label_notes/<int:label_id>', views.label_notes, name='label_notes'),
    path('create_note', views.create_note, name='create_note'),
    path('edit_note/<int:note_id>', views.edit_note, name='edit_note'),
]
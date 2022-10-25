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
    path('delete_note/<int:note_id>', views.delete_note, name='delete_note'),
    path('edit_label/<int:label_id>', views.edit_label, name='edit_label'),
    path('delete_label/<int:label_id>', views.delete_label, name='delete_label'),
    path('create_label', views.create_label, name='create_label'),
]
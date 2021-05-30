from django.contrib import admin, auth
from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('dialog/show/<int:dialog_pk>/', mainapp.dialog_show, name='dialog_show'),
    path('dialog/create/', mainapp.create_dialog, name='create_dialog'),
    path('user/dialog/create/<int:user_id>/', mainapp.user_dialog_create,
         name='user_dialog_create'),

    path('dialog/member/<int:sender_pk>/message/create/',
         mainapp.DialogMessageCreate.as_view(),
         name='dialog_message_create'),

    path('user/dialog/new/messages/<int:dialog_pk>/',
         mainapp.dialog_new_messages,
         name='dialog_new_messages'),

    path('dialog/delete/message/<int:message_id>', mainapp.delete_dialog, name='delete_dialog'),
]

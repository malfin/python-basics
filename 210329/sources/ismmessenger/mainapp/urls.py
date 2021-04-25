"""messenger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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

    # path('user/dialog/update/<int:user_id>/',
    #      mainapp.dialog_show_update, name='dialog_show_update'),

    path('dialog/delete/message/<int:message_id>', mainapp.delete_dialog, name='delete_dialog'),
]

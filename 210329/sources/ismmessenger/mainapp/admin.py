from django.contrib import admin

from .models import Dialog, DialogMemebers, Message

admin.site.register(Dialog)
admin.site.register(DialogMemebers)
admin.site.register(Message)

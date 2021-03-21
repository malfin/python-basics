from django.contrib.auth.models import User
from django.db import models


class Dialog(models.Model):
    owner = models.ForeignKey(User, verbose_name='cоздатель', on_delete=models.CASCADE)
    opponent = models.ForeignKey(User, verbose_name='cоздатель', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.owner} - {self.opponent}'

    class Meta:
        verbose_name = 'диалог'
        verbose_name_plural = 'диалоги'


class Message(models.Model):
    dialog = models.ForeignKey(Dialog, verbose_name='диалог', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, verbose_name='отправитель', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='сообщение')
    read = models.BooleanField(verbose_name='прочитано', default=False)

    def __str__(self):
        return f'{self.dialog.owner} - {self.sender.username}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

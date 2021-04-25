from django.contrib.auth.models import User
from django.db import models
from django.utils.functional import cached_property


class Dialog(models.Model):
    created = models.DateTimeField(verbose_name='отправлено',
                                   auto_now_add=True,
                                   db_index=True)
    name = models.CharField(verbose_name='имя', max_length=64, blank=True)

    @cached_property
    def get_all_members(self):
        return self.members.all()

    def get_messages_all(self):
        return Message.objects.filter(sender__in=self.get_all_members). \
            select_related('sender__member')

    def get_sender(self, user_id):
        return self.get_all_members.filter(member_id=user_id).first()

    def __str__(self):
        members = User.objects.filter(
            pk__in=self.get_all_members.values_list('member_id', flat=True)). \
            values_list('username', flat=True)
        result = f'{self.created.strftime("%Y.%m.%d %H:%M")} ' \
                 f'({" - ".join(members)})'
        return result

    class Meta:
        verbose_name = 'диалог'
        verbose_name_plural = 'диалоги'
        ordering = ['-created']


class DialogMemebers(models.Model):
    CREATOR = '0'
    INTERLOCUTOR = '1'

    ROLE_CHOICES = (
        (CREATOR, 'создатель'),
        (INTERLOCUTOR, 'собеседник'),
    )

    dialog = models.ForeignKey(Dialog,
                               verbose_name='диалог',
                               on_delete=models.CASCADE,
                               related_name="members")
    member = models.ForeignKey(User,
                               verbose_name='участник диалога',
                               on_delete=models.CASCADE,
                               related_name="dialogs")
    role = models.CharField(verbose_name='роль',
                            choices=ROLE_CHOICES,
                            db_index=True, max_length=128)

    class Meta:
        verbose_name = 'люди в диалоге'
        verbose_name_plural = 'люди в диалогах'
        ordering = ['dialog', '-role', 'member']


class Message(models.Model):
    sender = models.ForeignKey(DialogMemebers,
                               verbose_name='отправитель',
                               on_delete=models.CASCADE)
    text = models.TextField(verbose_name='сообщение')
    read = models.BooleanField(verbose_name='прочитано', default=False)
    created = models.DateTimeField(verbose_name='отправлено',
                                   auto_now_add=True,
                                   db_index=True)

    def __str__(self):
        return f'{self.sender} ({self.created}):\n\t{self.text[:35]}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ['-created']

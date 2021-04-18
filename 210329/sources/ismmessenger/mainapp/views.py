from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from mainapp.forms import Dialogs, MessageCreate
from mainapp.models import Dialog, Message, DialogMemebers


@login_required
def index(request):
    dialogues = request.user.dialogs.all()
    context = {
        'title': 'главная',
        'dialogues': dialogues,
    }
    return render(request, 'mainapp/index.html', context)


@login_required
def dialog_show(request, dialog_pk):
    dialog = get_object_or_404(Dialog, pk=dialog_pk)
    _dialog_members = DialogMemebers.objects.filter(dialog=dialog)
    dialog_members = _dialog_members.exclude(member=request.user). \
        select_related('member')
    dialog_messages = Message.objects.filter(sender__in=_dialog_members). \
        select_related('sender__member')
    context = {
        'title': 'Диалоги',
        'dialog': dialog,
        'dialog_members': dialog_members,
        'dialog_messages': dialog_messages,
    }
    return render(request, 'mainapp/dialog.html', context)


@login_required
def create_dialog(request):
    dialogues = request.user.dialogs.select_related('dialog').all(). \
        values_list('dialog_id', flat=True)
    interlocutors = DialogMemebers.objects.filter(dialog__in=dialogues). \
        values_list('member_id', flat=True)
    new_interlocutors = User.objects.exclude(pk__in=interlocutors)
    context = {
        'title': 'новый диалог',
        'new_interlocutors': new_interlocutors,
    }
    return render(request, 'mainapp/create_dialog.html', context)


@login_required()
def user_dialog_create(request, user_id):
    interlocutor = User.objects.get(pk=user_id)
    dialog = Dialog.objects.create(
        name=interlocutor.username
    )
    DialogMemebers.objects.create(
        dialog=dialog,
        member=request.user,
        role=DialogMemebers.CREATOR
    )
    DialogMemebers.objects.create(
        dialog=dialog,
        member=interlocutor,
        role=DialogMemebers.INTERLOCUTOR
    )
    return HttpResponseRedirect(
        reverse('main:dialog_show', kwargs={'dialog_pk': dialog.pk})
    )


@login_required()
def create_message(request):
    if request.POST == "POST":
        form = MessageCreate(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно отправили сообщение!")
            return HttpResponseRedirect(reverse('main:create_message'))
    else:
        form = MessageCreate()
    context = {
        'title': 'отправить сообщение',
        'form': form,
    }
    print(form)
    return render(request, 'mainapp/create_message.html', context)


@login_required()
def delete_dialog(request, message_id):
    item = Dialog.objects.get(id=message_id)
    item.delete()
    messages.success(request, "Вы успешно удалили диалог!")
    return HttpResponseRedirect(reverse('main:index'))


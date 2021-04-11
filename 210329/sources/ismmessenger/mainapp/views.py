from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from mainapp.forms import Dialogs, DialogsCreate
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
def dialog(request, dialog_pk):
    dialog = get_object_or_404(Dialog, pk=dialog_pk)
    _dialog_members = DialogMemebers.objects.filter(dialog=dialog)
    dialog_members = _dialog_members.exclude(member=request.user). \
        select_related('member')
    dialog_messages = Message.objects.filter(sender__in=_dialog_members). \
        select_related('sender__member')
    context = {
        'title': 'главная',
        'dialog': dialog,
        'dialog_members': dialog_members,
        'dialog_messages': dialog_messages,
    }
    return render(request, 'mainapp/dialog.html', context)


@login_required
def create_dialog(request):
    if request.method == 'POST':
        form = DialogsCreate(request.POST)
        form_2 = Dialogs(request.POST)
        if form.is_valid():
            if request.method == 'POST':
                if form.is_valid():
                    form.save()
                    form_2.save()
                    messages.success(request, 'Вы успешно создали диалог!')
                    return HttpResponseRedirect(reverse('main:index'))
            else:
                messages.error(request, 'В чёт-то ошибка...')
        else:
            messages.error(request, 'В чёт-то ошибка...')
    else:
        form = DialogsCreate()
        form_2 = Dialogs()
    context = {
        'title': 'Создание диалога',
        'form': form,
        'form_2': form_2,
    }
    return render(request, 'mainapp/create_dialog.html', context)

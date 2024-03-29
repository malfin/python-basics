from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from mainapp.forms import DialogMessageForm
from mainapp.models import Dialog, DialogMemebers, Message


@login_required
def index(request):
    dialogues = request.user.dialogs.select_related('dialog').all()
    context = {
        'title': 'диалоги',
        'dialogues': dialogues,
    }

    return render(request, 'mainapp/index.html', context)


def dialog_show(request, dialog_pk):
    dialog = get_object_or_404(Dialog, pk=dialog_pk)
    sender = dialog.get_sender(request.user.pk)

    context = {
        'title': 'диалог',
        'dialog': dialog,
        'sender': sender,
    }

    return render(request, 'mainapp/dialog.html', context)


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


def delete_dialog(request, pk):
    instance = get_object_or_404(Dialog, pk=pk)
    instance.delete()
    return HttpResponseRedirect(reverse('main:index'))


class DialogMessageCreate(CreateView):
    model = Message
    form_class = DialogMessageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        sender_pk = self.request.resolver_match.kwargs['sender_pk']
        form.initial['sender'] = sender_pk

        return context

    def get_success_url(self):
        return reverse(
            'main:dialog_show',
            kwargs={'dialog_pk': self.object.sender.dialog_id}
        )


def dialog_new_messages(request, dialog_pk):
    if request.is_ajax():
        dialog = Dialog.objects.filter(pk=dialog_pk).first()
        status = False
        new_messages = None
        if dialog:
            status = True
            _new_messages = dialog.get_messages_new(request.user.pk)
            new_messages = [
                {'pk': el.pk,
                 'username': el.sender.member.username,
                 'created': el.created.strftime('%Y.%m.%d %H:%M'),
                 'text': el.text}
                for el in _new_messages
            ]
            if _new_messages.update(read=True):
                return JsonResponse({
                    'status': status,
                })

        return JsonResponse({
            'status': status,
            'new_messages': new_messages,
        })
    return HttpResponseRedirect(reverse('main:dialog_show', kwargs={'dialog_pk': dialog_pk}))

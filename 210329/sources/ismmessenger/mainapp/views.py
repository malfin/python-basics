from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import CreateView

from mainapp.forms import DialogMessageForm
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
    sender = dialog.get_sender(request.user.pk)
    context = {
        'title': 'Диалоги',
        'dialog': dialog,
        'sender': sender,
    }
    return render(request, 'mainapp/dialog.html', context)


# def dialog_show_update(request, dialog_pk):
#     if request.is_ajax():
#         dialog = get_object_or_404(Dialog, pk=dialog_pk)
#         sender = dialog.get_sender(request.user.pk)
#         return JsonResponse({
#             'status': 'ok',
#             'sender_id': sender,
#         })


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


@login_required()
def delete_dialog(request, message_id):
    item = get_object_or_404(Dialog, id=message_id)
    item.delete()
    messages.success(request, "Вы успешно удалили диалог!")
    return HttpResponseRedirect(
        reverse('main:index')
    )

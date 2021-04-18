from django import forms

from mainapp.models import Message, DialogMemebers


class MessageCreate(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control {name} form-control-lg mt-2'
            item.widget.attrs['style'] = f'resize: none'
            item.help_text = ''


class Dialogs(forms.ModelForm):
    class Meta:
        model = DialogMemebers
        fields = (
            'dialog',
            'member',
            'role',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control {name} form-control-lg mt-2'
            item.widget.attrs['style'] = f'resize: none'
            item.help_text = ''

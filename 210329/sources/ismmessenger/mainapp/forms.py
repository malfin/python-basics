from django.forms import ModelForm, HiddenInput

from mainapp.models import Message


class DialogMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('sender', 'text')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control form-control-lg mt-2'
            field.widget.attrs['style'] = f'resize: none'
            if field_name == 'sender':
                field.widget = HiddenInput()

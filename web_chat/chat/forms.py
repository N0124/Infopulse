from django.forms import ModelForm, PasswordInput

from chat.models import ChatUser


class RegistrationForm(ModelForm):
    class Meta:
        model = ChatUser
        fields = ['name','login','password']
        widgets = {'password': PasswordInput(),
                   }
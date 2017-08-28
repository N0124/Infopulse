from .models import ChatUser


class ChatUserService:
    @staticmethod
    def save_user(reg_form):
        if reg_form.is_valid():
            user_name=reg_form.cleaned_data['name']
            user_login = reg_form.cleaned_data['login']
            user_password = reg_form.cleaned_data['password']
            chat_user=ChatUser(name=user_name,login=user_login,password=user_password, role_id=1)
            try:
                chat_user.save()
                return True
            except ValueError:
                return False
        else:
            return False

class Auth:
    @staticmethod
    def verify_login(user_login,user_password):
        user = ChatUser.objects.filter(login=user_login).first()
        if user is not None:
            if user.password==user_password:
                return user
            return None
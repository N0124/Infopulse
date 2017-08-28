from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.views.generic import FormView

from chat.forms import RegistrationForm
from chat.models import Ban
from .service import ChatUserService, Auth


class IndexController(View):
    def get(self,request):
        return render(request,'index.html',{'login': reverse('login'),
                                            'registration': reverse('registration')})

class LoginController(View):
    def get(self,request):
        err=request.session.get('error')
        if err is not None:
            del request.session['error']
        else:
            err=''

        return render(request,'login.html',{'error':err})
    def post(self, request):
        user_login=request.POST['login']
        user_password = request.POST['password']
        user= Auth.verify_login(user_login, user_password)
        if user is not None:
            request.session['login'] = user_login
            if user.role.role_name=='USER':
                ban=Ban.objects.filter(user_id=user.id).first()

                request.session['role'] = 'USER'
                if ban is not None:

                    request.session['is_ban']=True
                    return redirect(reverse('ban'))
                else:
                    request.session['is_ban'] = False
                    return redirect(reverse('chat'))
            else:
                return redirect(reverse('admin'))
        else:
            request.session['error']='Login is incorrect.Try again.'
            return redirect(reverse('login'))



class RegistrationController(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    '''def get(self,request):
        return render(request,'registration.html',{'form':RegistrationForm})'''
    def post(self, request):
        reg_form=RegistrationForm(request.POST)
        if ChatUserService.save_user(reg_form):
            root_url = reverse('index')
            return redirect(root_url)
        else:
            return render(request,'registration.html',{'form': reg_form})

class ChatController(View):
    def get(self, request):
        return render(request,'chat/chat.html',{})

class AdminController(View):
    def get(self, request):
        pass

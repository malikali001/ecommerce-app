from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from store.forms.user_creation_form import SignUpForm
from store.forms.user_updation_form import UserUpdate
from store.models.newuser import NewUser
from django.views import View
import random

# Create your views here.


class UserView(View):
    def get(self, request):
        user_form = SignUpForm()
        return render(request, 'store/signup.html', {'form': user_form})

    def post(self, request):
        user_form = SignUpForm(request.POST, request.FILES)
        if user_form.is_valid():
            token = random.randrange(1000,9999)
            email = user_form.cleaned_data.get('email')
            user = user_form.save(commit=False)
            user.token = token
            user.save()
            send_mail('Confirmation Mail', f'http://127.0.0.1:8000/store/email-validate/?token={token}', 'pt.alihussain@gmail.com', [email,])
            return HttpResponse('user created')
        return HttpResponse(user_form.errors)






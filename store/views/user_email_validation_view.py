from django.http import HttpResponse
from django.shortcuts import render
from store.models.newuser import NewUser
from django.views import View


class EmailConfirmation(View):
    def get(self, request):
        token = request.GET.get('token')
        user = NewUser.objects.get(token=token)
        if user:
            user.confirmed = True
            user.save()
            return HttpResponse('validated')
        return HttpResponse('You are not validated')

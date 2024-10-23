from django.http import HttpResponse
from django.shortcuts import render
from store.forms.user_updation_form import UserUpdate
from django.views import View


class UserUpdateView(View):
    def get(self, request):
        user_form = UserUpdate()
        return render(request, 'store/update.html', {'form': user_form})

    def post(self, request):
        user_form = UserUpdate(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse('user Updated')
        return HttpResponse(user_form.errors)
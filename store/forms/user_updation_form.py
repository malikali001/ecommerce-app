from django.contrib.auth.forms import UserChangeForm
from store.models.newuser import NewUser


class UserUpdate(UserChangeForm):
    class Meta:
        model = NewUser
        fields = ['username', 'first_name', 'last_name', 'email', 'image']
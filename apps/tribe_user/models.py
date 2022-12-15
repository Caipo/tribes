from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm 

class CustomUser(AbstractUser, PermissionsMixin):
    tribe  = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username']

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__( *args, **kargs)
        del self.fields['username']

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')
        

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            get_user_model().objects.get(username=username)
        except get_user_model().DoesNotExist:
            return username
        raise forms.ValidationError(self.error_message['duplicate_username'])

from users.models import UserProfile
from django import forms


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

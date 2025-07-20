from django import forms
from django.utils.translation import gettext_lazy as _
from schoolGrade.models import *


class ImageUpload(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['desc', 'image']


class ClassmateAdd(forms.ModelForm):
    # profile_image = forms.ModelChoiceField(
    #     queryset=Images.objects.all()
    # )

    class Meta:
        model = Classmates
        fields = ['first_name', 'last_name', 'description', 'profile_image']

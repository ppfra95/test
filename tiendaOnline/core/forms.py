from core.models import FContacto
from django_mongoengine import forms


class Contacto(forms.DocumentForm):
    class Meta:
        document=FContacto
        fields = ['subject','email','message']

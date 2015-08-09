from django.forms import ModelForm
from phones.models import Person

class PersonForm(ModelForm):
    class Meta:
    model = Person
    fields = ['last_name', 'first_name', 'middle_name', 'unit', 'position',]



import django_filters

from .models import City
from django.forms import ModelForm, TextInput, Form


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'form-control',
                                            'name': 'city',
                                            'id': 'search-input',
                                            'placeholder': 'Введите город ...',
                                            'autocomplete': "off"
                                            })}

    # def __init__(self, *args, **kwargs):
    #     lang = kwargs.pop("language")
    #
    #     super(CityForm, self).__init__(*args, **kwargs)
    #     if lang == 'ru':
    #         self.fields['name'].placeholder = 'Введите город ...'
    #     else:
    #         self.fields['name'].placeholder = 'Enter a city ...'

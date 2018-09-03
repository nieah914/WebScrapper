from django.forms import ModelForm
from community.models import *

class Form(ModelForm):
    class Meta:
        model = Scrapper
        fields = ['required_keywords','optional_keywords','except_keywords']

class PostForm(Form):
    required_keywords = models.CharField(max_length=100, null = True)
    optional_keywords = models.CharField(max_length=100, null = True)
    except_keywords = models.CharField(max_length=1000, null = True)

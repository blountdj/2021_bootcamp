from django.forms import ModelForm
from .models import Project


# here we are using ModelForms
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__' # select all fields from model
        exclude = ['vote_total', 'vote_ratio'] # exclude certain fields



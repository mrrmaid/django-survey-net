from django import forms
from django.forms import CheckboxSelectMultiple

from basic_app.models import Survey, Tag

#class RegForm(forms.Form):
#    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

#class LogForm(forms.Form):
 #   username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
 #   password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ('title', 'tags')
        TAGS_CHOICES = Tag.objects.all()
        widgets = {
            'title': forms.TextInput(attrs={'class': 'create-title'})#forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
        }

        def __init__(self, *args, **kwargs):
            super(SurveyForm, self).__init__(*args, **kwargs)

            self.fields["tags"].widget = CheckboxSelectMultiple(attrs={'class': 'create-title'})
            self.fields["tags"].queryset = Tag.objects.all()


from django import forms
from jobs.models import Applicant,Comment
class JobForm(forms.Form):
  firstname = forms.CharField(max_length=200,
        widget = forms.TextInput(
         attrs = {
            'type':'text',
            'id':'firstname'
         }
        )
  )
  lastname = forms.CharField(max_length=200,
      widget = forms.TextInput(
       attrs = {
         'type':'text',
          'id':'lastname'
       }
      )
    )
  job = forms.CharField(max_length=200,
        widget = forms.TextInput(
          attrs = {
            'type':'text',
            'id':'job'
         }
        )
  )
  email = forms.CharField(max_length=200,
        widget = forms.TextInput(
         attrs = {
           'type':'email',
           'id':'email'
         }
        )
  )
class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ("name","email","body")
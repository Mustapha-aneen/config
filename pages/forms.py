
from django import forms
from pages.models import Users
class LoginForms(forms.Form):
    email = forms.CharField(
      widget = forms.TextInput(
        attrs = {
          "type":"email",
          "onchange":"valid(this)"
          
        }
        )
    )
    password = forms.CharField(
        widget = forms.TextInput(
          attrs = {"type":"password"}
          )
      )
        
class CreateForms(forms.Form):
  username = forms.CharField(
      label = "username",
      widget = forms.TextInput(
          attrs = {
            "type":"text"
            
          }
        )
    )
  email = forms.CharField(
      label = "email",
      widget = forms.TextInput(
          attrs = {
            "type":"email"
            
          }
        )
    )
  password = forms.CharField(
      label = "password",
      widget = forms.TextInput(
          attrs = {
            "type":"password",
            'class':"password1",
            'onchange':'confirm(this)',
            'onfocus':'confirm(this)',
          }
        )
    )
  confirm_password = forms.CharField(
      label = "confirm_password",
      widget = forms.TextInput(
          attrs = {
            "type":"password",
            "class":"password2",
            'onchange':'confirm(this);',
            'onclose':'confirm(this);',
            
          }
        )
    )
  
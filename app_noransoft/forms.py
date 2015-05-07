from django import forms
from .models import *

class AddForm(forms.ModelForm):

	class Meta:
		model = Blog
		fields = ('title', 'body', 'category')
		widgets = {
			'title': forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Title"}),
			'body': forms.Textarea(attrs={"class":"form-control", "rows":"6", "placeholder":"Enter Content"}),
			'category': forms.Select(attrs={"class":"form-control"}),
		}
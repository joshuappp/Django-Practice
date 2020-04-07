from django import forms
from blogs.models import Article

class ModelForm(forms.ModelForm):

	class Meta:

		model = Article

		fields = [
           'title',
           'content',
           'active',
		]



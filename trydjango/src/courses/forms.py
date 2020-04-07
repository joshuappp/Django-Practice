from django import forms
from .models import Course

class CouurseModelForm(forms.ModelForm):

	class Meta:
		model = Course
		fields = [
             'title'
		]

	def clean_title(self):

		title = self.cleaned_data.get('title')

		if title.lower() == 'abc':

			raise forms.ValidationError('This is not valid title')
		return title 


from django import forms

class ContactForm(forms.Form):

	full_name = forms.CharField()
	email     = forms.EmailField()
	contact   = forms.CharField(widget=forms.Textarea) 

	def clean_email(self, *args, **kwargs):

		email = self.cleaned_data.get('email')

		if email.endswith('.edu'):
			raise forms.ValidationError('This is not valid email, Please dont use .edu ')
		return email
from django import forms
from .models import Cart

class CartModelForm(forms.ModelForm):

	class Meta:

		model = Cart
		fields = [
		    'title',
		    'content',
		    'active',
		]
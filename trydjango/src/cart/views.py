from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
	CreateView,
	ListView,
	DetailView,
	UpdateView,
	DeleteView
	)
from .models import Cart
from .forms import CartModelForm

# Create your views here.

class CartsCreateView(CreateView):
	template_name = 'carts/cart_create.html'
	form_class = CartModelForm
	queryset = Cart.objects.all() 
	#success_url = '/'

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)

	#def get_success_url(self):
		#return success_url



class CartsListView(ListView):
	template_name = 'carts/cart_list.html'
	queryset = Cart.objects.all() 

class CartsDetailView(DetailView):
	template_name = 'carts/cart_detail.html'
	#queryset = Carts.objects.all() 

	def get_object(self): 

		id_ = self.kwargs.get('id')

		return get_object_or_404(Cart,id=id_) 

class CartsUpdateView(UpdateView):
	template_name = 'carts/cart_create.html'
	form_class = CartModelForm
	queryset = Cart.objects.all() 

	def get_object(self): 

		id_ = self.kwargs.get('id')

		return get_object_or_404(Cart,id=id_)

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)

class CartsDeleteView(DeleteView):
	template_name = 'carts/cart_delete.html'
	#queryset = Carts.objects.all() 
	#success_url = '/' 

	def get_object(self): 

		id_ = self.kwargs.get('id')

		return get_object_or_404(Cart,id=id_)

	def get_success_url(self):   
		return reverse("carts:cart-list")

	 















from django.urls import path
from .views import (
	CartsListView,
	CartsDetailView,
	CartsCreateView,
	CartsUpdateView,
	CartsDeleteView
	)

app_name = 'carts'
urlpatterns = [
     path('',CartsListView.as_view(),name = 'cart-list'),
     path('<int:id>/',CartsDetailView.as_view(),name = 'cart-detail'),
     path('create/',CartsCreateView.as_view(),name = 'cart-create'),
     path('<int:id>/update/',CartsUpdateView.as_view(),name = 'cart-update'),
     path('<int:id>/delete/',CartsDeleteView.as_view(),name = 'cart-delete'),
]
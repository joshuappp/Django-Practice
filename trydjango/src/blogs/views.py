from django.shortcuts import get_object_or_404,render,redirect
from blogs.models import Article
from blogs.forms import ModelForm

# Create your views here.

def article_delete_view(request,my_id):

	obj = get_object_or_404(Article,id=my_id)

	obj.delete()
	return redirect('/blogs/list') 

def article_update_view(request,my_id):

	obj = get_object_or_404(Article,id=my_id)

	form = ModelForm(request.POST or None,instance=obj)

	if form.is_valid():
		form.save()
		form = ModelForm()

	context = {
	  'form': form
	}

	return render(request, 'blogs/article_create.html',context)

def article_detail_view(request,my_id):

	obj = get_object_or_404(Article,id=my_id)

	context = {
	  'object': obj
	}

	return render(request, 'blogs/article_details.html',context)

def article_list_view(request):

	queryset = Article.objects.all()

	context = {
	  'article_list': queryset
	}

	return render(request, 'blogs/article_list.html',context)

def article_create_view(request):

	form = ModelForm(request.POST or None)

	if form.is_valid():
		form.save()
		form = ModelForm()

	context = {
	  'form': form
	}

	return render(request, 'blogs/article_create.html',context)



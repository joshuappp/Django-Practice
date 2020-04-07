from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from .models import Course
from .forms import  CouurseModelForm

# Create your views here.

#BASE VIEW Class=View

# def CourseObjectMixin(object):
# 	model = Course
# 	lookup = 'id'

# 	def get_object(self):
# 		id = self.kwargs.get(self.lookup)
# 		obj = None
# 		context = {}
# 		if id is not None:
# 			obj = get_object_or_404(self.model,id=id)
# 		return obj

# class CourseDeleteView(CourseObjectMixin,View):
# 	template_name = 'courses/course_delete.html'

# 	def get(self,request,id=None,*args,**kwargs):
# 		#GET METHOD
# 		context = {} 
# 		obj = self.get_object()

# 		if obj is not None:		
# 			context['object'] = obj
# 		return render(request,self.template_name,context)

# 	def post(self,request,id=None,*args,**kwargs):
# 		#POST METHOD
# 		context = {} 
# 		obj = self.get_object()

# 		if obj is not None:
# 			obj.delete()
# 			context['object'] = obj
# 			return redirect('/courses/') 
# 		return render(request,self.template_name,context)





class CourseDeleteView(View):
	template_name = 'courses/course_delete.html'
	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		context = {}
		if id is not None:
			obj = get_object_or_404(Course,id=id)
		return obj  

	def get(self,request,id=None,*args,**kwargs):
		#GET METHOD
		context = {} 
		obj = self.get_object()

		if obj is not None:		
			context['object'] = obj
		return render(request,self.template_name,context)

	def post(self,request,id=None,*args,**kwargs):
		#POST METHOD
		context = {} 
		obj = self.get_object()

		if obj is not None:
			obj.delete()
			context['object'] = obj
			return redirect('/courses/') 
		return render(request,self.template_name,context) 

class CourseUpdateView(View):
	template_name = 'courses/course_update.html'
	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		context = {}
		if id is not None:
			obj = get_object_or_404(Course,id=id)
		return obj  

	def get(self,request,id=None,*args,**kwargs):
		#GET METHOD
		context = {} 
		obj = self.get_object()

		if obj is not None:
			form = CouurseModelForm(instance=obj)

			if form.is_valid():
				form.save()
			context['object'] = obj
			context['form'] = form
		return render(request,self.template_name,context)

	def post(self,request,id=None,*args,**kwargs):
		#POST METHOD
		context = {} 
		obj = self.get_object()

		if obj is not None:
			form = CouurseModelForm(request.POST,instance=obj)
			if form.is_valid():
				form.save()
			context['object'] = obj
			context['form'] = form
		return render(request,self.template_name,context) 




class CourseCreateView(View):
	template_name = 'courses/course_create.html'
	def get(self,request,*args,**kwargs):
		#GET METHOD
		form = CouurseModelForm()
		context = {
		    'form':form
		} 
		return render(request,self.template_name,context)

	def post(self,request,*args,**kwargs):
		#POST METHOD
		form = CouurseModelForm(request.POST)

		if form.is_valid():
			form.save()
			form = CouurseModelForm()
		context = {
		    'form':form
		}
		return render(request,self.template_name,context)

class CourseListView(View):
	template_name = 'courses/course_list.html'
	queryset = Course.objects.all()

	def get_queryset(self):
		return self.queryset

	def get(self,request,*args,**kwargs):
		context = {
		      'object_list':self.get_queryset()
		}
		return render(request,self.template_name,context)



class CourseView(View):
	template_name = 'courses/course_detail.html'
	def get(self,request, id=None,*args,**kwargs):
		context = {}
		 
		return render(request,self.template_name,context)


#HTTP METHODS
def my_fbv(request, *args,**kwargs):
	print(request.method)
	return render(request,'about.html',{})

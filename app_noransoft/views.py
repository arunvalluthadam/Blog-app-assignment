from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
	blogs = Blog.objects.all()
	variables = RequestContext(request, {
		'blogs': blogs,
	})
	return render_to_response("index.html", variables)

def one_page(request, blog_id=1):
	blog = Blog.objects.get(id=blog_id)
	variables = RequestContext(request, {
		'single_blog': blog,
	})
	return render_to_response("one_page.html", variables)

@csrf_exempt
def add(request):
	form = AddForm()
	if request.POST:
		form = AddForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
		else:
			print form.errors
	variables = RequestContext(request, {
		'form':form,
	})
	return render_to_response("add.html", variables)

def category(request):
	categorys = Category.objects.all()
	variables = RequestContext(request, {
		'categorys':categorys,
	})
	return render_to_response("category.html", variables)

def category_index(request, cat_name):
	blogs = Blog.objects.filter(category__category=cat_name)
	variables = RequestContext(request, {
		'blogs':blogs,
	})
	return render_to_response("category_index.html", variables)
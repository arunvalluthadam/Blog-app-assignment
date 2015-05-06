from django.shortcuts import render_to_response

# Create your views here.
def home(request):
	return render_to_response("index.html")

def one_page(request):
	return render_to_response("one_page.html")

def add(request):
	return render_to_response("add.html")

def category(request):
	return render_to_response("category.html")
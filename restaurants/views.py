from django.shortcuts import render

# Create your views here.
def hello_world(request):
	context = {"msg" : "Hello World!"}
	return render(request, "restaurant.html", context)
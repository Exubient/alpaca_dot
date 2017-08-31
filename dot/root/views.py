from django.shortcuts import render

# Create your views here.
def root(request):
	if request.method =="GET":
		return render(request, 'root/src/index.html', {})
	elif request.method == "POST":
		startAdmin()
		return render(request, 'response_time/src/etc/root.html', {})


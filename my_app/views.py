from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request=request, template_name="my_app/index.html")
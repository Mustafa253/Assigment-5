from django.shortcuts import render
from .models import PythonType, Product, Review

# Create your views here.
def index (request):
    return render(request, 'pythonclubapp/index.html')

def getTypes(request):
    types_list=PythonType.objects.all()
    context={'types_list' : types_list}
    return render(request, 'pythonclubapp/types.html', context=context)



    

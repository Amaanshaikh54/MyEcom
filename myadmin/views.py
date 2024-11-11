from django.shortcuts import render

# # Create your views here.
def index(request):
    return render(request,'myadmin/common/index.html')


def dashboard(request):
    return render(request,'myadmin/dashboard.html')
def add_category(request):
    return render(request,'myadmin/add_category.html')
def all_category(request):
    return render(request,'myadmin/all_category.html')
def add_product(request):
    return render(request,'myadmin/add_product.html')
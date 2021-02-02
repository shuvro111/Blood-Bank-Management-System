from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def create__account(request):
    return render(request, 'main/create__account.html') 
 
def log__in(request):
    return render(request, 'main/log__in.html') 


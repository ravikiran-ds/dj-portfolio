from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from my_portfolio.forms import InfoForm
from my_portfolio.models import Msg
from django.views.generic import ListView

# Create your views here.
def index(request):
    return render(request,"my_portfolio/index.html")

def projects(request):
    return render(request,"my_portfolio/projects.html")

def info(request):
        form=InfoForm()
        if request.method=='POST':
            form=InfoForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return index(request)
            else:
                return HttpResponse("Failed!")
        return render(request,"my_portfolio/info.html",context={"form":form})

class messages(ListView):
    model=Msg
    context_object_name="data"

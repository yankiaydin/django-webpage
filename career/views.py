from django.shortcuts import render, redirect
from .forms import CareerForm
from django.contrib.auth.decorators import login_required
from .models import Career

# Create your views here.

def career_page(request):
    adverts = Career.objects.all()
    return render(request, "career.html",{"adverts":adverts})

@login_required(login_url='/member/login/')
def career_advert(request):
    if request.method == "POST":
        form = CareerForm(request.POST)
        if form.is_valid():
            advert = request.user.career_set.create(advert_title = request.POST.get("advert_title"))
            advert.firm = request.POST.get("firm")
            advert.content = request.POST.get("content")
            advert.save()
            return redirect("home")

    form = CareerForm()
    return render(request,"career_form.html",{"form":form})

def advert_detail(request, id):
    advert = Career.objects.get(id = id)
    return render(request, "career_detail.html",{"advert":advert})


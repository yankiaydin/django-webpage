from django.shortcuts import render, redirect
from career.models import Career
from article.models import Article


# Create your views here.

def main_page(request):
    article1 = Article.objects.get(id=19)
    article2 = Article.objects.get(id=20)
    article3 = Article.objects.get(id=21)
    career1 = Career.objects.get(id=15)
    career2 = Career.objects.get(id=16)
    career3 = Career.objects.get(id=17)
    context= {
        "article1":article1,
        "article2":article2,
        "article3":article3,
        "career1":career1,
        "career2":career2,
        "career3":career3
    }
    return render(request,"home.html",context)

def results_page(request):
    if request.method == "POST":
        keyword= request.POST.get("search-input")
        articles = Article.objects.filter(title__startswith=keyword)
        adverts = Career.objects.filter(advert_title=keyword)
        context = {
            "articles":articles,
            "adverts":adverts
        }
        return render(request,"search.html", context)
    return redirect("home")

def about(request):
    return render(request,"about.html")


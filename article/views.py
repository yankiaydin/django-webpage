from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    reverse,
    HttpResponseRedirect,
)
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/member/login/")
def dashboard_page(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, "dashboard.html", {"articles": articles})


def articles_page(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "articles.html", context)


@login_required(login_url="/member/login/")
def edit_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article.objects.create(author=request.user)
            article.title = form.cleaned_data.get("title")
            article.content = form.cleaned_data.get("content")
            article.save()
            return redirect("articles:articles_page")
    form = ArticleForm()
    return render(request, "edit_article.html", {"form": form})


def article_detail(request, id):
    if request.method == "POST":
        article = Article.objects.get(id=id)
        article.comment_set.create(
            commenter=request.user, comment_content=request.POST.get("content")
        )
        return HttpResponseRedirect(reverse("articles:article_detail", args=[id]))

    form = CommentForm()
    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(comment_to=article)
    context = {"article": article, "form": form, "comments": comments}
    return render(request, "article.html", context)


@login_required(login_url="/member/login/")
def delete_article(request, id=id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect("articles:articles_page")


@login_required(login_url="/member/login/")
def update_article(request, id):
    if request.method == "POST":
        article = get_object_or_404(Article, id=id)
        form = ArticleForm(request.POST or None, instance=article)
        if form.is_valid():
            revision = form.save(commit=False)
            revision.content = form.cleaned_data.get("content")
            revision.save()
            return redirect("articles:articles_page")
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, instance=article)
    return render(request, "update_article.html", {"form": form})

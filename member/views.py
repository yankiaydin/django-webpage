from django.shortcuts import (
    render,
    redirect,
    HttpResponseRedirect,
    reverse,
    get_object_or_404,
)
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from .forms import UserForm, myForm, ProfileForm, ArchForm, EduForm, ConstForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Architect, Constructor, Education

# Create your views here.


def login_user(request):
    if request.method == "POST":
        form = myForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Username and Password did not match")
                form = myForm()
                return render(request, "login.html", {"form": form})
    form = myForm()
    return render(request, "login.html", {"form": form})


def register_user(request):
    if request.method == "POST":
        u_form = UserForm(request.POST)
        if u_form.is_valid():
            name = u_form.cleaned_data.get("username")
            password = u_form.cleaned_data.get("password")
            mail = u_form.cleaned_data.get("email")
            user = User.objects.create(username=name, email=mail)
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect("home")
    else:
        u_form = UserForm()
        return render(request, "register.html", {"u_form": u_form})


def logout_user(request):
    logout(request)
    messages.success(request, "Succesfully logged out")
    return redirect("home")


def user_profile(request, user):
    member = get_object_or_404(User, username=user)
    context = {"user": user, "member": member}
    return render(request, "profile.html", context)


@login_required(login_url="/member/login/")
def edit_profile(request, user):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            u1 = User.objects.get(username=request.user)
            persona = Profile(
                user=u1,
                location=form.cleaned_data.get("location"),
                web_page=form.cleaned_data.get("web_page"),
                job=form.cleaned_data.get("job"),
                bio=form.cleaned_data.get("bio"),
                profile_pic=form.cleaned_data.get("profile_pic"),
            )
            persona.save()
            if persona.job == "Architect":
                return HttpResponseRedirect(
                    reverse("member:architect_profile", args=[user])
                )
            elif persona.job == "Constructor":
                return HttpResponseRedirect(
                    reverse("member:const_profile", args=[user])
                )
            elif persona.job == "Lecturer/Student":
                return HttpResponseRedirect(reverse("member:edu_profile", args=[user]))
            else:
                return HttpResponseRedirect(reverse("member:user_profile", args=[user]))
    persona = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=persona)
    return render(request, "edit_profile.html", {"user": user, "form": form})


@login_required(login_url="/member/login/")
def architect_profile(request, user):
    if request.method == "POST":
        form = ArchForm(request.POST, instance=request.user)
        if form.is_valid():
            arch = Architect(user=request.user)
            arch.office = form.cleaned_data.get("office")
            arch.experience = form.cleaned_data.get("experience")
            arch.save()
            return HttpResponseRedirect(reverse("member:user_profile", args=[user]))
    form = ArchForm()
    return render(request, "edit_profile_02.html", {"form": form})


@login_required(login_url="/member/login/")
def const_profile(request, user):
    if request.method == "POST":
        form = ConstForm(request.POST, instance=request.user)
        if form.is_valid():
            const = Constructor(user=request.user)
            const.company_name = form.cleaned_data.get("company_name")
            const.service = form.cleaned_data.get("service")
            const.save()
            return HttpResponseRedirect(reverse("member:user_profile", args=[user]))
    form = ConstForm()
    return render(request, "edit_profile_02.html", {"form": form})


@login_required(login_url="/member/login/")
def edu_profile(request, user):
    if request.method == "POST":
        form = EduForm(request.POST, instance=request.user)
        if form.is_valid():
            edu = Education(user=request.user)
            edu.university = form.cleaned_data.get("university")
            edu.role = form.cleaned_data.get("role")
            edu.save()
            return HttpResponseRedirect(reverse("member:user_profile", args=[user]))
    form = EduForm()
    return render(request, "edit_profile_02.html", {"form": form})

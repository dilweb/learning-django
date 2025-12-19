from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LogoutView 

def login_view(rerquest: HttpRequest) -> HttpResponse:
    if rerquest.method == "GET":
        if rerquest.user.is_authenticated:
            return redirect("/admin/")
        
        return render(rerquest, "myauth/login.html")
    
    username = rerquest.POST["username"]
    password = rerquest.POST["password"]
    user = authenticate(rerquest, username=username, password=password)

    if user is not None:
        login(rerquest, user)
        return redirect("/admin/")
    
    return render(rerquest, "myauth/login.html", {"error": "Invalid username or password"})


def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("fizz", "buzz", max_age=3600)
    return response


def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fizz", "Cookie not found")
    return HttpResponse(f"Value of 'fizz' cookie: {value!r}")


def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["foobar"] = "spameggs"
    return HttpResponse("Session set!")


def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "Session not found")
    return HttpResponse(f"Value of 'foobar' session: {value!r}")


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect(reverse("myauth:login"))


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")

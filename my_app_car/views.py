from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from django.conf import settings
from .models import Car, Person, Rent
from django.urls import reverse
from django.shortcuts import redirect
import logging
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from .forms import CarForm, PersonForm, RentForm, LoginForm, UserForm
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.core.validators import RegexValidator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def logout_user(req):
    if req.user.is_authenticated:
        logout(request=req)

    return redirect("home")


def create_user(req):
    if req.method == "GET":
        return render(request=req, template_name="my_app/signup.html",
                      context={'userform': UserForm(),
                               "person_form": PersonForm()})

    elif req.method == 'POST':
        userform = UserForm(data=req.POST)
        person_form = PersonForm(data=req.POST)
        if userform.is_valid() and person_form.is_valid():
            user = userform.save()
            person_form.instance.user = user
            person_form.save()
            login(request=req, user=user)
            return redirect("home")
        else:
            return render(request=req, template_name="my_app/signup.html",
                          context={'form': userform})


def connect(req):
    if req.method == 'GET':
        return render(request=req, template_name="my_app/login.html",
                      context={'form': LoginForm(),
                               'action': 'login'})

    elif req.method == 'POST':
        un = req.POST.get("username")
        pw = req.POST.get("password")

        user = authenticate(req, username=un, password=pw)
        if user is None:
            return HttpResponse("wrong user info")
        else:
            login(request=req, user=user)
            return redirect("home")


def home(req):
    return render(request=req, template_name="my_app/home.html")


@login_required
def add_car(req):
    if req.method == 'GET':
        return render(request=req, template_name="my_app/add_car.html",
                      context={"form": CarForm()})
    elif req.method == 'POST':
        form = CarForm(data=req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "car added successfully")
            return HttpResponseRedirect("http://127.0.0.1:8000/")
        else:
            return render(request=req, template_name="my_app/add_car.html",
                          context={"form": CarForm()})


@login_required
def add_person(req):
    if req.method == 'GET':
        return render(request=req, template_name="my_app/add_person.html",
                      context={"form": PersonForm()})
    elif req.method == 'POST':
        form = PersonForm(data=req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("http://127.0.0.1:8000/")
        else:
            return render(request=req, template_name="my_app/add_person.html",
                          context={"form": PersonForm()})


def home1(req):
    req.session['session_key'] = "session_value"
    ses = req.session.get("session_key", "no ses found")
    return HttpResponse(f"hello home - {ses}")


@login_required
def add_rent(req):
    if req.method == 'GET':
        return render(request=req, template_name="my_app/add_rent.html",
                      context={"form": RentForm()})
    elif req.method == 'POST':
        form = RentForm(data=req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("http://127.0.0.1:8000/")
        else:
            return render(request=req, template_name="my_app/add_rent.html",
                          context={"form": RentForm()})


@login_required
def edit_car(req, cid):
    car = Car.objects.get(pk=cid)
    if req.method == "GET":
        form = CarForm(instance=car)
        return render(request=req, template_name="my_app/edit_car.html",
                      context={'form': form, 'cid': cid})
    elif req.method == 'POST':
        form = CarForm(req.POST, instance=car)
        if form.is_valid():
            try:
                form.save()
                messages.success(req, f"car added successfully, car name => {car.car_type}")
            except Exception as e:
                print(e)
        return render(request=req, template_name="my_app/edit_car.html",
                      context={'form': form, 'cid': cid})


def show_car(req):
    car = req.POST['q']
    message = Car.objects.filter(car_type__contains=car)
    return render(request=req, template_name="my_app/home.html", context={'car': message})


@login_required
def show_renters(req):
    renters = req.POST['q']
    r = Car.objects.filter(renters=renters)
    return render(request=req, template_name="my_app/s.html", context={'renters': r})


def show_person(req):
    person = req.POST['l']
    message = User.objects.filter(username__contains=person)
    return render(request=req, template_name="my_app/home.html", context={'person': message})


@require_http_methods(['GET'])
def serve_cars(req):
    cars = Car.objects.all()

    return render(request=req, template_name="my_app/cars_list.html",
                  context={'cars': cars})


@require_http_methods(['GET'])
def serve_persons(req):
    persons = Person.objects.all()

    return render(request=req, template_name="my_app/person_list.html",
                  context={'persons': persons})


@require_http_methods(['GET'])
def serve_rents(req):
    rents = Rent.objects.all()

    return render(request=req, template_name="my_app/rent_list.html",
                  context={'rents': rents})


class CarsListView(ListView):
    model = Car
    template_name = "my_app/car_list.html"
    # context_object_name = "my_car_list"
    queryset = Car.objects.filter(car_type__contains="o")


class PersonCreationForm(CreateView):
    model = Person
    template_name = "my_app/person_creation.html"
    fields = "__all__"
    success_url = "http://127.0.0.1:8000/"


class PersonUpdateForm(UpdateView):
    model = Person
    template_name = "my_app/update_person.html"
    fields = ["id", "address", "age"]
    success_url = "http://127.0.0.1:8000/"


class RentUpdateForm(UpdateView):
    model = Rent
    template_name = "my_app/update_rent.html"
    fields = "__all__"
    success_url = "http://127.0.0.1:8000/"


class RentCreationForm(CreateView):
    model = Rent
    template_name = "my_app/add_rent.html"
    fields = "__all__"
    success_url = "http://127.0.0.1:8000/"


class RentDeleteForm(DeleteView):
    model = Rent
    template_name = "my_app/delete_rent.html"
    fields = "__all__"

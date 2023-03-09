from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path("", views.home, name="home"),
   path("login", LoginView.as_view(), name="login"),
   path("logout", LogoutView.as_view(), name="logout"),
   path("signup", views.create_user, name="signup"),
   path("add_car", views.add_car, name="add_car"),
   path("add_person", views.add_person, name="add_person"),
   path("add_rent", views.RentCreationForm.as_view(), name="add_rent"),
   path("edit_car/<str:cid>", views.edit_car, name="edit_car"),
   path("search", views.show_car),
   path('cars_list', views.serve_cars, name='cars_list'),
   path('car_list', views.CarsListView.as_view()),
   path('person_creation', views.PersonCreationForm.as_view(), name='person_creation'),
   path("update_person/<int:pk>", views.PersonUpdateForm.as_view(), name='update_person'),
   path("person_list", views.serve_persons, name="person_list"),
   path("update_rent/<int:pk>", views.RentUpdateForm.as_view(), name="update_rent"),
   path("rent_list", views.serve_rents, name="rent_list"),
   path("sea", views.show_person),
   path("delete_rent", views.RentDeleteForm.as_view(), name="delete_rent")

]
#

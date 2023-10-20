from django.urls import path
from . import views


urlpatterns = [
    path('',views.google,name='google'),
    path('market',views.Homenew,name='index'),
    path('computers',views.computers,name='computers'),
    path('Router',views.Router,name='Router'),



]
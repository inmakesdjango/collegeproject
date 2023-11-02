from . import views
from django.urls import path
app_name='colegehome'

urlpatterns = [
path('',views.home,name='home'),

]
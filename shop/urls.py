from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('<slug:ct_slug>/',views.home,name='pro_ct'),
    path('search',views.search,name='search'),

]
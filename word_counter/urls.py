
from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage, name='home'),
    path('count/',views.countpage, name='count_name'),
    path('about/',views.aboutpage, name='aboutme')
]

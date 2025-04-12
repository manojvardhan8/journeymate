from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'),
    path('login/',views.login,name='login'),
    path('selection/',views.selection_view,name='selection'),
    # path('success/',views.success)
]

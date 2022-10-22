"""vsr_dnipro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'total_ugi'

urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('telephone_numbers/', views.telephone_directory, name='telephone_directory'),
    path('app_guide/', views.app_guide, name='app_guide'),
    # path('view_orders/', views.view_orders, name='view_orders'),
    # path('orders_in_work/', views.orders_in_work, name='orders_in_work'),
    # path('finished_orders/', views.finished_orders, name='finished_orders')
]

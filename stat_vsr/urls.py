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

app_name = 'stat_vsr'

urlpatterns = [
    path('all_materials_vsr/', views.all_materials_vsr, name='all_materials_vsr'),
    path('investigations_vsr/', views.investigations_vsr, name='investigations_vsr'),
    path('policemen_vsr/', views.policemen_vsr, name='policemen_vsr'),
    path('id_vsr/', views.id_vsr, name='id_vsr'),
    path('current_work_vsr/', views.current_work_vsr, name='current_work_vsr'),
    path('general_report_vsr/', views.general_report_vsr, name='general_report_vsr'),
    path('investigations_report_vsr/', views.investigations_report_vsr, name='investigations_report_vsr'),
    path('detailed_report_vsr/', views.detailed_report_vsr, name='detailed_report_vsr'),
    path('map_vsr/', views.map_vsr, name='map_vsr'),
]


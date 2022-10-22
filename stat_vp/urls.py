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

app_name = 'stat_vp'

urlpatterns = [
    path('all_materials_vp/', views.all_materials_vp, name='all_materials_vp'),
    path('inspections_results_vp/', views.inspections_results_vp, name='inspections_results_vp'),
    path('policemen_vp/', views.policemen_vp, name='policemen_vp'),
    path('id_vp/', views.id_vp, name='id_vp'),
    path('memorandums_about_inspections_vp/', views.memorandums_about_inspections_vp,
         name='memorandums_about_inspections_vp'),
    path('certificates_about_inspections_vp/', views.certificates_about_inspections_vp,
         name='certificates_about_inspections_vp'),
    path('investigations_vp/', views.investigations_vp, name='investigations_vp'),
    path('general_report_vp/', views.general_report_vp, name='general_report_vp'),
    path('current_work_vp/', views.current_work_vp, name='current_work_vp'),
    path('investigations_report_vp/', views.investigations_report_vp, name='investigations_report_vp'),
    path('detailed_report_vp/', views.detailed_report_vp, name='detailed_report_vp'),
    path('map_vp/', views.map_vp, name='map_vp'),
]

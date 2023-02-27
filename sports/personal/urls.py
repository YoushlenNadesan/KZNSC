from django.urls import path
from . import views

urlpatterns = [
    path('', views.personinfo, name="personinfo"),
    path('education/',views.education, name="educationinfo"),
    path('employment/',views.employment, name="employmentinfo"),
    path('nextofkin/',views.nextofkin, name="nextofkeninfo"),
    path('crud/',views.cruds, name="cruds")
]
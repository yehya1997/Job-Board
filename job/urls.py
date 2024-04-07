
from django.urls import path , include
from . import views

urlpatterns = [
    path('<int:id>',views.job_deatails),
    path('',views.job_list),
]

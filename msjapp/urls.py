from django.urls import path
from msjapp import views

urlpatterns = [
    path('sendmsg',views.sendmsg),
    path('dashboard',views.dashboard),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
    
]
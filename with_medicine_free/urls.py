from django.urls import path
from with_medicine_free import views  

urlpatterns = [
    path('free_read/', views.free_read, name='free_read'),
]
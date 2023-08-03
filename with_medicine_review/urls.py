from django.urls import path
from with_medicine_review import views  

urlpatterns = [
    path('review_read/', views.review_read, name='review_read'),
]
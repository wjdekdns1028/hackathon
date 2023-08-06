"""
URL configuration for with_medicine_prj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

import with_medicine_app.views
import with_medicine_free
import with_medicine_review
#import with_medicine_user



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', with_medicine_app.views.main, name = 'main'),
    
    path('with_medicine_userapp/', include('with_medicine_userapp.urls')),
    #path('signup/', with_medicine_user.views.signup, name='signup'),
    #path('login/', with_medicine_user.views.login, name='login'),
    #path('logout/', with_medicine_user.views.logout, name='logout'),

    path('', include('with_medicine_free.urls')),
    path('free_create/', with_medicine_free.views.free_create, name = 'free_create'),
    path('free_read/', with_medicine_free.views.free_read, name = 'free_read'),
    path('free_detail/<str:id>/', with_medicine_free.views.free_detail, name= 'free_detail'),
    path('free_update/<str:id>/', with_medicine_free.views.free_update, name = 'free_update'),
    path('free_delete/<str:id>/', with_medicine_free.views.free_delete, name='free_delete'),
    path('<int:id>/comments/<int:c_id>/free_comment_delete', with_medicine_free.views.free_comment_delete, name="free_comment_delete"),
    path('free_comment_update/<int:id>/<int:com_id>/', with_medicine_free.views.free_comment_update, name="free_comment_update"),
    
    path('', include('with_medicine_review.urls')),
    path('review_create/', with_medicine_review.views.review_create, name = 'review_create'),
    path('review_read/', with_medicine_review.views.review_read, name = 'review_read'),
    path('review_detail/<str:id>/', with_medicine_review.views.review_detail, name= 'review_detail'),
    path('review_update/<str:id>/', with_medicine_review.views.review_update, name = 'review_update'),
    path('review_delete/<str:id>/', with_medicine_review.views.review_delete, name='review_delete'),
    path('<int:id>/comments/<int:c_id>/review_comment_delete', with_medicine_review.views.review_comment_delete, name="review_comment_delete"),
    path('review_comment_update/<int:id>/<int:com_id>/', with_medicine_review.views.review_comment_update, name="review_comment_update"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

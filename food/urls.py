from django.urls import path
from .views import create_food, update_food, delete_food  , food_detail
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.select_by_category, name='select_by_category'),
    path('create/', create_food, name='create_food'),
    path('update/<int:id>/', update_food, name='update_food'),
    path('delete/<int:id>/', delete_food, name='delete_food'), 
    path('food/<int:food_id>/', food_detail, name='food_detail'),    
    path('comment/<int:comment_id>/update/', views.update_comment, name='update_comment'),
    path('food/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    path('food/<int:pk>/like/', views.like_food, name='like_food'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

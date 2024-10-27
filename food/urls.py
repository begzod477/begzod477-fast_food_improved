from django.urls import path
from .views import (
    create_food,
    update_food,
    delete_food,
    food_detail,
    home,
    select_by_category,
    add_comment,
    like_food,
    logout_view,
    login,
    register
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/', select_by_category, name='select_by_category'),
    path('create/', create_food, name='create_food'),
    path('update/<int:id>/', update_food, name='update_food'),
    path('delete/<int:id>/', delete_food, name='delete_food'),
    path('food/<int:food_id>/', food_detail, name='food_detail'),
    path('food/<int:pk>/add_comment/', add_comment, name='add_comment'),  
    path('food/<int:pk>/like/', like_food, name='like_food'),
    path('logout/', logout_view, name='logout'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

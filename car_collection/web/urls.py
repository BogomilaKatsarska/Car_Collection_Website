from django.urls import path, include

from car_collection.web.views import index, details_car, add_car, edit_car, delete_car, create_profile, delete_profile, \
    edit_profile, details_profile, view_catalogue

urlpatterns = (
    path('', index, name='index'),
    path('car/', include([
        path('<int:pk>/details/', details_car, name='details car'),
        path('create/', add_car, name='add car'),
        path('<int:pk>/edit/', edit_car, name='edit car'),
        path('<int:pk>/delete', delete_car, name='delete car'),
    ])),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('delete/', delete_profile, name='delete profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('details/', details_profile, name='details profile'),
    ])),
    path('catalogue/', view_catalogue, name='view catalogue'),
)
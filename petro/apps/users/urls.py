from django.urls import path
# from rest_framework.routers import DefaultRouter

from apps.users import views


urlpatterns = [
    path('', views.UserListAPIView.as_view())
]


# urlpatterns += router.urls

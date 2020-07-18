from django.urls import path
from . import views


urlpatterns = [
    path('items/', views.ItemViewSet.as_view(), name='items'),
    path('ratings/', views.RatingViewSet.as_view(), name='ratings'),
]
from django.urls import path
from .views import MakerList

urlpatterns = [
    path('list/', MakerList.as_view())
]
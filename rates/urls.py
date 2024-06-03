from django.urls import path
from . import views
urlpatterns = [
      path('', views.logistics, name='logistics_view'),
]

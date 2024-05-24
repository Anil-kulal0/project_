from django.urls import path
from . import views



urlpatterns = [
      path('login/', views.login,name='login'),
      path('upload/', views.upload_file, name='upload_file'),
      path('success/', views.process_file, name='upload_success'),
      path('filter/', views.filter_data, name='filter_data'),
      path('add/', views.add_data, name='add_data'),
      path('data_record/', views.data_record, name='data_record'),
      
]

from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.upload_ewaybill, name='upload_ewaybill'),
    path('upload-multiple', views.upload_multiple_ewaybills, name='upload_multiple_ewaybills'),
    path('date', views.current_date_api, name='current_date'),
    path('ewaybills', views.get_ewaybill_data, name='get_ewaybills'),  # All records
    path('ewaybills/<int:pk>', views.get_ewaybill_data, name='get_ewaybill_by_id'),  # Specific record
]
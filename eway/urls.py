from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.upload_ewaybill, name='upload_ewaybill'),
    path('ewaybills', views.get_ewaybill_data, name='get_ewaybills'),  # All records
    path('ewaybills/<int:pk>', views.get_ewaybill_data, name='get_ewaybill_by_id'),  # Specific record
]
from django.db import models

class EWayBill(models.Model):
    pdf_file = models.FileField(upload_to='eway_bills/')
    extracted_data = models.JSONField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, 
        choices=[
            ('processing', 'Processing'),
            ('completed', 'Completed'),
            ('failed', 'Failed')
        ],
        default='processing'
    )
    
    class Meta:
        db_table = 'eway_bills'
    
    def __str__(self):
        return f"EWayBill {self.id} - {self.uploaded_at}"
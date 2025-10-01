from rest_framework import serializers
from .models import EWayBill
import os

class EWayBillUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = EWayBill
        fields = ['pdf_file']
    
    def validate_pdf_file(self, value):
        # Check file extension
        ext = os.path.splitext(value.name)[1].lower()
        if ext != '.pdf':
            raise serializers.ValidationError("Only PDF files are allowed.")
        
        # Check file size (max 10MB)
        if value.size > 10 * 1024 * 1024:
            raise serializers.ValidationError("File size must be under 10MB.")
        
        return value

class EWayBillDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EWayBill
        fields = ['id', 'pdf_file', 'extracted_data', 'uploaded_at', 'status']
        read_only_fields = ['extracted_data', 'uploaded_at', 'status']

class EWayBillUploadResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    status = serializers.CharField()
    extracted_data = serializers.JSONField()
    message = serializers.CharField()


class MultipleEWayBillUploadSerializer(serializers.Serializer):
    pdf_files = serializers.ListField(
        child=serializers.FileField(
            max_length=100000, 
            allow_empty_file=False, 
            use_url=False
        ),
        allow_empty=False,
        write_only=True
    )

    def validate_pdf_files(self, value):
        # Limit to 10 files
        if len(value) > 10:
            raise serializers.ValidationError("You can upload a maximum of 10 PDFs at a time.")
        
        # Validate extensions & size (like single upload serializer)
        for file in value:
            ext = os.path.splitext(file.name)[1].lower()
            if ext != ".pdf":
                raise serializers.ValidationError(f"{file.name} is not a PDF.")
            if file.size > 10 * 1024 * 1024:  # 10MB
                raise serializers.ValidationError(f"{file.name} exceeds the 10MB size limit.")
        
        return value


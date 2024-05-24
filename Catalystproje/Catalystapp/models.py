from django.db import models

class UploadedData(models.Model):
      data_file = models.FileField(upload_to='uploads/')
      uploaded_at = models.DateTimeField(auto_now_add=True)
    


class DataRecord(models.Model):
      
      keyword = models.CharField(max_length=100)  # Add this line
      city = models.CharField(max_length=100, null=False )    
      employees_from = models.IntegerField()
      industry = models.CharField(max_length=100)
      state = models.CharField(max_length=100)
      employees_to = models.IntegerField()
      year_founded = models.IntegerField()
      country = models.CharField(max_length=100)

      # def __str__(self):
      #       return self.keyword
      
# class DataRecord(models.Model):
#       keyword = models.CharField(max_length=100)
#       city = models.CharField('City', max_length=100)
#       employees_from = models.CharField('Employees (From)', max_length=255)
#       industry = models.CharField('Industry', max_length=255)
#       state = models.CharField('State', max_length=100)
#       employees_to = models.CharField('Employees (To)', max_length=255)
#       year_founded = models.IntegerField('Year Founded')
#       country = models.CharField('Country', max_length=255)       
#       data_file = models.FileField(upload_to='uploads/')



from django.db import models

class City(models.Model):
      name = models.CharField(max_length=100)
      zone = models.CharField(max_length=100)

      def __str__(self):
            return self.name


class Rate(models.Model):
      zone = models.CharField(max_length=100)
      rate_per_kg = models.DecimalField(max_digits=10, decimal_places=2)

      def __str__(self):
            return f"{self.zone}: {self.rate_per_kg}"


from django.db import models

class BloodStock(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-'),
    ]
    group = models.CharField(max_length=3, choices=BLOOD_GROUPS, unique=True)
    units = models.PositiveIntegerField(default=0)
    threshold = models.PositiveIntegerField(default=5)
    

    def __str__(self):
        return f"{self.group}: {self.units} units"

class Donor(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=3, choices=BloodStock.BLOOD_GROUPS)
    email = models.EmailField()
    last_donation_date = models.DateField()
    is_eligible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.blood_group})"
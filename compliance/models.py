from django.db import models
from django.conf import settings
import datetime
from django.contrib.auth.models import User, AbstractUser

class Country(models.Model):
    name = models.CharField(max_length=40)
    abbreviation = models.CharField(max_length=2)
    vat_deadline = models.CharField(max_length=40)
    ec_sales_deadline = models.CharField(max_length=40)
    intrastat_deadline = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Division(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} {self.name}"

class TaxRegistration(models.Model):
    tax_id = models.CharField(max_length=12)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.tax_id

class Declaration(models.Model):
    DECLARATION_CHOICES = [
        ('VAT', 'VAT Return'),
        ('INT', 'Intrastat'),
        ('ECS', 'EC Sales List'),
    ]
    declaration_type = models.CharField(
        max_length=3,
        choices=DECLARATION_CHOICES,
        default='VAT'
    )
    month = models.CharField(max_length=40, null=True)
    year = models.CharField(max_length=40, null=True)
    period_start = models.DateField(null=True)
    period_end = models.DateField(null=True)
    is_payable = models.BooleanField(default=False)
    payable_receivable_amount = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    time_budget = models.IntegerField(default=60)
    is_submitted_for_review = models.BooleanField(default=False)
    is_reviewed = models.BooleanField(default=False)
    is_filed = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=100, default='not started')
    tax_registration = models.ForeignKey(TaxRegistration, on_delete=models.CASCADE, null=True)
    completion_pct = models.IntegerField(null=True)
    preparer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer', null=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='preparer', null=True)


    def __str__(self):
        return f"{self.declaration_type} {self.country} {self.month} {self.year}"

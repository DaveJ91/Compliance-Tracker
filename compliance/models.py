from django.db import models

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

class TeamMember(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    role = models.CharField(max_length=40)
    is_authorized_reviewer = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tax_Registration(models.Model):
    tax_id = models.CharField(max_length=12)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    divsion = models.ForeignKey(Division, on_delete=models.CASCADE)

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
    division = models.CharField(max_length=40)
    month = models.CharField(max_length=40)
    year = models.CharField(max_length=40)
    is_payable = models.BooleanField(default=False)
    payable_receivable_amount = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    preparer = models.CharField(max_length=40)
    time_budget = models.IntegerField()
    is_submitted_for_review = models.BooleanField(default=False)
    is_reviewed = models.BooleanField(default=False)
    is_filed = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.declaration_type
    




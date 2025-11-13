from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    baseQty = models.IntegerField()
    baseVal = models.DecimalField(max_digits=10, decimal_places=2)
    curQty = models.IntegerField()
    curVal = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    corpus = models.DecimalField(max_digits=10, decimal_places=2)
    portfolio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    companies = models.ManyToManyField(Company, blank=True, related_name='teams')

    def __str__(self):
        return self.name

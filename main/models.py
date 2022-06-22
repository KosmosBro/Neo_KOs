from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    company = models.ForeignKey(Company, related_name='category', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ['id', 'name']


class Contact(models.Model):
    type = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    company = models.ForeignKey(Company, related_name='contact', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.type

    class Meta:
        unique_together = ['id', 'type']


class Branch(models.Model):
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    company = models.ForeignKey(Company, related_name='branch', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.address

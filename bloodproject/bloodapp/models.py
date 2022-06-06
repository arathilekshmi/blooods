from django.db import models


class District(models.Model):
    name = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    # class Meta:
    #     db_table="district"
    def __str__(self):
        return self.name


class Center(models.Model):
    name = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    # class Meta:
    #     db_table="center"
    def __str__(self):
        return self.name

class Registrations(models.Model):
    class Meta:
        db_table = "registrations"

    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    gender = models.CharField(
        max_length=6,
        blank=True,
        null=True,
        choices=gender_choices,
    )

    email = models.EmailField(
        max_length=50,
        blank=True,
        null=True
    )

    age = models.CharField(
        max_length=3,
        blank=True,
        null=True,
    )
    address = models.TextField(
        max_length=50,
        blank=True,
        null=True,
    )
    district = models.ForeignKey(District,on_delete=models.SET_NULL,null=True)
    center=models.ForeignKey(Center,on_delete=models.SET_NULL,null=True)
    blood_group_choices = [
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b', 'B'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
    ]

    blood_group = models.CharField(
        max_length=4,
        blank=True,
        null=True,
        choices=blood_group_choices,
    )

    def __str__(self):
        return self.name




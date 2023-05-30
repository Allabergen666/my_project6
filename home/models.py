from django.db import models

# Create your models here.

# class Home(models.Model):
GENDER_CHOISE = (
    ("male", "Male"),
    ("female", "Female"),
    )

class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    phone = models.CharField(max_length=12, verbose_name="Phone")
    email = models.CharField(max_length=50, verbose_name="Email")
    gender = models.CharField(max_length=50, choices=GENDER_CHOISE, verbose_name="Gender")
    github = models.URLField(max_length=100, verbose_name="GitHub")
    image = models.ImageField(verbose_name="Image")



    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class Blog (models.Model):
    image = models.ImageField(upload_to="contact/", verbose_name="Image")
    firsname = models.CharField(max_length=50, verbose_name="Firstname")
    lastname = models.CharField(max_length=50, verbose_name="Lastname")
    email = models.EmailField(max_length=100, verbose_name="Email")
    phone = models.EmailField(max_length=12, verbose_name="Phone")
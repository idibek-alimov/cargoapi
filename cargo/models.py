from django.db import models

# Create your models here.


# class Message(models.Model):
#     text = models.CharField(max_length=50, blank=True)


class CalculatorData(models.Model):
    name = models.CharField(max_length=50, blank=True)
    number = models.CharField(max_length=50, blank=True)
    productType = models.CharField(max_length=50, blank=True)
    productName = models.CharField(max_length=50, blank=True)
    quantity = models.IntegerField()
    mass = models.DecimalField(
        max_digits=19, decimal_places=10, blank=True, null=True)
    deliveryMethod = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    insurance = models.BooleanField(default=False)
    comment = models.TextField(blank=True)
    deliveryPrice = models.DecimalField(
        max_digits=19, decimal_places=10, blank=True, null=True)
    deliveryTime = models.IntegerField(default=0, blank=True, null=True)
    checked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50, blank=True)
    number = models.CharField(max_length=50, blank=True)
    comment = models.TextField()
    deliveryMethod = models.CharField(
        max_length=50, blank=True, default="Авто", null=True)
    checked = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    question = models.CharField(max_length=50, blank=True)
    answer = models.TextField()

    def __str__(self) -> str:
        return self.question


class Feedback(models.Model):
    name = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    comment = models.TextField()
    pic = models.ImageField(upload_to="pics", default="hello1")
    video = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class MoscowPicture(models.Model):
    pic = models.ImageField(upload_to="pics", default="hello1")


class ChinaPicture(models.Model):
    pic = models.ImageField(upload_to="pics", default="hello1")


class Video(models.Model):
    upload = models.FileField(upload_to='videos/')

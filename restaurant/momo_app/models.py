from django.db import models

# Create your models here.
class Form(models.Model):
    name=models.CharField(max_length=50)
    number=models.CharField(max_length=50,null=True)
    email=models.EmailField()
    message=models.TextField()    

    def __str__(self):
        return self.name  

class Category(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Momo(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    desc=models.TextField()
    image=models.ImageField(upload_to='images')
    price=models.DecimalField(max_digits=8,decimal_places=2)
    is_available=models.BooleanField(default=True)
    create_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)
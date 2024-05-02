from django.db import models

# Create your models here.
class Taklif(models.Model):
    Title=models.CharField(max_length=50,verbose_name='عنوان')
    Author=models.CharField(max_length=30,verbose_name='نویسنده')
    content=models.TextField(verbose_name='متن')
    Date=models.DateTimeField(verbose_name='تاریخ')
    status=models.BooleanField(verbose_name='معلومه اشتباهه)وضعیت)')
    Email=models.EmailField(verbose_name="ایمیل")
    #picture=models.ImageField()
    def __str__(self):
        return f'{self.Title}'

from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    price       = models.DecimalField(decimal_places=2,max_digits=1000)
    summay      = models.TextField(blank=True, null=False)#blank torna o campo obrigatorio ou não
    featured    = models.BooleanField(default=True)
    #featured    = models.BooleanFiled(null=True)# Todos os valores anteriores serão vazios
    #summay      = models.TextField(default='this is cool!') 

    # def get_absolute_url(self):
    #     return f"/products/{self.id}/"

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"


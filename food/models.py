from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "kategoriya"
        verbose_name_plural = "kategoriyalar"
        ordering = ['name']  

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='food_photos/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    have = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ocqat soni"
        verbose_name_plural = "ocqat nomi"
        ordering = ['name'] 

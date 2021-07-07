from django.db import models
# Create your models here.


class Subscriber(models.Model):
    first_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, blank=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Name:{self.first_name}, Email: {self.email}"

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"
        ordering = ('first_name',)




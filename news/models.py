from django.db import models

# Create your models here.
class news(models.Model):
	title = models.CharField(max_length = 255)
	image = models.ImageField(upload_to="news/anons/%Y/%m/")
	def __str__(self):
		return self.title
	class Meta:
		verbose_name='Новость'
		verbose_name_plural='Новости'
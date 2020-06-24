from django.db import models


# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to = 'uploads/', blank = True, null=True)
	category = models.CharField(max_length=200)
	content = models.TextField()
	is_published = models.BooleanField(default=False)
	published_date =models.DateTimeField(blank=True ,null=True)
	modified_date = models.DateTimeField(blank=True , null=True)

	def __str__(self):
		return self.title


	class Meta:
		ordering = ('-published_date', )


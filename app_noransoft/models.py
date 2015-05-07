from django.db import models

# Create your models here.

class Category(models.Model):
	category = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.category)


class Blog(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	category = models.ForeignKey(Category, null=True, blank=True)

	def __unicode__(self):
		return unicode(self.title)


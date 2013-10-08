from django.db import models
from django.contrib.auth.models import User

class ProUser(models.Model):
	tel  = models.CharField(max_length=18)
	addr = models.CharField(max_length=50)
	QQ   = models.CharField(max_length=20,blank=True,null=True)
	user = models.ForeignKey(User)
	def __unicode__(self):
		return self.user.username

class Category(models.Model):
	name = models.CharField(max_length=20)
	p_category = models.ForeignKey('self',blank=True,null=True)
	def __unicode__(self):
		return self.name


class Goods(models.Model):
	name  = models.CharField(max_length=20)
	price = models.FloatField()
	img   = models.FileField(upload_to="./goodsImg") 
	info  = models.TextField()
	category = models.ForeignKey(Category)
	def __unicode__(self):
		return self.name

	

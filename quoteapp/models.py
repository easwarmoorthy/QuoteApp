from __future__ import unicode_literals

from django.db import models, migrations
# Create your models here.

#from django.contrib.auth.models import User

class QuoteModel(models.Model):
	quote = models.CharField(max_length = 150)
	qname = models.CharField(max_length = 25)
	def __str__(self):
		return self.quote

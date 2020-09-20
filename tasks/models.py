from django.db import models


class Task(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
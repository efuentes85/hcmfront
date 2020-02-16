from django.db import models
from bootstrap_datepicker_plus import DatePickerInput
from django import forms


class Schedule(models.Model):
	usuario = models.CharField(max_length=200)
	jornada = models.CharField(max_length=200)
	codigo = models.CharField(max_length=200)
	date = models.CharField(max_length=255)

	def __str__(self):
		return str(self.usuario)+ ' ' + self.codigo + ' ' + self.jornada + ' ' + self.date


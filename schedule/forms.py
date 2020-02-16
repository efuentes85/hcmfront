from django import forms
from .models import Schedule
from bootstrap_datepicker_plus import DatePickerInput


class ScheduleForm(forms.ModelForm):
	class Meta:
		model = Schedule
		fields = ["usuario", "jornada", "codigo", "date"]
		

# class ToDoForm(forms.Form):
#     todo = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control"})
#     )
#     date = forms.DateField(
#         widget=DatePickerInput(format='%m/%d/%Y')
#     )    


class NewSchedule(forms.Form):
	usuario = forms.CharField(label="Usuario", max_length=200)
	jornada = forms.CharField(label="Jornada", max_length=200)
	codigo = forms.CharField(label="codigo", max_length=200)
	date1 = forms.CharField(label="Hora Inicio", max_length=200)
	date2 = forms.CharField(label="Hora Termino", max_length=200)

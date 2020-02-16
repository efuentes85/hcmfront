from django.shortcuts import render
from .models import Schedule
from .forms import ScheduleForm, NewSchedule


def home(request):

	all_items = Schedule.objects.all
	return render(request, 'home.html', {'all_items':all_items})

def create(request):
	
	if request.method == 'POST':
		form = NewSchedule(request.POST or None)

		if form.is_valid():
			usuario = form.cleaned_data["usuario"]
			jornada = form.cleaned_data["jornada"]
			codigo = form.cleaned_data["codigo"]
			date = form.cleaned_data["date1"]
			t = Schedule(usuario=usuario, jornada=jornada, codigo=codigo, date=date)
			t.save()	
		return render(request, "create.html" , {"form": form})		

		
	else:
		form = NewSchedule()
			
	return render(request, "create.html" , {"form": form})


	# if request.method == 'POST':
	# 	form = ScheduleForm(request.POST or None)

	# 	if form.is_valid():
	# 		form.save()
	# 		all_items = Schedule.objects.all
	# 		return render(request, 'create.html' , {'all_items' : all_items})
	# else:
		
	# 	all_items = Schedule.objects.all
	# 	return render(request, 'create.html', {'all_items' : all_items})

# def create_user(request):
#     user_form = UserForm()
#     return render(request, 'my_template.html', {'my_form': user_form})
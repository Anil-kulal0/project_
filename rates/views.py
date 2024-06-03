from django.shortcuts import render
from .forms import LogisticsForm
from .models import Rate

def calculate_rate(from_zone, to_zone, kg):
      from_rate = Rate.objects.get(zone=from_zone).rate_per_kg
      to_rate = Rate.objects.get(zone=to_zone).rate_per_kg
      total_rate = (from_rate + to_rate) * kg
      return total_rate

def logistics(request):
      if request.method == 'POST':
            form = LogisticsForm(request.POST)
            if form.is_valid():
                  from_city = form.cleaned_data['from_city']
                  to_city = form.cleaned_data['to_city']
                  kg = form.cleaned_data['kg']
                  
                  from_zone = from_city.zone
                  to_zone = to_city.zone
                  
                  total_rate = calculate_rate(from_zone, to_zone, kg)
                  
                  return render(request, 'result.html', {'total_rate': total_rate})
      else:
            form = LogisticsForm()
      
      return render(request, 'form.html', {'form': form})
      

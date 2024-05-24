import csv
from django.shortcuts import render, redirect
from django.db import transaction
from .forms import UploadFileForm, DataFilterForm, LoginForm,DataRecordForm
from .models import UploadedData, DataRecord
from django.contrib.auth import authenticate, login







def login(request):
      form = LoginForm(request.POST or None)
      if request.method == 'POST':
            if form.is_valid():
                  username = form.cleaned_data.get('username')
                  password = form.cleaned_data.get('password')
                  user = authenticate(request, username=username, password=password)
                  if user is not None:
                        login(request, user)
                        return redirect('upload')  # Redirect to your desired page after login
                  else:
                        form.add_error(None, 'Invalid username or password')
      return render(request, 'login.html', {'form': form})


def upload_file(request):
      if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                  uploaded_file = form.save()
                  process_file(uploaded_file.data_file.path)
                  return redirect('success')
      else:
            form = UploadFileForm()
      return render(request,'upload.html', {'form': form})

# def upload_file(request):
#       if request.method == 'POST':
#             print("POST data:", request.POST)  # Debugging: Print POST data
#             form = UploadFileForm(request.POST, request.FILES)
#             if form.is_valid():
#                   uploaded_file = form.save()
#                   process_file(uploaded_file.data_file.path)
#                   return redirect('success')
#             else:
#                   print("Form errors:", form.errors)  # Debugging: Print form errors
#                   return render(request, 'upload.html', {'form': form})
#       else:
#             form = UploadFileForm()
#       return render(request, 'upload.html', {'form': form})
@transaction.atomic
def process_file(Documents):
      with open(Documents, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                  DataRecord.objects.create(
                  keyword=row[0],
                  city=row[1],
                  employees_from=row[2],
                  industry=row[3],
                  state=row[4],
                  employees_to=row[5],
                  year_founded=row[6],
                  country=row[7],
                  
                  # Add other columns as needed
                  )

def filter_data(request):
      form = DataFilterForm(request.GET or None)
      results = None
      if form.is_valid():
            filters = {}
            if form.cleaned_data['keyword']:
                  filters['keyword'] = form.cleaned_data['keyword']
            if form.cleaned_data['city']:
                  filters['city'] = form.cleaned_data['city']
            if form.cleaned_data['employees_from']:
                  filters['employees_from'] = form.cleaned_data['employees_from']
            if form.cleaned_data['industry']:
                  filters['industry'] = form.cleaned_data['industry']
            if form.cleaned_data['state']:
                  filters['state'] = form.cleaned_data['state']
            if form.cleaned_data['employees_to']:
                  filters['employees_to'] = form.cleaned_data['employees_to']
            if form.cleaned_data['year_founded']:
                  filters['year_founded'] = form.cleaned_data['year_founded']
            if form.cleaned_data['country']:
                  filters['country'] = form.cleaned_data['country']                              
            results = DataRecord.objects.filter(**filters)
      return render(request, 'filter.html', {'form': form, 'results': results})



def data_record(request):
      records = DataRecord.objects.all()
      return render(request, 'data_record.html', {'records': records})



def add_data(request):
      if request.method == 'POST':
            form = DataRecordForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect('data_record')
      else:
            form = DataRecordForm()
      return render(request, 'data_record.html', {'form': form})



from django.shortcuts import render
from .models import Person
from .resources import PersonResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']
        if not new_person.name.endswith('xlsx'):
            messages.info(request, 'wrong file')
            return render(request,'input.html')

            import_data = dataset.load(new_person.read(),format='xlsx')
            for data in import_data:
                value = Person(
                   data[0],
                   data[1],
                   data[2],
                   data[3]
                )
                value.save()
    return render(request,'input.html')

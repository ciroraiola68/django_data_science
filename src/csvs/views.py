from django.shortcuts import render
from .models import Csv
from .forms import CsvForm

def upload_file_view(request):
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()
    context = {
        "form": form
    }
    return render(request, "csvs/upload.html", context)


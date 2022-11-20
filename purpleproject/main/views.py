from django.shortcuts import render
from .forms import FotoForm
from .models import Foto
from django.http import HttpResponse

def main(request):
    form = FotoForm()
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            if 'img' in request.FILES:
                photo = request.FILES['img']

            return HttpResponse('image upload success')
        else:
            print(form.errors)
    return render(request, 'main/index.html', {'form': form})

def final(request):
    return render(request, 'main/final.html')





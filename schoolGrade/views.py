from django.shortcuts import render, redirect
from random import shuffle

from schoolGrade.forms import *
from schoolGrade.models import *

def get_base_context(pagename):
    context = dict()
    context['pagename'] = pagename
    return context

def main_page(request):
    context = get_base_context("Главная")
    context['classmates'] = Classmates.objects.all()
    return render(request, 'pages/main.html', context)


def create_columns(unsorted):
    into = len(unsorted)//4 + (1 if len(unsorted) % 4 != 0 else 0)
    for i in range(0, len(unsorted), into):
        yield unsorted[i:i + into]

def images_page(request):
    context = get_base_context("Фото")
    raw = list(Images.objects.all())
    shuffle(raw)
    context['photos'] = list(create_columns(raw))
    return render(request, 'pages/view-photos.html', context)


def upload(request):
    if request.method == 'POST':
        image_form = ImageUpload(request.POST, request.FILES)
        if image_form.is_valid():
            image_form.save()
            return redirect(to=upload)

        classmates = ClassmateAdd(request.POST)
        if classmates.is_valid():
            classmates.save()
            return redirect(to=upload)

    context = get_base_context("Загрузка")
    context['image_form'] = ImageUpload()
    context['classmate_form'] = ClassmateAdd()

    return render(request, 'pages/upload.html', context)


def view(request, id):
    context = get_base_context("Просмотр")
    context['classmate'] = Classmates.objects.get(id=id)

    return render(request, 'pages/view.html', context)

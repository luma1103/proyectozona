# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from .forms import LaboratorioForm, EventoForm
from controlapp.models import Laboratorio, Registro, Evento
from django.contrib.auth.decorators import login_required

@login_required
def lab_nuevo(request):
    formulario = LaboratorioForm()
    if request.method == "POST":
        formulario = LaboratorioForm(request.POST)
        if formulario.is_valid():
            laboratorio = Laboratorio.objects.create(nombre=formulario.cleaned_data['nombre'], encargado = formulario.cleaned_data['encargado'])
            for evento_id in request.POST.getlist('eventos'):
                registro = Registro(evento_id=evento_id, laboratorio_id = laboratorio.id)
                registro.save()
            messages.add_message(request, messages.SUCCESS, 'Registro realizado')
        else:
            formulario = LaboratorioForm()
    return render(request, 'controlapp/lab_nuevo.html', {'formulario': formulario})

@login_required
def evento_nuevo(request):
    formulario = EventoForm()
    if request.method == "POST":
        formulario = EventoForm(request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.save()
        messages.add_message(request, messages.SUCCESS, 'Registro realizado')

    return render(request, 'controlapp/evento_nuevo.html', {'formulario': formulario})

def post_list(request):
    laboratorios = Laboratorio.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'controlapp/post_list.html', {'laboratorios':laboratorios})

def post_detail(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    return render(request, 'controlapp/post_detail.html', {'laboratorio': laboratorio})

@login_required
def post_edit(request):
    post = get_object_or_404(Laboratorio, pk=pk)
    if request.method == "POST":
        form = LaboratorioForm(request.POST, instace=laboratorio)
        if form.is_valid():
            laboratorio = form.save(commit = False)
            laboratorio.save()
            return redirect('post_edit', pk=laboratorio.pk)
    else:
        form = LaboratorioForm(instace=laboratorio)
    return render(request, 'controlapp/post_edit.html', {'form':form})

@login_required
def post_delete(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    laboratorio.delete()
    return redirect('post_list')

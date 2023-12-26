from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import *
from .forms import*
from django.db.models import Count
from django.http import HttpResponse
import matplotlib.pyplot as plt
import mpld3
from io import BytesIO
import base64
import plotly.express as px
import plotly.io as pio
from io import BytesIO
from markupsafe import Markup 
import plotly.graph_objs as go
import os
# Create your views here.

def Login(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        pws = request.POST.get('pws')

        try:
            user = admin.objects.get(nom=nom, password=pws)
        except admin.DoesNotExist:
            # Handle the case where the user does not exist or the password is incorrect
            return render(request, 'forms/loginForm.html', {'error_message': 'Invalid username or password'})

        # Authentication successful, redirect to the home page
        return redirect('statistics')

    return render(request, 'forms/loginForm.html')


def SingIn(request):

    if request.method=='POST':
        
        nom=request.POST['nom']
        pasw=request.POST['pws']
        if nom and pasw :

            admin.objects.create(
                nom=nom,
                password=pasw
            )

            return redirect('login')

    return render(request,'forms/SignForm.html')

    return render(request,'forms/singForm.html')



def intervenant_list(request):
    intervenants = Intervenant.objects.all()
    return render(request, 'inervenant.html', {'intervenants': intervenants})



def intervenant_create(request):
    if request.method == 'POST':
        form = IntervenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('intervenant_list')
    else:
        form = IntervenantForm()
    return render(request, 'forms/intervenant_form.html', {'form': form})

def intervenant_edit(request, id_intervenant):
    intervenant = get_object_or_404(Intervenant, idInter=id_intervenant)
    if request.method == 'POST':
        form = IntervenantForm(request.POST, instance=intervenant)
        if form.is_valid():
            form.save()
            return redirect('intervenant_list')
    else:
        form = IntervenantForm(instance=intervenant)
    return render(request, 'forms/intervenant_form.html', {'form': form})

def intervenant_delete(request, id_intervenant):
    intervenant = get_object_or_404(Intervenant, idInter=id_intervenant)
    intervenant.delete()
    return redirect('intervenant_list')



def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client.html', {'clients': clients})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'forms/client_form.html', {'form': form})

def client_edit(request, id_client):
    client = get_object_or_404(Client, idclient=id_client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'forms/client_form.html', {'form': form})

def client_delete(request, id_client):
    client = get_object_or_404(Client, idclient=id_client)
    client.delete()
    return redirect('client_list')



def intervention_list(request):
    interventions = Intervention.objects.all()
    clients=Client.objects.all()
    intervenants=Intervention.objects.all()
    return render(request, 'intervention.html', {'interventions': interventions,'clients':clients,'intervenants':intervenants})


def intervention_create(request):
    if request.method == 'POST':
        form = InterventionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('intervention_list')
    else:
        form = InterventionForm()
    return render(request, 'forms/intervention_form.html', {'form': form})

def intervention_edit(request, id_intervention):
    intervention = get_object_or_404(Intervention, idintervention=id_intervention)
    if request.method == 'POST':
        form = InterventionForm(request.POST, instance=intervention)
        if form.is_valid():
            form.save()
            return redirect('intervention_list')
    else:
        form = InterventionForm(instance=intervention)
    return render(request, 'forms/intervention_form.html', {'form': form})

def intervention_delete(request, id_intervention):
    intervention = get_object_or_404(Intervention, idintervention=id_intervention)
    intervention.delete()
    return redirect('intervention_list')

# def home(request):

#     return render(request,'home.html')


def get_intervenant_percentage_data():
    intervenants = Intervenant.objects.all()

    data = {}

    for intervenant in intervenants:
        total_tasks = Intervention.objects.filter(id_intervenant=intervenant).count()
        completed_tasks = Intervention.objects.filter(id_intervenant=intervenant, etat='réalisée').count()

        if total_tasks > 0:
            percentage_completed = (completed_tasks / total_tasks) * 100
            data[intervenant.nom] = percentage_completed

    return data

def taches_realise_en_attente():
    interventions = Intervention.objects.all()

    # Calculer le pourcentage des tâches réalisées ou en attente
    total_tasks = interventions.count()
    completed_tasks = interventions.filter(etat='réalisée').count()
    pending_tasks = interventions.filter(etat='en attente').count()

    percentage_completed = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    percentage_pending = (pending_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    # Données pour le pie chart
    pie_chart_data = {
        'Réalisées': percentage_completed,
        'En attente': percentage_pending
    }

    

    return pie_chart_data


    
def generate_pie_chart(data, title):
    labels = list(data.keys())
    sizes = list(data.values())

    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes)])
    fig.update_layout(title=title)

    # Convertir la figure Plotly en HTML
    chart_html = Markup(fig.to_html(full_html=False))

    return chart_html

def statistics(request):
    
    intervenant_data = get_intervenant_percentage_data()
    intervenant_chart = generate_pie_chart(intervenant_data, 'Pourcentage des tâches réalisées par intervenant')
    
    taches_data = taches_realise_en_attente()
    taches_chart = generate_pie_chart(taches_data, 'Pourcentage des tâches réalisées et en attente')
    
    return render(request, 'home.html', {'intervenant_chart': intervenant_chart, 'taches_chart': taches_chart})

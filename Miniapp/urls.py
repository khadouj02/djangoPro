
from django.urls  import path
from .import views
from django.contrib.auth import views as auth_views
from .views import intervenant_list, intervenant_create, intervenant_edit, intervenant_delete
from .views import client_list,  client_create, client_edit, client_delete
from .views import intervention_list, intervention_create, intervention_edit, intervention_delete


urlpatterns =[
    path('',views.Login,name='login'),
    path('SingIn',views.SingIn,name='signin'),
    path('intervenants/', intervenant_list, name='intervenant_list'),
    path('intervenants/new/', intervenant_create, name='intervenant_create'),
    path('intervenants/<int:id_intervenant>/edit/', intervenant_edit, name='intervenant_edit'),
    path('intervenants/<int:id_intervenant>/delete/', intervenant_delete, name='intervenant_delete'),
    path('clients/', client_list, name='client_list'),
    path('clients/new/', client_create, name='client_create'),
    path('clients/<int:id_client>/edit/', client_edit, name='client_edit'),
    path('clients/<int:id_client>/delete/', client_delete, name='client_delete'),
    path('interventions/', intervention_list, name='intervention_list'),
    path('interventions/new/', intervention_create, name='intervention_create'),
    path('interventions/<int:id_intervention>/edit/', intervention_edit, name='intervention_edit'),
    path('interventions/<int:id_intervention>/delete/', intervention_delete, name='intervention_delete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('statistics/', views.statistics, name='statistics'),

]



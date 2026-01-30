from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path("", views.index,name="index"),
    path('about/', views.about, name='about'),
    path('special/', views.special, name='special'),
    path('product/', views.product, name='product'),
    path('service/', views.service, name='service'),
    path('air-conditioner-installation/', views.air_conditioner_installation, name='air_conditioner_installation'),
    path('electrical-appliance-repair-installation/', views.electrical_appliance_repair, name='electrical_appliance_repair'),
    path('new-switchboard-installation-repair/', views.new_switchboard_installation, name='new_switchboard_installation'),
    path('fan-supply-installation/', views.fan_supply_installation, name='fan_supply_installation'),
    path('light-repair-installation/', views.light_repair_installation, name='light_repair_installation'),
    path('new-powerpoints-installation-replacement/', views.new_powerpoints_installation, name='new_powerpoints_installation'),
    path('shed-granny-flat-power-connection/', views.shed_granny_power, name='shed_granny_power'),
    path('indoor-outdoor-installation/', views.indoor_outdoor_installation, name='indoor_outdoor_installation'),
    path('emergency-call-outs/', views.emergency_call_outs, name='emergency_call_outs'),
    path('smoke-alarms/', views.smoke_alarms, name='smoke_alarms'),
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact')
]
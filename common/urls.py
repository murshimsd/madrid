from django.urls import path
from . import views
 
app_name='common'   #for redirection purpose

urlpatterns=[
    path('',views.home,name='home'),
    path('fixtures',views.fixtures,name='fixtures'),
    path('madridistas',views.madridistas,name='madriditas'),
    path('players',views.players,name='players'),
    path('stores',views.stores,name='stores')
]
from django.urls import path
from . import views, api

app_name = 'sales'

urlpatterns = [
    path('', views.index, name='site_index'),
    path('upload', views.car_upload, name='Cars'),
    path('fetchdata', views.fetch, name='datafetch'),
    path(r'^searchdata/$', views.searchposts, name='searchlist'),
    path('add', views.addData, name='add'),
    path('submitadd', views.submitadd, name='submitadd'),
    path('savesCars', api.savesCars, name='savesCars'),

    # path('<sales_id>/update_view', views.update_view, name='update_view' ), 
    ]
    

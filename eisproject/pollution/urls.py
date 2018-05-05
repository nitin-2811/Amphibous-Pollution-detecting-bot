from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^send$', views.getdata, name='getdata'),
    url(r'detail',views.detail,name='detail'),
    url(r'map3',views.map3,name='heat map'),
    url(r'graph1',views.graph1,name='graph1'),
    url(r'graph2',views.graph2,name='graph2'),
    url(r'graph3',views.graph3,name='graph3')
]



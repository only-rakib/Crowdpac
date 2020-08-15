
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('home/', views.home_view, name='home'),
    path('petition/', views.petitionView, name='petition'),
    path('view_campaign/', views.view_campaignView, name='view_campaign'),
    path('view_petitions/', views.view_petitionsView, name='view_petitions'),
    path('contribute/<amount>', views.donateView, name='donate_page'),
    path('explore/', views.exploreView, name='explore'),
    path('crowdpac_tv/', views.crowdpac_tv_view, name='crowdpac_tv'),

]

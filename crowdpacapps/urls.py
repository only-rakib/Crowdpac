
from django.urls import path
from . import views
urlpatterns = [
    path('', views.petitionView, name='petition'),
    path('view_campaign/', views.view_campaignView, name='view_campaign'),
    path('view_petitions/', views.view_petitionsView, name='view_petitions'),
    path('contribute/<amount>', views.donateView, name='donate_page'),

]

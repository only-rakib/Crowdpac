
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('home/', views.home_view, name='home'),
    path('feed/', views.social_feed_View, name='feed'),
    path('view_campaign/', views.view_campaignView, name='view_campaign'),
    path('view_petitions/', views.view_petitionsView, name='view_petitions'),
    path('contribute/<amount>', views.donateView, name='donate_page'),
    path('explore/', views.exploreView, name='explore'),
    path('crowdpac_tv/', views.crowdpac_tv_view, name='crowdpac_tv'),
    path('start_campaign/', views.start_campaign_view, name='start_campaign'),
    path('pricing/', views.pricing_view, name='pricing'),
    path('media/', views.media_view, name='media'),
    path('privacy_policy/', views.privacy_policy_view, name='privacy_policy'),
    path('terms/', views.terms_view, name='terms'),
    path('jobs/', views.jobs_view, name='jobs'),
    path('jobs/', views.jobs_view, name='jobs'),
    path('about_us/', views.about_us_view, name='about_us'),
    path('my_campaigns/', views.my_campaigns_view, name='my_campaigns'),
    path('signin/', views.signin_view, name='signin'),
    path('remaind/', views.remaind_view, name='remaind'),
    path('start_rally/', views.start_rally_view, name='start_rally'),
    path('notifications/', views.notifications_view, name='notifications'),

]

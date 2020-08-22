from django.shortcuts import render
from itertools import chain
from .models import Donar_list, Endorsement_list

login = "f"


def home_view(request):
    global login
    return render(request, 'index.html', {'login': login})


def exploreView(request):
    return render(request, 'explore.html')


def crowdpac_tv_view(request):
    return render(request, 'crowdpac_tv.html')


def social_feed_View(request):
    global login
    #donar_orders = Donar_list.objects.all()

    #endorse_orders = Endorsement_list.objects.all()
    # orders = list(
    #    sorted(
    #        chain(donar_orders, endorse_orders),
    #        key=lambda objects: objects.created
    #    ))
    #paginator = Paginator(orders, 5)
    news1 = {
        'newspaper_name': 'Plastics News',
        'date_time': 'Aug 17th 06:00 pm',
        'news_link': 'https://www.plasticsnews.com/blog/kickstart-plastics-and-politics-head-state-level',
        'news_title': 'Kickstart: Plastics and politics head to the state level',
        'news_pic': 'images/udall-05_i.jpg'
    }
    news2 = {
        'newspaper_name': 'GoLocalProv',
        'date_time': 'Aug 17th 06:00 pm',
        'news_link': 'https://www.golocalprov.com/cache/images/remote/https_s3.amazonaws.com/media.golocalprov.com/Fung_and_Council_Candidates_No_Masks_August_2020.png',
        'news_title': 'News | Politics of Coronavirus: Fung and GOP Candidates Fail to Wear Masks for Political Photo',
        'news_pic': 'images/Fung_and_Council_Candidates_No_Masks_August_2020.png'
    }
    lstNews = []
    lstNews.append(news1)
    lstNews.append(news2)

    tv1 = {
        'tv_reporter_pro_pic': 'images/lhbebvoswhrprssro4ar.jpg',
        'tv_reporter_name': 'Aimee Rivera Cole',
        'tv_reporter_profile_link': '#',
        'tv_reporter_category': 'Candidate Video',
        'tv_title': 'Aimee Rivera Cole for State Representative | Committed To Indiana',
        'tv_video_src': "https://res.cloudinary.com/crowdpac/video/upload/v1593640761/videos/campaigns/395501/1.mp4#t=0.1",
        'tv_campaign_link': 'view_campaign',
        'tv_details': '''Indiana needs change and can't keep using the same old playbook. I'm running against the House Speaker who is commanding over a Republican supermajority in the Indiana State House. We can …''',
    }
    lstTv = []
    lstTv.append(tv1)
    first_topic_petition = {

        'reporter_pro_pic': 'lhbebvoswhrprssro4ar.jpg',
        'reporter_name': 'Rent Strike 2020 ',
        'date': ' 4 months ago',
        'title': 'Rent Strike 2020',
        'image': 'rentstrike_ry2ddq.jpg',
        'details': '''Rent Strike 2020 is a response to a the signed demand of over 1.5 million Americans who need immediate,\
             structural economic relief during the COVID-19 pandemic.
              Our initial demand is simple: every governor, in every state,
               must do what is necessary t..''',
        'view_url': 'view_petitions',
        'signeture_count': '1.8m'
    }
    second_topic_petition = {

        'reporter_pro_pic': 'lhbebvoswhrprssro4ar.jpg',
        'reporter_name': 'Rent Strike 2020 ',
        'date': ' 4 months ago',
        'title': 'Rent Strike 2020',
        'image': 'rentstrike_ry2ddq.jpg',
        'details': '''Rent Strike 2020 is a response to a the signed demand of over 1.5 million Americans who need immediate,\
             structural economic relief during the COVID-19 pandemic.
              Our initial demand is simple: every governor, in every state,
               must do what is necessary t..''',
        'view_url': 'view_petitions',
        'signeture_count': '1.8m'
    }
    lstPetition = []
    lstPetition.append(first_topic_petition)
    lstPetition.append(second_topic_petition)
    return render(request, 'social_feed.html', {'news': lstNews, 'tv': lstTv, 'data': lstPetition, 'login': login})


def view_campaignView(request):

    post = {
        'post_title': 'Rent Strike 2020',
        'video_link': 'https://www.youtube.com/embed/ozRlOJyuJfU',
        'reporter_pro_pic': 'lhbebvoswhrprssro4ar.jpg',  # see the location in html
        'reporter_name': 'Rent Strike 2020',
        'reporter_position': 'Campaign creator',
        'reporter_org_type': 'Non-profit',
        'reporter_url': '#'
    }
    support = {
        'donate_button_name': 'Donate $20',
        'donate_title': 'Support this campaign!',
        'update_title': 'Campaign created! ',
        'endorsement_title': 'Show your support for this campaign by endorsing it and sharing why! ',
        'endorsement_status': 'true',
        'endorsement_count': '814',
        'story_details': '''What’s at Stake? Beginning on April 1st,
         2020, many Americans will be unable to pay their rent, mortgage,
          loans, or utility bills in the context of the pandemic and global
           recession. The president has so far spent $2.5 trillion in bailing
            out the stock market and large corporations, and nothing to bail
             out the working class. Without a massive stimulus package, freeze
              on rent, utilities, and mortgage collection, millions of people
               will lose their jobs and homes. Unemployment could reach 30%
                according to some projections. We have to start organizing 
                right now, turn our collective desperation to collective power,
                 and force our government to enact a bailout for regular people, not Wall Street.''',
        'number_of_pledge': '',
        'percent': '',
        'goal': ''

    }
    endorsed_people1 = {
        'end_pro_pic': 'images/lhbebvoswhrprssro4ar.jpg',
        'end_name': 'rakib',
        'end_status': 'endorsed',
        'end_comment': '',
        'end_pro_data_letter': '',
    }
    endorsed_people2 = {
        'end_pro_pic': 'none',
        'end_name': 'rakib',
        'end_status': 'endorsed',
        'end_comment': '''e all need to stand together and fight for what is right. And this campaign knows what's right ''',
        'end_profile': '#',
        'end_pro_data_letter': 'r'
    }
    lstend = []
    lstend.append(endorsed_people1)
    lstend.append(endorsed_people2)

    donar_1 = {
        'donar_name': 'Meera Bajwa',
        'donate_amount': '$20',
        'time_ago': '2 months ago ',
    }
    donar_2 = {
        'donar_name': 'rakib',
        'donate_amount': '$50',
        'time_ago': '6 months ago ',
    }
    lstdon = []
    lstdon.append(donar_1)
    lstdon.append(donar_2)
    tagDic1 = {
        'name': 'Union Rights',
        'url': '#',
    }
    tagDic2 = {
        'name': 'Civil Rights',
        'url': '#',
    }
    tagDic3 = {
        'name': 'Civil Rights',
        'url': '#',
    }
    taglst = []
    taglst.append(tagDic1)
    taglst.append(tagDic2)
    taglst.append(tagDic3)
    context = {
        'post': post,
        'support': support,
        'endorsed_people': lstend,
        'donars': lstdon,
        'tags': taglst,
        'login': login
    }

    return render(request, 'view_campaign.html', context)


def view_petitionsView(request):
    return render(request, 'view_petitions.html', {'login': login})


def donateView(request, amount):
    if amount == "20":

        total = {'amount': '20.00', 'tip': '2.00',
                 'handle': '0.83', 'total': ' 22.83'}

    elif amount == "27":

        total = {'amount': '27.00', 'tip': '2.70',
                 'handle': '1.05', 'total': ' 30.75'}

    elif amount == "50":

        total = {'amount': '50.00', 'tip': '5.00',
                 'handle': '1.79', 'total': ' 56.79'}

    elif amount == "100":

        total = {'amount': '100.00', 'tip': '10.00',
                 'handle': '3.39', 'total': ' 113.39'}

    return render(request, 'donate_page.html', {'data': total, 'login': login})


def start_campaign_view(request):
    global login
    if login == 'True':
        return render(request, 'startcampaign.html', {'login': login})
    else:

        return render(request, 'startcampaignSignup.html', {'login': login})


def pricing_view(request):
    return render(request, 'Pricing.html', {'login': login})


def media_view(request):
    return render(request, 'media.html', {'login': login})


def privacy_policy_view(request):
    return render(request, 'privacy_policy.html', {'login': login})


def terms_view(request):
    return render(request, 'terms_of_service.html', {'login': login})


def jobs_view(request):
    return render(request, 'jobs.html', {'login': login})


def about_us_view(request):
    return render(request, 'about_us.html', {'login': login})


def my_campaigns_view(request):
    return render(request, 'my_campaigns.html', {'login': login})


def signin_view(request):
    return render(request, 'signin.html',)


def remaind_view(request):
    return render(request, 'forgotpass.html',)

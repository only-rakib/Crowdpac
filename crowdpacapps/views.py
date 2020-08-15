from django.shortcuts import render
from itertools import chain
from .models import Donar_list, Endorsement_list


def home_view(request):
    return render(request, 'index.html')


def exploreView(request):
    return render(request, 'explore.html')


def crowdpac_tv_view(request):
    return render(request, 'crowdpac_tv.html')


def petitionView(request):
    donar_orders = Donar_list.objects.all()

    endorse_orders = Endorsement_list.objects.all()
    orders = list(
        sorted(
            chain(donar_orders, endorse_orders),
            key=lambda objects: objects.created
        ))
    #paginator = Paginator(orders, 5)

    first_topic = {

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
    second_topic = {

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
    lst = []
    lst.append(first_topic)
    lst.append(second_topic)
    return render(request, 'Petitions.html', {'data': lst})


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
    }
    endorsed_people2 = {
        'end_pro_pic': 'images/lhbebvoswhrprssro4ar.jpg',
        'end_name': 'rakib',
        'end_status': 'endorsed',
        'end_comment': '''e all need to stand together and fight for what is right. And this campaign knows what's right ''',
        'end_profile': '#',
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
    taglst = []
    taglst.append(tagDic1)
    taglst.append(tagDic2)
    context = {
        'post': post,
        'support': support,
        'endorsed_people': lstend,
        'donars': lstdon,
        'tags': taglst,
    }

    return render(request, 'view_campaign.html', context)


def view_petitionsView(request):
    return render(request, 'view_petitions.html')


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

    return render(request, 'donate_page.html', {'data': total})

from django.shortcuts import render
from itertools import chain
from .models import Donar_list, Endorsement_list
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from json import loads as jsonloads
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

login = "True"


def home_view(request):
    global login
    return render(request, 'index.html')


def exploreView(request):
    return render(request, 'explore.html')


def crowdpac_tv_view(request):
    return render(request, 'crowdpac_tv.html')


def social_feed_View(request):
    global login
    # donar_orders = Donar_list.objects.all()

    # endorse_orders = Endorsement_list.objects.all()
    # orders = list(
    #    sorted(
    #        chain(donar_orders, endorse_orders),
    #        key=lambda objects: objects.created
    #    ))
    # paginator = Paginator(orders, 5)
    # Campaign Start

    campaign_1 = {

        'campaign_title': "26-year old truck driver & climate activist fighting for the working class",
        'campaign_cover_image': "images/gvmy4rgh6fkxr9jk0mnv.png",
        'campaign_content_writer': "Joshua Collins",
        'campaign_content_year': "2021",
        'campaign_content_writer_address': "U.S. House, 10th District,",
        'campaign_content_writer_state': "WA",
        'campaign_story': '''I've been a trucker for 5 years, and part of the workforce for over 11 years. I grew up poor in the Midwest; my college plans...''',
        'campaign_content_tags': ['Climate Change', 'Health care', 'Immigration Reform', 'LGBTQ Rights Inequality', 'Income Inequality'],
        'campaign_raised_amount': 868,
        'Fundraising_Goal': 3000,
        'campaign_raised_amount_percentanges': (868 / 3000) * 100,
        'campaign_supporter': 22,
        'gender': 'Female',
        'political_affiliation': 'Independent',
        'recipient': 'Organization',
        'upload_time': '20200907010001',  # yyyyMMddHHmmss
    }
    campaign_2 = {

        'campaign_title': "26-year old truck driver & climate activist fighting for the working class",
        'campaign_cover_image': "images/cyst94ggea6r6iag1568.png",
        'campaign_content_writer': "Joshua Collins",
        'campaign_content_year': "2020",
        'campaign_content_writer_address': "U.S. House, 10th District,",
        'campaign_content_writer_state': "WA",
        'campaign_story': '''I've been a trucker for 5 years, and part of the workforce for over 11 years. I grew up poor in the Midwest; my college plans...''',
        'campaign_content_tags': ['Environment', 'Gender Equality', ' Gun Safety'],
        'campaign_raised_amount': 880,
        'Fundraising_Goal': 1000,
        'campaign_raised_amount_percentanges': (880 / 1000) * 100,
        'campaign_supporter': 22,
        'gender': 'Male',
        'political_affiliation': 'Democrat',
        'recipient': 'Candidate',
        'upload_time': '20200906010001',
    }
    campaign_3 = {

        'campaign_title': "26-year old truck driver & climate activist fighting for the working class",
        'campaign_cover_image': "images/iizefpiztgn8bo2vindb.png",
        'campaign_content_writer': "Joshua Collins",
        'campaign_content_year': "2020",
        'campaign_content_writer_address': "U.S. House, 10th District,",
        'campaign_content_writer_state': "WA",
        'campaign_story': '''I've been a trucker for 5 years, and part of the workforce for over 11 years. I grew up poor in the Midwest; my college plans...''',
        'campaign_content_tags': ['Environment', 'Gender Equality', ' Gun Safety'],
        'campaign_raised_amount': 3000,
        'Fundraising_Goal': 10000,
        'campaign_raised_amount_percentanges': (3000 / 10000) * 100,
        'campaign_supporter': 22,
        'gender': 'Male',
        'political_affiliation': 'Democrat',
        'recipient': 'Candidate',
        'upload_time': '20190907230005',
    }
    lst_campaign = []
    lst_campaign.append(campaign_1)
    lst_campaign.append(campaign_2)
    lst_campaign.append(campaign_3)
    # Campaign end
    # News Start
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

    # News End

    # TV start
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
    # TV end
    # petition Start
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
    # petition end
    # member Start
    member1 = {
        'member_name': 'xyz',
        "member_pro_pic": "none",
        'memberDataLetter': 'X',
        'memberId': 1,
        'tagValue': 'tag-1' + ' ' + 'tag-2' + ' ' + 'tag-3'
    }
    member2 = {
        'member_name': 'abc',
        "member_pro_pic": "none",
        'memberDataLetter': 'A',
        'memberId': 1,
        'tagValue': 'tag-2' + ' ' + 'tag-3' + ' ' + 'tag-4'
    }
    member3 = {
        'member_name': 'xyzz',
        "member_pro_pic": "none",
        'memberDataLetter': 'X',
        'memberId': 1,
        'tagValue': 'tag-4' + ' ' + 'tag-5' + ' ' + 'tag-6',
    }
    lstMember = []
    lstMember.append(member1)
    lstMember.append(member2)
    lstMember.append(member3)
    # member end
    return render(request, 'social_feed.html', {'news': lstNews, 'tv': lstTv, 'data': lstPetition, 'login': login, 'member': lstMember, 'campaign': lst_campaign})


def view_campaignView(request):
    candidate_self_or_not = "No"
    post = {
        'post_title': 'Rent Strike 2020',
        'video_link': 'https://www.youtube.com/embed/ozRlOJyuJfU',
        'cover_pic': "",
        'reporter_pro_pic': 'lhbebvoswhrprssro4ar.jpg',  # see the location in html
        'reporter_name': 'Rent Strike 2020',
        'reporter_position': 'Campaign creator',
        'reporter_org_type': 'Non-profit',
        'reporter_url': '#'
    }
    support = {
        # if candidate_self_or_not is No then Pledge Otherwise Donate
        'candidate_self_or_not': candidate_self_or_not,
        'Fundraising_Goal': 2000,
        'campaign_raised_amount': 868,
        'campaign_raised_amount_percentanges': (868 / 2000) * 100,
        'campaign_supporter': 22,
        'Default_Donation': '20.00',
        'Default_Donation_tips': '2.00',
        'Default_Donation_handling': '0.83',
        'Default_Donation_total': '22.83',
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
        'end_comment': '''We all need to stand together and fight for what is right. And this campaign knows what's right.Praesent luctus at erat at sagittis. Etiam posuere, erat nec laoreet ornare, odio dui mattis nisl, convallis semper ligula lectus eu turpis. Phasellus pharetra risus tortor, eget fringilla tortor laoreet at. Quisque egestas tristique dui. Mauris non iaculis ex. Ut pellentesque, massa ut molestie egestas, tortor leo imperdiet sem, vitae malesuada nibh dolor in magna. Etiam pulvinar pharetra dolor, vel dapibus ipsum commodo eget. Praesent turpis odio, suscipit ut ullamcorper vel, finibus at ligula. Phasellus dolor lectus, molestie a velit sed, iaculis rhoncus risus. Ut id pellentesque erat, quis elementum ligula. Donec dignissim diam sem, a bibendum erat mattis quis. Vivamus id erat dui. Vestibulum sollicitudin ac justo at lacinia.  ''',
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
        'id': 'tag18',
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

    donateButtonsDic1 = {
        'amount': '20.00',
        'tip': '2.00',
        'handle': '0.83',
        'total': ' 22.83'

    }
    donateButtonsDic2 = {

        'amount': '27.00',
        'tip': '2.70',
        'handle': '1.05',
        'total': ' 30.75'

    }
    donateButtonsDic3 = {
        'amount': '50.00',
        'tip': '5.00',
        'handle': '1.79',
        'total': ' 56.79'

    }
    donateButtonsDic4 = {
        'amount': '100.00',
        'tip': '10.00',
        'handle': '3.39',
        'total': ' 113.39'

    }

    donateButtonList = []
    donateButtonList.append(donateButtonsDic1)
    donateButtonList.append(donateButtonsDic2)
    donateButtonList.append(donateButtonsDic3)
    donateButtonList.append(donateButtonsDic4)

    otherDonate1 = {
        'amount': '20.00',
        'tip': '2.00',
        'handle': '0.83',
        'total': ' 22.83'

    }
    otherDonate2 = {

        'amount': '27.00',
        'tip': '2.70',
        'handle': '1.05',
        'total': ' 30.75'

    }
    otherDonate3 = {
        'amount': '50.00',
        'tip': '5.00',
        'handle': '1.79',
        'total': ' 56.79'

    }
    otherDonate4 = {
        'amount': '100.00',
        'tip': '10.00',
        'handle': '3.39',
        'total': ' 113.39'

    }
    otherDonatelist = []
    otherDonatelist.append(otherDonate1)
    otherDonatelist.append(otherDonate2)
    otherDonatelist.append(otherDonate3)
    otherDonatelist.append(otherDonate4)
    context = {
        'post': post,
        'support': support,
        'endorsed_people': lstend,
        'donars': lstdon,
        'tags': taglst,
        'donateButtons': donateButtonList,
        'Fundraising_Goal': 1000,
        'otherDonate': otherDonatelist,
        'login': login,
    }

    return render(request, 'view_campaign.html', context)


def view_petitionsView(request):
    data = {
        'title': 'Rent Strike 2020 ',
        'des': '''Ever man are put down his very. And marry may table him avoid. Hard sell it were into it upon. He forbade affixed parties of assured to me windows. Happiness him nor she disposing provision. Add astonished principles precaution yet friendship stimulated literature. State thing might stand one his plate. Offending or extremity therefore so difficult he on provision. Tended depart turned not are.
                            Not far stuff she think the jokes. Going as by do known noise he wrote round leave. Warmly put branch people narrow see. Winding its waiting yet parlors married own feeling. Marry fruit do spite jokes an times. Whether at it unknown warrant herself winding if. Him same none name sake had post love. An busy feel form hand am up help. Parties it brother amongst an fortune of. Twenty behind wicket why age now itself ten.
                            Perhaps far exposed age effects. Now distrusts you her delivered applauded affection out sincerity. As tolerably recommend shameless unfeeling he objection consisted. She although cheerful perceive screened throwing met not eat distance. Viewing hastily or written dearest elderly up weather it as. So direction so sweetness or extremity at daughters. Provided put unpacked now but bringing.''',
        'cover_pic': "images/rentstrike_ry2ddq.jpg",
    }
    # signeture is sample data.

    signeture = [
        {
            "id": 4051,
            "name": "manoj",
            "email": "manoj@gmail.com",

        },
        {
            "id": 4050,
            "name": "pankaj",
            "email": "p1@gmail.com",

        },
        {
            "id": 3050,
            "name": "Neeraj1993",
            "email": "neeraj.singh@adequateinfosoft.com",

        },
        {
            "id": 3049,
            "name": "Sophia",
            "email": "sophia@gmail.com",

        },
        {
            "id": 3048,
            "name": "Raju Prasad",
            "email": "raju.nsit@gmail.com",

        },
        {
            "id": 3047,
            "name": "Ankiish Thapliyal",
            "email": "thapliyalankiish958@gmail.com",

        },
        {
            "id": 3046,
            "name": "Aryan Thapliyal",
            "email": "ashithewarrior@gmail.com",

        },
        {
            "id": 3045,
            "name": "shivam",
            "email": "shivam@gmail.com",

        },
        {
            "id": 3044,
            "name": "Navya Upadhyay",
            "email": "navya.adequate@gmail.com",

        },
        {
            "id": 3043,
            "name": "Ritu singh",
            "email": "ritusinghadequate@gmail.com",

        },
        {
            "id": 3042,
            "name": "faiz",
            "email": "faizadequate@gmail.com",

        },
        {
            "id": 3041,
            "name": "Martin Wilson",
            "email": "ravencomputer667@gmail.com",

        },
        {
            "id": 3040,
            "name": "Shweta Singh",
            "email": "amelia.claire.hi@gmail.com",

        },
        {
            "id": 3039,
            "name": "jagjit",
            "email": "jagjit.singh.adequate.36@gmail.com",

        },
        {
            "id": 3038,
            "name": "Ashi 123",
            "email": "ashi123@gmail.com",

        },
        {
            "id": 3037,
            "name": "shivamvermaa4",
            "email": "shivam.vemaa4@gmail.com",

        },
        {
            "id": 3036,
            "name": "Sophia",
            "email": "n2@gmail.com",

        },
        {
            "id": 3035,
            "name": "n1",
            "email": "n1@gmail.com",

        },
        {
            "id": 3034,
            "name": "neha",
            "email": "neha@gmail.com",

        },
        {
            "id": 3033,
            "name": "sanjay",
            "email": "sanjay@gmail.com",

        },
        {
            "id": 3032,
            "name": "Akku2",
            "email": "akku2@gmail.com",

        },
        {
            "id": 3031,
            "name": "Ashish Thapliyal",
            "email": "ashi1@gmail.com",

        },
        {
            "id": 3030,
            "name": "singh",
            "email": "singh@gmail.com",

        },
        {
            "id": 3029,
            "name": "Akku Testing",
            "email": "akku1@gmail.com",

        },
        {
            "id": 3028,
            "name": "Aakankshi Gupta",
            "email": "aakankshi.cuminte@gmail.com",

        },

        {
            "id": 3022,
            "name": "Raju Prasad",
            "email": "raju.prasad@adequateinfosoft.com",

        },
        {
            "id": 3021,
            "name": "Ashok Patel",
            "email": "ashoktest@gmail.com",

        },
        {
            "id": 2021,
            "name": "manresh1",
            "email": "manresh1@gmail.com",

        },
        {
            "id": 2020,
            "name": "Manresh Chandra",
            "email": "manresh@gmail.com",

        },
        {
            "id": 2019,
            "name": "Test",
            "email": "aakankshi7@gmail.com",

        },
        {
            "id": 2018,
            "name": "aakankshi6",
            "email": "aakankshi6@gmail.com",

        },
        {
            "id": 2017,
            "name": "aakankshi5",
            "email": "aakankshi5@gmail.com",

        },

    ]
    return render(request, 'view_petitions.html', {'context': data, 'signetures': signeture})


def donateView(request, amount):
    # view_campaign.html <!-- Donate card side contents start-->
    if amount == "20.00":

        total = {'amount': '20.00', 'tip': '2.00',
                 'handle': '0.83', 'total': ' 22.83'}

    elif amount == "27.00":

        total = {'amount': '27.00', 'tip': '2.70',
                 'handle': '1.05', 'total': ' 30.75'}

    elif amount == "50.00":

        total = {'amount': '50.00', 'tip': '5.00',
                 'handle': '1.79', 'total': ' 56.79'}

    elif amount == "100.00":

        total = {'amount': '100.00', 'tip': '10.00',
                 'handle': '3.39', 'total': ' 113.39'}

    return render(request, 'donate_page.html', {'data': total, })


@csrf_exempt
def start_campaign_view(request):
    # in this all data for the startcampaing.
    # see the comments to know where the events occur
    global login
    userList = [
        {
            "id": 4051,
            "value": "manoj",
            "descprition": "manoj@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"

        },
        {
            "id": 4050,
            "value": "pankaj",
            "descprition": "p1@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3050,
            "value": "Neeraj1993",
            "descprition": "neeraj.singh@adequateinfosoft.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3049,
            "value": "Sophia",
            "descprition": "sophia@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3048,
            "value": "Raju Prasad",
            "descprition": "raju.nsit@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3047,
            "value": "Ankiish Thapliyal",
            "descprition": "thapliyalankiish958@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3046,
            "value": "Aryan Thapliyal",
            "descprition": "ashithewarrior@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3045,
            "value": "shivam",
            "descprition": "shivam@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3044,
            "value": "Navya Upadhyay",
            "descprition": "navya.adequate@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3043,
            "value": "Ritu singh",
            "descprition": "ritusinghadequate@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3042,
            "value": "faiz",
            "descprition": "faizadequate@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3041,
            "value": "Martin Wilson",
            "descprition": "ravencomputer667@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3040,
            "value": "Shweta Singh",
            "descprition": "amelia.claire.hi@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3039,
            "value": "jagjit",
            "descprition": "jagjit.singh.adequate.36@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3038,
            "value": "Ashi 123",
            "descprition": "ashi123@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3037,
            "value": "shivamvermaa4",
            "descprition": "shivam.vemaa4@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3036,
            "value": "Sophia",
            "descprition": "n2@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3035,
            "value": "n1",
            "descprition": "n1@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3034,
            "value": "neha",
            "descprition": "neha@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3033,
            "value": "sanjay",
            "descprition": "sanjay@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3032,
            "value": "Akku2",
            "descprition": "akku2@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3031,
            "value": "Ashish Thapliyal",
            "descprition": "ashi1@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3030,
            "value": "singh",
            "descprition": "singh@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3029,
            "value": "Akku Testing",
            "descprition": "akku1@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3028,
            "value": "Aakankshi Gupta",
            "descprition": "aakankshi.cuminte@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },

        {
            "id": 3022,
            "value": "Raju Prasad",
            "descprition": "raju.prasad@adequateinfosoft.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 3021,
            "value": "Ashok Patel",
            "descprition": "ashoktest@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 2021,
            "value": "manresh1",
            "descprition": "manresh1@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 2020,
            "value": "Manresh Chandra",
            "descprition": "manresh@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 2019,
            "value": "Test",
            "descprition": "aakankshi7@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 2018,
            "value": "aakankshi6",
            "descprition": "aakankshi6@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },
        {
            "id": 2017,
            "value": "aakankshi5",
            "descprition": "aakankshi5@gmail.com",
            "img": "http://images.maskworld.com/is/image/maskworld/bigview/john-doe-foam-latex-mask--mw-117345-1.jpg"
        },

    ]
    states_city = {
        # Add  all the city list where AL = ALABAMA
        # the list contains the states/citys of ALABAMA
        'AL': ['Auburn', 'Baldwin County', 'Bay Minette', 'Bessemer']
    }
    race_list = {
        # list all the election where the First element is the location
        # the table populate "location|Office|Next Election date|"
        # idl1,idl2 is the id for these data
        # These items poputales in #stateTable in race_info.html
        'lst': [
            ['Auburn', 'kayor', '5/28/2022', 'idl1'],
            ['Auburn', 'Mayor', '5/28/2022', 'idl2'],
            ['Baldwin County', 'Mayor', '5/28/2022', 'idl3'],
            ['Baldwin County', 'Mayor', '5/28/2022', 'idl4'],
            ['VI', 'Mayor', '5/28/2022', 'ids1'],
            ['AL', 'Mayor', '5/28/2022', 'ids1']
        ],
    }
    race_local = {
        # list all the election where the First element is the location
        # the table populate "location|Office|Next Election date|"
        # idl1,idl2 is the id for these data
        # These items poputales in #localTable and federalTable in
        # race_info.html
        'lst': [
            ['Auburn', 'kayor', '5/28/2022', 'idl1'],
            ['Auburn', 'Mayor', '5/28/2022', 'idl2'],
            ['Baldwin County', 'Mayor', '5/28/2022', 'idl3'],
            ['Baldwin County', 'Mayor', '5/28/2022', 'idl4'],
        ],
    }
    candidancy = ''  # self candidate or any organization
    name = ""  # name of the candidate
    pro_pic = ""  # candidate profile pic
    data_letter = ""  # if no profile pic then show the first letter
    pro_id = ""  # id of the profile from db
    campaign_title = ""
    video_url = ""
    cover_pic = ""
    Default_Donation = ""
    optional_settings = ""
    Other_donation_amounts1 = ""
    Other_donation_amounts2 = ""
    Other_donation_amounts3 = ""
    campaign_story = ""
    data = {}
    if login == 'True':
        if request.is_ajax and request.method == "POST":
            candidate = request.POST.get("candidate")
            print(candidate)
            # request comes from campaign_recipients.html
            # "$("#recipients_save_button_select_candidate").on('click',
            # function() {"
            if candidate == 'candidate_self':
                candidancy = candidate
                name = "rakib"  # if self then the user data will come from database for current user
                pro_pic = "none"
                data_letter = name[0]
                data = {
                    'candidancy': candidate,
                    'name': name,
                    'pro_pic': pro_pic,
                    'data_letters': data_letter,


                }
            else:
                try:
                    # this request comes from campaign_recipients.html
                    # "$("#button_another_candidate_or_organization").on("click",
                    # function() {"
                    candidate_another = json.loads(
                        request.POST.get("candidate_another"))

                    # print(candidate_another)
                    name = "radf"
                    pro_pic = "none"
                    data_letter = ""
                    pro_id = candidate_another  # when the Id name startwith digit then it was from db
                    # when the ID start with letter then it is the new assign name.Stored it in db and
                    # the imgae will be sample image and the position will be New
                    # candidate.
                    candidancy = "candidate_another"
                    data = {
                        'candidancy': candidancy,
                        'name': name,
                        'pro_pic': pro_pic,
                        'data_letters': data_letter,
                        'pro_id': pro_id,


                    }
                except:
                    pass
            # this request comes from candidate_info.html
            # "$("#recipients_save_button_myself_yes_no_click").on("click",
            # function() {"
            candidate_self_or_not = request.POST.get("yes_no")

            # this request comes from campaign_story.html "function
            # butonStorySave() {"
            try:
                story = jsonloads(request.POST["story"])
                # print(story)
                campaign_title = story['title']
                cover_pic = story['img']
                video_url = story['video_url']
                campaign_story = story['story']
                print(campaign_title)
            except Exception as e:
                pass

            # this request comes from campaign_recipients.html
            # "$("#removeProfile").on('click', function() {"
            deleteCampaingBYName = request.POST.get("deleteID")

            try:
                # this request comes from candidate_info.html
                # $("#recipients_save_button_yes_no_form_click").on("click",
                # function() {
                candidate_info = jsonloads(request.POST['values'])
                print(candidate_info)

            except Exception as e:
                # print("Exception", e)
                pass
            try:
                # this request comes from race_info.html
                # $("#save_custom_candidate").on('click',function()
                race_info = jsonloads(request.POST['race_info'])
                print(race_info)
            except Exception as e:
                # print("Exception", e)
                pass

            try:
                # this request comes from fundraising.html
                # function saveFundraising(){}
                fundraising = jsonloads(request.POST['fundraising'])
                # print(fundraising)
                Default_Donation = fundraising["Default_Donation"]
                Other_donation_amounts1 = fundraising[
                    "Other_donation_amounts1"]
                Other_donation_amounts2 = fundraising[
                    "Other_donation_amounts2"]
                Other_donation_amounts3 = fundraising[
                    "Other_donation_amounts3"]
            except Exception as e:
                # print("Exception", e)
                pass

            privacy_type = request.POST.get("privacy_type")
            print(privacy_type)

            # Which race is selected from default table, the id of this race
            # will store in selected race. The ajax call is generated in
            # race_info.html "$("#save_race_selected").on('click',function(){"

            selected_race = request.POST.get("race_selected")

            try:
                # this request comes from custom_sharing.html
                # function save_custom_sharing () {}
                custom_sharing = jsonloads(request.POST['custom_sharing'])
                print(custom_sharing)
            except Exception as e:
                # print("Exception", e)
                pass
            try:
                # this request comes from optional_settings.html
                # optionalSettingsSave() {}
                optional_settings = jsonloads(
                    request.POST['optional_settings'])
                # print(optional_settings)
            except Exception as e:
                # print("Exception", e)
                pass

            data = {
                'candidancy': candidancy,
                'name': name,
                'pro_pic': pro_pic,
                'data_letters': data_letter,
                'pro_id': pro_id,
                'candidate_self_or_not': candidate_self_or_not,
                'campaign_title': campaign_title,
                'optional_settings': optional_settings,
                'Default_Donation': Default_Donation,
                'Other_donation_amounts1': Other_donation_amounts1,
                'Other_donation_amounts2': Other_donation_amounts2,
                'Other_donation_amounts3': Other_donation_amounts3,
                'cover_pic': cover_pic,
                'video_url': video_url,
                'campaign_story': campaign_story,


            }
            publish = request.POST.get("publish_campaign")

            return JsonResponse({'context': data}, status=200)
        data = {
            'candidancy': candidancy,
            'name': name,
            'pro_pic': pro_pic,
            'data_letters': data_letter,
            'states_city': states_city,
            'race_list': race_list,
            'race_local': race_local,
            'video_url': video_url,

        }
        # print(data)
        return render(request, 'startcampaign.html', {'context': data, 'userList': userList})
    else:

        return render(request, 'startcampaignSignup.html')


def pricing_view(request):
    return render(request, 'Pricing.html')


def media_view(request):
    return render(request, 'media.html')


def privacy_policy_view(request):
    return render(request, 'privacy_policy.html')


def terms_view(request):
    return render(request, 'terms_of_service.html')


def jobs_view(request):
    return render(request, 'jobs.html')


def about_us_view(request):
    return render(request, 'about_us.html')


def my_campaigns_view(request):
    return render(request, 'my_campaigns.html')


def signin_view(request):
    return render(request, 'signin.html')


def remaind_view(request):
    return render(request, 'forgotpass.html')


def start_rally_view(request):
    global login
    if login == "true":
        pass
    else:
        return render(request, 'rallySignIn.html')


def notifications_view(request):
    return render(request, 'notifications.html')


def campaign_create_conditional_view(request):
    return render(request, 'campaigns_create_conditional.html')


def how_it_works_view(request):
    return render(request, 'learn.html')


def innovative_fundraising_view(request):
    return render(request, 'promote.html')


def members_view(request):
    data1 = {
        'member_name': 'xyz',
        "member_pro_pic": "none",
        'memberDataLetter': 'X',
        'memberId': 1
    }
    data2 = {
        'member_name': 'abc',
        "member_pro_pic": "none",
        'memberDataLetter': 'A',
        'memberId': 1
    }
    data3 = {
        'member_name': 'xyzz',
        "member_pro_pic": "none",
        'memberDataLetter': 'X',
        'memberId': 1
    }
    lstData = []
    lstData.append(data1)
    lstData.append(data2)
    lstData.append(data3)
    # return render(request, 'members.html', {'data': lstData})


def connection_view(request):
    return render(request, 'Connections.html')


def endorsements_view(request):
    return render(request, 'Endorsements.html')


@csrf_exempt
def start_petition_view(request):
    if request.is_ajax and request.method == "POST":
        try:
            # this request comes from startpetitions.html
            # optionalSettingsSave() {}
            petition = jsonloads(
                request.POST['start_petition'])
            print(petition)
            # print(optional_settings)
        except Exception as e:
            # print("Exception", e)
            pass
        return JsonResponse({'data': 'null'}, status=200)
    return render(request, 'startpetitions.html')


def my_contributions_view(request):
    return render(request, 'my_contributions.html')


def my_profile_view(request):
    return render(request, 'my_profile.html')


def my_settings_view(request):
    return render(request, 'setting.html')


def others_profile_view(request):
    data = {
        'pro_pic': 'none',
        'data_letters': 'N',
        'user_name': 'Name',
        'member_ago': 'Member since August 2020',
        'endorsed': 1,
        'contribution': 0,
    }
    return render(request, 'others_profile.html', {'data': data})


def support_view(request):
    return render(request, 'support.html')


def support_slug_view(request):
    return render(request, 'support_inner.html')

# import user data from auth model


def contain_user_data(request):
    #from yourapp.models import table
    #obj = table.objects.all()
    #global login
    data = {
        'login': "True",
        'pro_pic': 'none',
        'data_letters': 'R',
        'user_name': 'rakib',
        'member_ago': 'Member since August 2020',
        'endorsed': 1,
        'contribution': 0,

    }
    return {'contain_user_data': data, }

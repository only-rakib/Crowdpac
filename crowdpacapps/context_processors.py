def contain_user_data(request):
    #from yourapp.models import table
    #obj = table.objects.all()
    global login
    data = {
        'login': "True",
        'pro_pic': 'none',
        'data_letters': 'R',

    }
    return {'contain_user_data': data, }

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.generic import View

#from .models import Festival


# save data for web browser


save_data = []
dict1 = {}
dict2 = {}
dict3 = {}
empty_dict = {'title': '', 'start': '', 'finish': '', 'number': '', 'address': '', 'img': '', 'tag' : ''}

weather = {}


def post_list(request)   :
    return render(request, 'blog/post_list.html', {})


def httpres(request):
    return HttpResponse('OK')


def run(request):
    global dict1, dict2, dict3
    global weather

    data = request.GET

    # replace data
    outer_data = ''
    for d in data:
        outer_data = d

    tmp_data = outer_data.split(" //// ")

    tmp_data[2], weather_tmp = tmp_data[2].split(" /weather/ ")

    print(tmp_data)


    weather_data = weather_tmp.split(" ")

    weather['max_tem'] = weather_data[0]
    weather['min_tem'] = weather_data[1]
    weather['avg_rhm'] = weather_data[2]
    weather['sum_rn'] = weather_data[3]

    weather['str1'] = weather_data[4]
    weather['wat1'] = weather_data[5]
    weather['ban1'] = weather_data[6]
    weather['blu1'] = weather_data[7]

    print(weather_data)


    # split data
    replace_data_to_dict = []
    for tmp in tmp_data:

        replace_data_to_dict.append(tmp.replace("\'", "\""))

    # check list's length(festival number), and
    if len(replace_data_to_dict) == 3:

        d1, d2, d3 = replace_data_to_dict

        dict1 = json.loads(d1)
        dict2 = json.loads(d2)
        dict3 = json.loads(d3)

    elif len(replace_data_to_dict) == 2:

        d1, d2 = replace_data_to_dict
        dict1 = json.loads(d1)
        dict2 = json.loads(d2)

        # empty
        dict3 = empty_dict
    elif len(replace_data_to_dict) == 1:

        d1 = str(replace_data_to_dict)
        d1 = d1.replace('[\'', '').replace('\']', '')
        dict1 = json.loads(d1)

        dict2 = empty_dict
        dict3 = empty_dict
    else:
        dict1 = empty_dict
        dict2 = empty_dict
        dict3 = empty_dict

    return render(request, 'blog/post_list.html')


def Festivalget(request):
    global dict1, dict2, dict3
    global weather

    data = {
        'title1': dict1['title'],
        'address1': dict1['address'],
        'img1': dict1['img'] + '&thumb',
        'gu1' :  dict1['address'].split(' ')[0] + ' ' + dict1['address'].split(' ')[1],
        'tag1' : dict1['tag'],
        'clock1' : dict1['start'] + ' ~ ' + dict1['finish'],
        'number1' : dict1['number'],

        'title2': dict2['title'],
        'address2': dict2['address'],
        'img2': dict2['img'] + '&thumb',
        'gu2': dict2['address'].split(' ')[0] + ' ' + dict2['address'].split(' ')[1],
        'tag2': dict2['tag'],
        'clock2': dict2['start'] + ' ~ ' + dict2['finish'],
        'number2': dict2['number'],

        'title3': dict3['title'],
        'address3': dict3['address'],
        'img3': dict3['img'] + '&thumb',
        'gu3': dict3['address'].split(' ')[0] + ' ' + dict3['address'].split(' ')[1],
        'tag3': dict3['tag'],
        'clock3': dict3['start'] + ' ~ ' + dict3['finish'],
        'number3': dict3['number'],


        'max_tem' : weather['max_tem'],
        'min_tem' : weather['min_tem'],
        'avg_rhm' : weather['avg_rhm'],
        'sum_rn' : weather['sum_rn'],

        'str1' : weather['str1'],
        'wat1' : weather['wat1'],
        'ban1' : weather['ban1'],
        'blu1' : weather['blu1'],
    }

    return JsonResponse(data)

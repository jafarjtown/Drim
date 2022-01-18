from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
alpha = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm',
         'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', ' ', '/', '|', ':', ";", '>', '<', "." ,'\'','\\' ]


def Index(request):
    return render(request,'cipher/index.html')

def EncodeText(text, method):
    def downgrade(method):
        method = abs(int(method)) / 8 / 7 / 3 / 2
        if abs(int(method)) > 107:
            return downgrade(abs(method))
        return abs(method)
    if int(method) > 107:
        method = downgrade(method)
    indexs = []
    for t in text:
        indexs.append(alpha.index(t))
    if int(method) > len(alpha):
        m = int(method) - abs(len(alpha))
        am = abs(m)
        ts1 = alpha[am:]
        ts2 = alpha[:am]
        for t in ts2:
            ts1.append(t)
    elif int(method) < 10:
        m = int(method) + 26
        am = abs(m)
        ts1 = alpha[am:]
        ts2 = alpha[:am]
        for t in ts2:
            ts1.append(t)
    else:
        m = int(method)
        am = abs(m)
        ts1 = alpha[am:]
        ts2 = alpha[:am]
        for t in ts2:
            ts1.append(t)
    e = []
    for i in indexs:
        e.append(ts1[i])
    # text = open(file, 'w+')
    # text.write(''.join(e))
    return ''.join(e)


def DecodeText(text, method):
    def downgrade(method):
        method = abs(int(method)) / 8 / 7 / 3 / 2
        if abs(int(method)) > 107:
            return downgrade(abs(method))
        return abs(method)
    if int(method) > 107:
        method = downgrade(method)
    indexs = []
    if int(method) > len(alpha):
        m = int(method) - abs(len(alpha))
        am = abs(m)
        ts1 = alpha[:am]
        ts2 = alpha[am:]
        for t in ts2:
            ts1.append(t)
    elif int(method) < 10:
        m = int(method) + 26
        am = abs(m)
        ts1 = alpha[:am]
        ts2 = alpha[am:]
        for t in ts2:
            ts1.append(t)
    else:
        m = int(method)
        am = abs(m)
        ts1 = alpha[:am]
        ts2 = alpha[am:]
        for t in ts2:
            ts1.append(t)
    e = []
    for t in text:
        indexs.append(alpha.index(t) - am)
    for i in indexs:
        e.append(ts1[i])
    #     pass
    # text = open(file, 'w+')
    # text.write(''.join(e))
    # pass
    return ''.join(e)

import json
def encript(request):
    json_d = json.loads(request.body)
    text = json_d['text']
    key = json_d['key']
    t = EncodeText(text, key)
    return JsonResponse({
        'encripted': t,
        'key': key,
        'normal': text,
    })

def decript(request):
    json_d = json.loads(request.body)
    text = json_d['text']
    key = json_d['key']
    t = DecodeText(text, key)
    return JsonResponse({
        'decripted': t,
        'key': key,
        'normal': text
    })
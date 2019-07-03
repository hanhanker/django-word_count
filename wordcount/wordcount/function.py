# from django.http import HttpResponse
from django.shortcuts import HttpResponse, render, redirect

# def home(request):
#     return HttpResponse('hello')

def home(request):
    return render(request,'home.html')

def count(request):
    text = request.GET['text'].strip() # 去除前后空格
    total_count = len( text )
    word_dict = {}
    for word in text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    # items 将字典里面的键（key ）和值（value），变成了[键，值]，
    # 定义一个w[]的列表，取w[1]，就是列表里面的第二个数，也就是字典里面的 值
    sorted_dict = sorted(word_dict.items(), key = lambda  w:w[1], reverse = True) # 字典本身不可迭代，使用items()
    return render(request,'result.html', {
        'text': text,
        'total_count': total_count,
        'word_dict': word_dict,
        'sorted_dict': sorted_dict
    })

def about(request):
    return render(request,'about.html')



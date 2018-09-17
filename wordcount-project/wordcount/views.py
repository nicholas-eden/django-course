from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html', {'cat': 'Roro'})


def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    word_count = len(words)

    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    word_items = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': word_count, 'word_dict': word_items})

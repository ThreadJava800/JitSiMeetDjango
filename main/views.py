from django.shortcuts import render
import random
import string
import sqlite3 as sql

conference_link = str()
LINK_LENGTH = 15


def index(request):
    return render(request, 'index.html')


def create_page(request):
    global conference_link
    conference_link = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(LINK_LENGTH))
    data = {}
    data['link'] = conference_link
    return render(request, 'create_conference_page.html', data)


def watch_page(request):
    global conference_link
    print(conference_link)
    data = {}
    data['link'] = conference_link
    return render(request, 'watch.html', data)

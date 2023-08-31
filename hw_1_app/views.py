from django.shortcuts import render

from django.http import HttpResponse
def text(title, body ):
    return f'<h1>{title}</h1>' \
           f'<p> {body}</p>'

def index (request):
    title='Здравствуй дорогой друг,'
    body='добро пожаловать на мой Django сайт.'
    return HttpResponse (text(title,body))
def about (request):
    title = 'Если тебе интересно как меня зовут,'
    body = 'то меня зовут Виктор.'
    return HttpResponse (text(title,body))
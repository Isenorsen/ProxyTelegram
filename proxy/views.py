from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .serializers import *
from django.http import request
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.views.decorators.csrf import csrf_exempt


class ProxySerView(viewsets.ModelViewSet):
    """API endpoint that allows us to get and post new proxy"""
    queryset = Proxy.objects.all()
    serializer_class = ProxySerializer

def contact_form(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Заявка на прокси'
            period = form.cleaned_data['period']
            email = form.cleaned_data['email']
            nicknameForm = form.cleaned_data['nickname']
            message = 'Email: {} \nПериод: {} \nИмя канала: @{}'.format(email, period, nicknameForm)
            emailFrom = ['ak@arcanite.ru']
            emailTo = ['ak@arcanite.ru']
            try:
                send_mail(subject, message, emailFrom, emailTo)
                return HttpResponse('Ваше сообщение отправлено')
            except BadHeaderError:
                return HttpResponse('Invalid header')
        else:
            return HttpResponse('Ошибка отправки')
    return render(request, 'send.html', {'form': form})


def proxy_list(request):
    proxy = Proxy.objects.filter(active=True)
    context = {'proxy': proxy}
    return render(request, 'index.html', context)


def proxy_add(request):
    if request.method == "POST":
        form = AddingProxyForm(request.POST, request.FILES)
        if form.is_valid():
            form_item = form.save(commit=False)
            form_item.save()
            return HttpResponse('Item added')
        else:
         return HttpResponse('Oops, error...')
    else:
        form = AddingProxyForm()
    return render(request, 'add.html', {'form': form})
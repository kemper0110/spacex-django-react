# api/views.py
from datetime import datetime
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import MenuSerializer, BenefitSerializer
from .models import Menu, Benefit


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is {now}.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)


class BenefitViewSet(viewsets.ModelViewSet):
    queryset = Benefit.objects.all().order_by('id')
    serializer_class = BenefitSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all().order_by('id')
    serializer_class = MenuSerializer

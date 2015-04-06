from django.shortcuts import render
from django.http import HttpResponse

from .models import Category
from .models import Request
from .models import RequestAccept
from .models import Available

# views go here

def activeRequests(request):
    #all active requests in list format, boring i know
    active_request_list = Request.objects
    output = ', '.join([p.username for p in active_request_list])               # Anthony, reference by PK not username
    return HttpResponse(output)

def 

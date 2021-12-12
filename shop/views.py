from django.shortcuts import get_object_or_404, render
from . models import *
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def home(request,ct_slug=None):
    ct_page = None
    prodt = None

    if ct_slug!= None:
        ct_page = get_object_or_404(cat,slug = ct_slug)
        prodt = products.objects.filter(category=ct_page)

    else:
        prodt = products.objects.all().filter()

    ctg = cat.objects.all()
    return render(request,'home.html',{'prod':prodt,'ctg':ctg})


def search(request):
    prodt = None
    qry = None

    if 'qr' in request.GET:
        qry = request.GET.get('qr')
        prodt = products.objects.all().filter(Q(name__contains=qry))

    return render(request,'search.html',{'q':qry,'prod':prodt})

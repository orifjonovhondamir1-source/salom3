from django.shortcuts import render
from .models import TTM,Uzbek,Mahsulot, Salom
# Create your views here.

def index (request):
    ttm = TTM.objects.all()
    return render (request, "index.html ",  {"ttm": ttm})
def home (request):
    uzbek = Uzbek.objects.all()
    return render (request, "home.html ", {"uzbek": uzbek} )

def uzbek (request):
    mahsulot = Mahsulot.objects.all()
    return render (request, "uzbek.html ", {"mahsulot": mahsulot} )

def salom (request):
    return render (request, "salom.html " )

def nav (request):
    salom = Salom.objects.all()
    return render (request, "nav.html ", {"salom": salom} )
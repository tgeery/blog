from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Journal

def index(request):
    entries = Journal.objects.order_by('-date')
    return render(request, 'daily/index.html', {'entries':entries})

def entry_1(request):
    entry = Journal.objects.get(pk=1)
    return render(request, 'daily/entry_1.html', {'entry':entry})

def entry_2(request):
    entry = Journal.objects.get(pk=2)
    return render(request, 'daily/entry_2.html', {'entry':entry})

def entry_3(request):
    entry = Journal.objects.get(pk=3)
    return render(request, 'daily/entry_3.html', {'entry':entry})

def entry_4(request):
    entry = Journal.objects.get(pk=4)
    return render(request, 'daily/entry_4.html', {'entry':entry})

def entry_5(request):
    entry = Journal.objects.get(pk=5)
    return render(request, 'daily/entry_5.html', {'entry':entry})

def entry_6(request):
    entry = Journal.objects.get(pk=6)
    return render(request, 'daily/entry_6.html', {'entry':entry})

def entry_7(request):
    entry = Journal.objects.get(pk=7)
    return render(request, 'daily/entry_7.html', {'entry':entry})

def entry_8(request):
    entry = Journal.objects.get(pk=8)
    return render(request, 'daily/entry_8.html', {'entry':entry})

def entry_9(request):
    entry = Journal.objects.get(pk=9)
    return render(request, 'daily/entry_9.html', {'entry':entry})

def entry_10(request):
    entry = Journal.objects.get(pk=10)
    return render(request, 'daily/entry_10.html', {'entry':entry})

def entry_11(request):
    entry = Journal.objects.get(pk=11)
    return render(request, 'daily/entry_11.html', {'entry':entry})

def entry_12(request):
    entry = Journal.objects.get(pk=12)
    return render(request, 'daily/entry_12.html', {'entry':entry})

def entry_13(request):
    entry = Journal.objects.get(pk=13)
    return render(request, 'daily/entry_13.html', {'entry':entry})

def entry_14(request):
    entry = Journal.objects.get(pk=14)
    return render(request, 'daily/entry_14.html', {'entry':entry})

def entry_15(request):
    entry = Journal.objects.get(pk=15)
    return render(request, 'daily/entry_15.html', {'entry':entry})

def entry_16(request):
    entry = Journal.objects.get(pk=16)
    return render(request, 'daily/entry_16.html', {'entry':entry})

def entry_17(request):
    entry = Journal.objects.get(pk=17)
    return render(request, 'daily/entry_17.html', {'entry':entry})

def entry_18(request):
    entry = Journal.objects.get(pk=18)
    return render(request, 'daily/entry_18.html', {'entry':entry})

def entry_19(request):
    entry = Journal.objects.get(pk=19)
    return render(request, 'daily/entry_19.html', {'entry':entry})

def entry_20(request):
    entry = Journal.objects.get(pk=20)
    return render(request, 'daily/entry_20.html', {'entry':entry})

def entry_21(request):
    entry = Journal.objects.get(pk=21)
    return render(request, 'daily/entry_21.html', {'entry':entry})

def entry_22(request):
    entry = Journal.objects.get(pk=22)
    return render(request, 'daily/entry_22.html', {'entry':entry})

def entry_23(request):
    entry = Journal.objects.get(pk=23)
    return render(request, 'daily/entry_23.html', {'entry':entry})

def entry_24(request):
    entry = Journal.objects.get(pk=24)
    return render(request, 'daily/entry_24.html', {'entry':entry})

def entry_25(request):
    entry = Journal.objects.get(pk=25)
    return render(request, 'daily/entry_25.html', {'entry':entry})

def entry_26(request):
    entry = Journal.objects.get(pk=26)
    return render(request, 'daily/entry_26.html', {'entry':entry})

def entry_27(request):
    entry = Journal.objects.get(pk=27)
    return render(request, 'daily/entry_27.html', {'entry':entry})

def entry_28(request):
    entry = Journal.objects.get(pk=28)
    return render(request, 'daily/entry_28.html', {'entry':entry})

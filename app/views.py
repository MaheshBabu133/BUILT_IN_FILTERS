from django.shortcuts import render

# Create your views here.
def in_buit_filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'var':'hii GUys TheIS is ThE HarsHaD sir ClASs','c':'10','dt':dt}
    return render(request,'in_buit_filters.html',d)
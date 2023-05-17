from django.shortcuts import render
from .models import food

def home(request):
    if request.get_host() == 'indofa.herokuapp.com' or request.get_host() == 'www.indofa.herokuapp.com':
        return redirect('https://www.indofa.store')
    if request.get_host() == 'indofa.store' or request.get_host() == 'indofa.store':
        return redirect('https://www.indofa.store')
    else:
        plant = food.objects.filter(type__in=['HẠT GIỐNG HOA','HẠT GIỐNG RAU'], active=True)[:4]
        pot = food.objects.filter(type__in=['CHẬU GỐM', 'CHẬU NHỰA', 'CHẬU TREO'], active=True)[:4]
        other = food.objects.filter(type__in=['ĐẤT / GIÁ THỂ TRỒNG'], active=True)[:4]
        context = {"plant": plant, "pot": pot, "other": other}
        return render(request, "home.html", context)
def chinhsach(request):
    return render(request, 'chinhsach.html')
def blog(request):
    return render(request, "blog.html")
def speblog(request):
    return render(request, "blogspe.html")
def speblog2(request):
    return render(request, "blogspe2.html")
def speblog3(request): # bùa thầy Nghĩa
    return render(request, "blogspe3.html")
def tuyendung(request):
    return render(request,"tuyendung.html")
def aboutus(request):
    return render(request, "aboutus.html")
from django.shortcuts import redirect

def handle_404(request, exception):
    return redirect('home')
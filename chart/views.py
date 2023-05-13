from django.http import JsonResponse
from django.shortcuts import render, redirect
from calc.models import order
from django.db.models.functions import TruncMonth
from django.db.models import Sum

# Create your views here.
def home(request):
    if request.user.is_superuser:
        return render(request, 'chart.html')
    else:
        return redirect('/')
def chart(request):
    total_revenue_month = order.objects.annotate(month=TruncMonth("time")).values('month').annotate(total_revenue=Sum('total_price')).order_by('month')
    label = []
    data = []
    for i in total_revenue_month:
        label.append(i['month'].strftime('%B'))
        data.append(i['total_revenue'])
    data = {'label': label, 'data': data}
    return JsonResponse(data)
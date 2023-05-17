from django.shortcuts import render, redirect
from calc.models import food, order,OrderLine, CanvasImage
from django.contrib.auth.models import User
from django.contrib import messages
import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from register.models import customer
from django.contrib import messages
from django.core import mail
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from mysite import settings
from calc.models import food, order,OrderLine
EMAIL_ACCOUNT = settings.EMAIL_HOST_USER
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.html import strip_tags
def delete_order(request, id):
    if request.user.is_authenticated:
        if request.user.username == OrderLine.objects.get(id=id).username:
            OrderLine.objects.get(id=id).delete()
            return redirect('/order/cart')
        else:
            return redirect('/order/cart')
    else:
        return redirect("/register/login")
def dynamic_lookup_view(request, id):
    obj = food.objects.get(id = id)
    context = {
        "object": obj
}
    # try:
    if request.method == "POST":
        try:
            if request.user.is_authenticated:
                username1 = request.user.username
            else:
                redirect('/account/login')
            foods = obj.id
            name = obj.name
            price= obj.price
            url = obj.image
            quantity = request.POST['totalAmount']
            if int(quantity) == 0:
                messages.success(request, 'Tổng số lượng sản phẩm không thể là 0')
                return render(request, "specificproduct.html", context)         
            orders = OrderLine(username = username1,food=foods, quantity=quantity, name=name, price=price, image=url)
            orders.save()
            return redirect('/order/cart')
        except:
            return render(request, "specificproduct.html", context)
    else:
        return render(request, "specificproduct.html", context)
    # except:
    #     context["error"] = "Wrong data filled!"
    #     return render(request, "specificproduct.html", context)
def get_user_order(request):
    if request.user.is_authenticated:
        username1 = User.objects.get(username = request.user)
        orders = order.objects.filter(username = username1)
        context = {
            "name": username1,
            "orders": orders
        }
        return render(request, "check_order.html", context)
    else:
        return redirect('/register/login')
def pot_order(request):
    orders = food.objects.filter(type__in=['CHẬU GỐM', 'CHẬU NHỰA', 'CHẬU TREO'], active=True)
    title = "CHẬU CÂY"
    context = {"orders": orders, "title": title}
    return render(request, "order_list.html", context)
def gompot_order(request):
    orders = food.objects.filter(type__in=['CHẬU GỐM'], active=True)
    title = "CHẬU CÂY / CHẬU GỐM"
    context = {"orders": orders, "title": title}
    return render(request, "order_list.html", context)
def plapot_order(request):
    orders = food.objects.filter(type__in=['CHẬU NHỰA'], active=True)
    title = "CHẬU CÂY / CHẬU NHỰA"
    context = {"orders": orders, "title": title}
    return render(request, "order_list.html", context)
def hangpot_order(request):
    orders = food.objects.filter(type__in=['CHẬU TREO'], active=True)
    title = "CHẬU CÂY / CHẬU TREO"
    context = {"orders": orders, "title": title}
    return render(request, "order_list.html", context)
def other_order(request):
    orders = food.objects.filter(type__in=['DỤNG CỤ KHÁC'], active=True)
    title = "CHẬU CÂY / DỤNG CỤ KHÁC"
    context = {"orders": orders, "title": title}
    return render(request, "order_list.html", context)
def plant_order(request):
    orders = food.objects.filter(type__in=['HẠT GIỐNG HOA','HẠT GIỐNG RAU'], active=True)
    title = "HẠT GIỐNG"
    context = {"orders": orders, "title": title}
    return render(request, "order_list.html", context)
def flower_order(request):
    orders = food.objects.filter(type__in=['HẠT GIỐNG HOA'], active=True)
    title = "HẠT GIỐNG / HẠT GIỐNG HOA"
    context = {"orders": orders, "title": title}
    return render(request, "order_list.html", context)
def cuqua_order(request):
    orders = food.objects.filter(type__in=['HẠT GIỐNG CỦ QUẢ'], active=True)
    title = "HẠT GIỐNG / HẠT GIỐNG CỦ QUẢ"
    context = {"orders": orders, "title": title}
    return render(request, "order_list.html", context)
def veg_order(request):
    orders = food.objects.filter(type__in=['HẠT GIỐNG RAU'], active=True)
    title = "HẠT GIỐNG / HẠT GIỐNG RAU"
    context = {"orders": orders, "title": title}
    return render(request, "order_list.html", context)
def soil_order(request):
    orders = food.objects.filter(type__in=['ĐẤT / GIÁ THỂ TRỒNG'], active=True)
    title = "ĐẤT / GIÁ THỂ TRỒNG"
    context = {"orders": orders, "title": title}
    return render(request, "order_list.html", context)
def decor(request):
    orders = food.objects.filter(type__in=['TRANG TRÍ CHẬU CÂY'], active=True)
    title = "TRANG TRÍ CHẬU CÂY"
    context = {"orders": orders, "title": title}
    return render(request, "order_list.html", context)
def filter(request):
    orders = food.objects.filter(type__in=['TRANG TRÍ CHẬU CÂY'], active=True)
    title = "TRANG TRÍ CHẬU CÂY"
    context = {"orders": orders, "title": title}
    return render(request, "order_list.html", context)
def customize(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES.get('image'):
            username = request.user.username
            canvas_image = CanvasImage(image=request.FILES['image'], username=username)
            canvas_image.save()
            orders = OrderLine(username = username,food=99999, quantity=1, name="Chậu custom", price=30, image=request.FILES['image'])
            orders.save()
            return render(request, "customize.html")
        else:
            return render(request, "customize.html")
    else:
        return render(request, "customize.html")
def checkout(request):
    orders = OrderLine.objects.filter(username=request.user.username,status = False)
    context = {'orders': orders}
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                orders = OrderLine.objects.filter(username=request.user.username, status = False)
                if request.user.is_authenticated:
                    pass
                else:
                    redirect('/account/login')
                for order in orders.all():
                    order.quantity = request.POST['totalAmount{}'.format(order.id)]
                    order.save()
                return redirect('/order/checkout')
            except:
                return render(request, "orderinfo.html", context)
        return render(request, "orderinfo.html", context)
    else:
        return redirect("/register/login")
def saveorder(request):
    orders = OrderLine.objects.filter(username=request.user.username, status = False)
    
    context = {'orders': orders}
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                orders = OrderLine.objects.filter(username=request.user.username, status = False)
                username = request.user.username
                address = request.POST['address']
                province = request.POST['province']
                ward = request.POST['ward']
                commune = request.POST['commune']
                phone = request.POST['phone']
                total_price = 0
                for order1 in orders.all():
                    total_price += order1.price*order1.quantity
                    order1.status = True
                time = datetime.datetime.now()
                try:
                    CK_status = request.POST['checkbox']
                except:
                    CK_status =""
                if CK_status == "CK":
                    CK = True
                else:
                    CK = False
                if CK == True:
                    type_thanhtoan = "Chuyển khoản"
                else:
                    type_thanhtoan = "COD"
                status = "Đang xử lý"
                ordermain = order(username=username,address=address,province=province,ward=ward,commune=commune,phone=phone,time=time,CK=CK,status=status,total_price=total_price)
                ordermain.save()
                for order1 in orders.all():
                    order1.orderid = ordermain.id
                    order1.save()
                email_subject = "[INDOFA - XÁC NHẬN ĐƠN HÀNG ĐÃ ĐƯỢC ĐẶT]"
                message2 = render_to_string('templatemailsuccess.html', {
                            'name': request.user.last_name,
                            'city': province,
                            'ward': ward,
                            'commune': commune,
                            'CK': type_thanhtoan,
                            'total_amount': total_price
                        })
                plain_message = strip_tags(message2)
                email = mail.send_mail(
                            email_subject,
                            plain_message,
                            EMAIL_ACCOUNT,
                            [request.user.email],
                            html_message=message2
                        )
                return redirect('/order/ordersuccess')
            except:
                return render(request, "orderinfo.html")
        return render(request, "orderinfo.html", context)
    else:
        return redirect("/register/login")
def successfulorder(request):
    return render(request,"ordersuccess.html")
def cart(request):
    orders = OrderLine.objects.filter(username=request.user.username, status= False)
    context = {'orders': orders}
    if request.method == "POST":
        orders = OrderLine.objects.filter(username=request.user.username,status = False)
        if request.user.is_authenticated:
            username1 = request.user.username
        else:
            redirect('/account/login')
        for order in orders.all():
            print(order.id)
        return redirect('/order/checkout')
    if request.user.is_authenticated:
        return render(request, "cart.html", context)
    else:
        return redirect("/register/login")
def returnhome(request):
    return redirect("/")

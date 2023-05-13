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
from django.utils.html import strip_tags

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            text_type(user.pk) + text_type(timestamp)
        )


generate_token = TokenGenerator()

def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect'})
    else:
        return render(request, 'login.html')
def register(request):
    if request.method == "POST":
        # try:
            first = request.POST['first']
            last = request.POST['last']
            email = request.POST['email']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                if customer.objects.filter(username=username).exists():
                    return render(request, 'register.html', {'error': 'Tài khoản đã tồn tại'})
                if customer.objects.filter(email = email).exists():
                    return render(request, 'register.html', {'error': 'Email đã tồn tại'})
                else:
                    user = customer.objects.create_user(username=username, password=password1, email=email, first_name=first, last_name=last)
                    user.save()
                    user = auth.authenticate(username=username, password=password1)
                    auth.login(request, user)
                    messages.info(request, 'Your account has been created successfully!')
                    current_site = get_current_site(request)
                    email_subject = "[INDOFA - XÁC NHẬN TÀI KHOẢN]"
                    message2 = render_to_string('email_confirmation.html', {
                        'name': user.first_name,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': generate_token.make_token(user),
                    })
                    plain_message = strip_tags(message2)
                    email = mail.send_mail(
                        email_subject,
                        plain_message,
                        EMAIL_ACCOUNT,
                        [user.email],
                        html_message=message2
                    )
                    # email.fail_silently = True
                    # email.send()
                    return redirect('/')
            else:
                return render(request, 'register.html', {'error': 'Password does not match!'})
        # except:
        #     return render(request, 'register.html', {'error': 'Please fill all the fields!'})
    return render(request, 'register.html')



def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = customer.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, customer.DoesNotExist):
        myuser = None
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        return redirect('login')
    else:
        return render(request, 'activation_failed.html')
def account(request):
    obj = order.objects.filter(username=request.user.username)
    context = {"orders": obj}
    if request.user.is_authenticated:
        return render(request, "account.html", context)
    else:
        return redirect('/register/login')
def returnhome(request):
    return redirect("/")

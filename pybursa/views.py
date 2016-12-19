from django.http import HttpResponse, response, HttpResponseRedirect
from django.shortcuts import render
from courses.models import Course
from django.contrib import auth

def index(request):
    courses = Course.objects.all()
    return render(request, "index.html", {'courses': courses})
    # if request.user.is_authenticated():
    #     return render(request, "index.html", {'courses': courses})
    # else:
    #     return render(request, "index.html" )

def contact(request):
    return render(request, "contact.html")

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         if user is not None and user.is_active:
#             # Правильный пароль и пользователь "активен"
#             auth.login(request, user)
#             # Перенаправление на "правильную" страницу
#             return HttpResponseRedirect("/account/loggedin/")
#         else:
#             # Отображение страницы с ошибкой
#             return HttpResponseRedirect("/account/invalid/")
#     else:
#         return render(request, 'login.html')
#
# def logout(request):
#     pass

# def student_list(request):
#     return render(request, "student_list.html")
#
# def student_detail(request):
#     return render(request, "student_detail.html")
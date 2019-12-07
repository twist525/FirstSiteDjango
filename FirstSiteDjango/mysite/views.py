from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *


# получаем ответы к вопросу
def f2(v):
    a = Answer.objects.filter(question__question_text=v)
    return a


# получаем вопрос в анкете
def f1(i):
    q_dict = []
    a_list = Questionnaire.objects.all()
    for a in a_list:
        q_list = Question.objects.filter(questionnaire__questionnaire=a)
        q_dict.extend(q_list)
    return q_dict[i]


# получаем анкету
def f0(i):
    a_list = Questionnaire.objects.all()
    return a_list[i]


def home_detail(request):
    a = 0 #номер анкеты из списка всех анкет
    n = 0 #номер вопроса

    # тут проверки на все 
    if request.POST:
        # в POST есть параметр инпута который был отмечен
        print(request.POST)
        n = n + 1 #номер следующего вопроса

    anketa = f0(a) #получаем анкету
    question = f1(n) #получаем вопрос 
    answers = f2(question) #получаем ответы к вопросу 

    # передаем в контекс словарь 
    context = {'ankete': anketa, 'question': question, 'answers': answers}
    return render(request, 'index.html', context=context)


# создать юзера в бд
def creat_user(request):
    if request.POST:
        try:
            d = dict(request.POST)
            print(d)
            login = d['login'][0]
            email = d['email'][0]
            password = d['password'][0]
            user = User.objects.create_user(login, email, password)
            user.save()
            print('пользователь сохранён')
        except:
            print('Неудачно')
        return render(request,'index.html')
    return render(request,'register.html')


# автоизация пользователя на сайте и првязка к сессии
def auth_user(request):
    if request.POST:
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user.is_active:
            login(request, user)
        context = {}
        return redirect('/', context = context)
    else:
        return render(request,'login.html')


# выход пользователя 
def logout_user(request):
    logout(request)
    return redirect('/')

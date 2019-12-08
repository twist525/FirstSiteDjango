from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *


t_dict = {} #список баллов
a_list = []
a = 0 #номер анкеты из списка всех анкет
n = 0 #номер вопроса

# плюсуем тип ответа анкеты
def f4(t):
    for key in a_list:
        if str(key) == str(t):
            print(str(key.type_result))
            print(t_dict)
            for item in t_dict:
                if item == str(key.type_result):
                    t_dict[item] = t_dict[item] + 1

def f3(a):
    if len(t_dict) >= 0:
        at_list = TypeResult.objects.filter(questionnaire__questionnaire = a)
        for key in at_list:
            t_dict[str(key)] = 0
    else:
        return

# получаем ответы к вопросу
def f2(v):
    a = Answer.objects.filter(question__question_text = v)
    return a

# получаем вопрос в анкете
def f1(i):
    q_dict = []
    a_list = Questionnaire.objects.all()
    for a in a_list:
        q_list = Question.objects.filter(questionnaire__questionnaire = a)
        q_dict.extend(q_list)
    return q_dict[i]

# получаем анкету
def f0(i):
    a_list = Questionnaire.objects.all()
    return a_list[i]


def home_detail(request):
    global n
    global a_list
    count = len(Question.objects.filter(questionnaire__questionnaire = f0(a))) #количество вопросов

    if request.POST: n = n + 1 #номер следующего вопроса         
    anketa = f0(a) #получаем анкету
    if n == 0: f3(anketa) #заполняем t_dict типами результата
    if n == count: n = 0 # если последний вопрос то 
    question = f1(n) #получаем вопрос
    answers = f2(question) #получаем ответы к вопросу
    if request.POST:
        d = dict(request.POST)
        del d['csrfmiddlewaretoken']
        for key in d:
            f4(d[key][0])
    a_list = answers 
    # передаем в контекс словарь 
    if n <= count - 1: 
        context = {'ankete': anketa, 'question':question, 'answers':answers, 'd':t_dict, 'n': n + 1}
    else:
        context = {'d':t_dict}
        
    return render(request, 'index.html', context = context)



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
            print('птица обламинго(((')
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

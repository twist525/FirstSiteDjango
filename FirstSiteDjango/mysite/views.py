from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Questionnaire, Question, Answer

n = 0


def polls_detail(request, path):
    global n
    data = {}
    current_poll = Questionnaire.objects.get(id=path)  # Получить ссылку на опрос выбранный пользователем
    current_questions_list = Question.objects.filter(questionnaire__questionnaire=current_poll)  # <QuerySet>

    if request.POST:
        for answer in Answer.objects.filter(question__question_text=current_questions_list[n]):
            if answer.answer_text == request.POST['otvet']:
                try:
                    data[answer.type_result] += 1
                except KeyError:
                    data[answer.type_result] = 1
        n += 1

    if n >= len(current_questions_list):
        n = 0
        current_result_test = None
        for finish_result_poll in data:
            if data[finish_result_poll]:
                current_result_test = finish_result_poll
        print(request.user.username, '+++++')
        print(data, '-----')
        user = User.objects.c
        data.clear()
        return render(request, 'polls.html', context={'result_test_text': 'Поздравляем, вы успешно прошли тест!',
                                                      'current_result_test': current_result_test}
                      )
    answer_options = Answer.objects.filter(question__question_text=current_questions_list[n])
    return render(request, 'polls.html',
                  context={
                      'current_question': current_questions_list[n],  # Вы мужчина? - Вопрос
                      'answer_options': answer_options,               # <QuerySet [<Answer: Да>, <Answer: Нет>
                      'number_of_question': n+1,                      # 2 - номер вопроса, +1 что бы не было Вопр: 0
                      'current_polls': current_poll}                  # Мы мужчина или женщина? - тип теста
                  )


def home_detail(request):
    polls_all_list = Questionnaire.objects.all()                      # Выбрать все существующие тесты(опросы)
    return render(request, 'index.html', context={'list_of_polls': polls_all_list})


# создать юзера в бд
def create_user(request):
    if request.POST:
        login = request.POST['login'][0]
        email = request.POST['email'][0]
        password = request.POST['password'][0]
        user = User.objects.create_user(login, email, password)
        user.save()
        return render(request, 'index.html')
    return render(request, 'register.html')


# автоизация пользователя на сайте и првязка к сессии
def auth_user(request):
    if not request.POST:
        return render(request, 'login.html')
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user.is_active:
        login(request, user)
    context = {}
    return redirect('/', context=context)


# выход пользователя 
def logout_user(request):
    logout(request)
    return redirect('/')

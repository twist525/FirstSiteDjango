from django.db import models
from django.contrib.auth.models import User


# Название теста
class Questionnaire(models.Model):
    questionnaire = models.CharField(max_length=200)

    def __str__(self):
        return self.questionnaire


# Вариация результата
class TypeResult(models.Model):
    type_result = models.CharField(max_length=200)
    questionnaire = models.ForeignKey(Questionnaire, related_name='type_result', on_delete=models.CASCADE)

    def __str__(self):
        return self.type_result


# Вопросы для теста
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    questionnaire = models.ForeignKey(Questionnaire, related_name='quest', on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


# Ответы на вопросы из модели Question
class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    type_result = models.ForeignKey(TypeResult, related_name='answer_type', on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text



from django.db import models


# Название анкеты
class Questionnaire(models.Model):
    questionnaire = models.CharField(max_length=200)

    def __str__(self):
        return self.questionnaire


# варианты результата
class TypeResult(models.Model):
    tupe_result = models.CharField(max_length=200)
    questionnaire = models.ForeignKey(Questionnaire, related_name='type_result', on_delete=models.CASCADE)

    def __str__(self):
        return self.tupe_result


# вопросы для анкеты
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    questionnaire = models.ForeignKey(Questionnaire, related_name='quest', on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


# ответы на вопросы
class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
#    answer_value = models.CharField(max_length=200)
#    answer_sum = models.IntegerField(default=0)
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
#    type_result = models.ForeignKey(TypeResult, default=None, related_name='tupe_result', on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text



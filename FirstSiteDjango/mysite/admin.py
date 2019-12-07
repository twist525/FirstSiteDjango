from django.contrib import admin
from .models import Questionnaire, TypeResult, Question, Answer

# admin.site.register(Questionnaire)
# admin.site.register(TypeResult)
# admin.site.register(Question)
# admin.site.register(Answer)


class TypeResultInline(admin.StackedInline):
    model = TypeResult
    extra = 0


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0


class QuestionnaireAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['questionnaire']}),
    ]
    inlines = [QuestionInline]

    list_display = ('questionnaire',)


admin.site.register(Questionnaire, QuestionnaireAdmin, )
admin.site.register(Answer)
admin.site.register(TypeResult)
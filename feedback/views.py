from django.shortcuts import render
from .forms import FeedbackForm
from .models import Feedback

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Создание нового объекта Feedback из данных формы
            feedback = Feedback(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                reason=form.cleaned_data['reason'],
                instagram=form.cleaned_data['instagram'],
                message=form.cleaned_data['message']
            )
            # Сохранение объекта в базу данных
            feedback.save()
            # Отправка электронной почты
            # ...
            return render(request, 'feedback.html', {'success': True})
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

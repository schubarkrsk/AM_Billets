from django import forms

# Определяем список вариантов для выпадающего списка
REASON_CHOICES = [
    ('option1', 'Биллет за 1р'),
    ('option2', 'Биллет за 5000р'),
    ('option3', 'Биллет за 1 млн руб'),
]

class FeedbackForm(forms.Form):
    name = forms.CharField(label='ФИО', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label="Телефон", max_length=50)
    reason = forms.ChoiceField(label='Тип биллета', choices=REASON_CHOICES)
    vk = forms.URLField(label="Ссылка на ВК")
    message = forms.CharField(label='Message', widget=forms.Textarea)

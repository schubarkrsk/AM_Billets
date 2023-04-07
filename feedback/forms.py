from django import forms

# Определяем список вариантов для выпадающего списка
REASON_CHOICES = [
    ('Classic', 'Classic для одного человека 1.000 рублей'),
    ('Gold', 'Gold для 4 человек 5.000 рублей + стол'),
    ('Platinum', 'Platinum для 8 человек 15.000 рублей + стол + 5.000 рублей депозита на стол'),
    ('Infinite', 'Infinite для одного человека 15.000 рублей (обслуживание без очереди,безлимитный бар на всю ночь')
]
# Classic для одного человека 1.000 рублей
# Gold для 4 человек 5.000рублей + стол
# Platinum для 8 человек 15.000 + стол + 5.000 рублей депозита на стол.
# Infinite для одного 15.000 (обслуживание без очереди,безлимитный бар на всю ночь)

class FeedbackForm(forms.Form):
    name = forms.CharField(label='ФИО', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label="Телефон", max_length=50)
    reason = forms.ChoiceField(label='Тип биллета', choices=REASON_CHOICES)
    instagram = forms.URLField(label="Ссылка на instagram")
    message = forms.CharField(label='Message', widget=forms.Textarea)

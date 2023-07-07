from django import forms

from .models import News


class NewsSearchForm(forms.Form):
    q = forms.CharField(label='Search')


class NewsForm(forms.ModelForm):
    TYPE_CHOICES = [
        ('Story', 'Story'),
        ('Job', 'Job'),
        ('Poll', 'Poll'),
    ]

    news_type = forms.ChoiceField(choices=TYPE_CHOICES)
    class Meta:
        model = News
        fields = ['title', 'text', 'news_type']
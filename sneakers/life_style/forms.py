from django import forms
from .models import *


class AddFeedbackForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(self, *args, **kwargs)
    #     self.fields["sneaker"].empty_label='Кроссовки не выбраны'

    class Meta:
        model = Feedback
        fields = ["sneaker", "feedback"]

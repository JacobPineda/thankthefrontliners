from django import forms
from django.utils.safestring import mark_safe

class MessageForm(forms.Form):

  COLOR_CHOICES = [
    ("BL", mark_safe("<div id='blue-btn' class='color-btn BL'></div>")),
    ("RE", mark_safe("<div class='color-btn RE'></div>")),
    ("YE", mark_safe("<div class='color-btn YE'></div>")),
    ("WH", mark_safe("<div class='color-btn WH btn-outline-secondary'></div>"))
  ]

  content = forms.CharField(label="Leave a thank you message for our frontliners", label_suffix="", max_length=300, required=True, widget=forms.Textarea(attrs= {'class': 'form-text', 'rows': 5, 'cols': 50}))
  name = forms.CharField(label="Name", label_suffix="", max_length=25, required=False, widget=forms.TextInput(attrs= {'class': 'form-text'}))
  color = forms.ChoiceField(choices=COLOR_CHOICES, label="", required=False, widget=forms.RadioSelect(attrs= {'class': 'color-container form-check-inline form-text'}))
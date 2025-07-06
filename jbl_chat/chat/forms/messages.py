from django import forms
from chat.models import Message


class MessageCreateForm(forms.ModelForm):
    receiver = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Message
        fields = ['content', 'receiver']
        widgets = {
            "content": forms.Textarea(attrs={'rows': 1, 'class': 'resize-none autoresize'}),
        }
from django import forms

class NewTweetForm(forms.Form):
    tweet = forms.CharField(widget=forms.Textarea)
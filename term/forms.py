from django import forms
class levelone(forms.Form):
    Word = forms.CharField(max_length=10)
    class Meta:
        fields = [
            'Word',
        ]
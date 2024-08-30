from django import forms
from .models import Post
from .models import Review


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'review']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


# class TourForm(forms.ModelForm):
#     class Meta:
#         model = Tour
#         fields = ['title', 'description', 'images']  # Dodaj inne pola według potrzeb
#         widgets = {
#             'images': forms.ClearableFileInput(attrs={'multiple': True}),
#         }

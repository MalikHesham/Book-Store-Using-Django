from django import forms
from .models import Book
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ("metrics","tag")

        widgets = {
            'title' : forms.TextInput(
            attrs = 
            {   'class':'form-control',
                'placeholder':' --- Book Title --- '
            }),
            'description' : forms.Textarea(attrs={'class' : 'form-control'}),
            'author' : forms.Select(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data.get("select")
        if "select" in title:
            raise ValidationError("title shouldn't have the select word!")
        return title


    def clean(self):
        super(BookForm, self).clean()
        category = self.cleaned_data.get('category')
        title = self.cleaned_data.get('title')
        
        if len(title) < 10 or len(title) > 50:
            raise ValidationError("title must be between 10 and 50 characters")

        return self.cleaned_data

    
    

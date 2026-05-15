from django import forms
from .models import Student,Student2,Address2
from .models import Club

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']




class Student2Form(forms.ModelForm):

    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']


    addresses = forms.ModelMultipleChoiceField(

        queryset=Address2.objects.all(),

        widget=forms.CheckboxSelectMultiple()

    )


class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'description', 'image']
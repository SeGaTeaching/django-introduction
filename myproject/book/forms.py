from django import forms

class BookForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Book Title'})
    )
    author = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Author Name'})
    )
    genre = forms.ChoiceField(
        choices=[
            ('fiction', 'Fiction'),
            ('nonfiction', 'Non-Fiction')
        ],
        widget=forms.RadioSelect
    )
    published_date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1900, 2024))
    )
    page_number = forms.IntegerField(
        min_value=1,
        max_value=5000
    )
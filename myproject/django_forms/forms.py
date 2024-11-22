from django import forms

class PizzaOrderForm(forms.Form):
    name = forms.CharField(
        #label='Name of User',
        max_length=100,
        widget=forms.TextInput()
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'john.doe@ex.com'})
    )
    size = forms.ChoiceField(
        choices=[
            ('small', 'Small'),
            ('medium', 'Medium'),
            ('large', 'Large')
        ],
        widget=forms.RadioSelect
    )
    date = forms.DateField(
        widget=forms.SelectDateWidget()
    )
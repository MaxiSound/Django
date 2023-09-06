from django import forms


class ClientForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', }))
    address = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', }))


class ProductForm(forms.Form):
    title = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    amount = forms.IntegerField()
    description = forms.CharField()
    image = forms.ImageField()

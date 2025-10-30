from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

        widgets = {
            'model': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Modelo do carro'}),
            'brand': forms.Select(attrs={'class': 'form-input'}),
            'factory_year': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Ano de fabricação'}),
            'model_year': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Ano do modelo'}),
            'plate': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Placa do veículo'}),
            'price': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Preço do carro'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-input'}),
        }

    def clean_price(self):
        price =self.cleaned_data.get('price')
        if price < 20000:
            self.add_error('price', 'Valor mínimo do carro deve ser de R$20.000')
        return price

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year is not None:
            if factory_year < 1975:
                self.add_error('factory_year', 'Ano de fabricação inválido.')
        return factory_year
    
    
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')

        # se for uma criação (objeto novo)
        if not self.instance:
            # foto é obrigatória
            if not photo:
                self.add_error('photo', 'A foto do carro é obrigatória.')
        return photo

        # Se for uma atualização (objeto já existe)
        # e o campo veio vazio, não faz nada (mantém a foto anterior ou None)

        if not photo:
            return self.instance.photo
        
        return photo
    
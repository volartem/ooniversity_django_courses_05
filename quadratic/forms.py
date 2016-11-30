from django import forms

class QuadraticForm(forms.Form):
    a = forms.CharField(max_length=15)
    b = forms.CharField(max_length=15)
    c = forms.CharField(max_length=15)

    def clean_a(self):
        try:
            data = int(self.cleaned_data['a'])
            if data == 0:
                raise forms.ValidationError('коэффициент при первом слагаемом уравнения не может быть равным нулю')
        except ValueError:
            raise forms.ValidationError('This field is required')
        return data

    def clean_b(self):
        try:
            return int(self.cleaned_data['b'])
        except ValueError:
            raise forms.ValidationError('This field is required')

    def clean_c(self):
        try:
            return int(self.cleaned_data['c'])
        except ValueError:
            raise forms.ValidationError('This field is required')

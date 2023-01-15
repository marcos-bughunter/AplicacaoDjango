from django import forms 

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Ex. Joao Silva'
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder' : 'Digite a sua senha'
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome de cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Ex. Joao Silva'
            }
        )
    )

    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Ex. joao@XPTO.com'
            }
        )
    )

    senha1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder' : 'Digite a sua senha'
            }
        )
    )

    senha2 = forms.CharField(
        label='Confirme sua senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder' : 'Digite a sua senha novamente'
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não foi possível inserir espaços dentro do campo Nome de Cadastro")
            else:
                return nome 

    def clean_senha2(self):
        senha1 = self.cleaned_data.get("senha1")
        senha2 = self.cleaned_data.get("senha2")

        if senha1 and senha2:
            if senha1 != senha2:
                raise forms.ValidationError('As senhas são diferentes!')
            else:
                return senha2

       

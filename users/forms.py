from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Team


class UserRegisterForm(ModelForm):
    game = forms.ChoiceField(choices=[('Rocket League', 'Rocket League'), ('CS:GO', 'CS:GO'), ('R6 Siege', 'R6 Siege'), ('Call Of Duty', 'Call Of Duty'), ('Apex Legends', 'Apex Legends'), ('Overwatch', 'Overwatch'), ('Smash Bros', 'Smash Bros'), ('Mortal Combat', 'Mortal Combat'), ('iRacing', 'iRacing')])
    ingame_name = forms.CharField(max_length=100)
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    discordtag = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    region = forms.ChoiceField(choices=[('NA', 'NA'), ('EU', 'EU'), ('OCE', 'OCE'), ('SAM', 'SAM')])
    email = forms.EmailField()
    shirt_size = forms.ChoiceField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')])
    team = forms.ModelChoiceField(queryset=Team.objects.all())
    birthday = forms.DateField()

    class Meta:
        model = Profile
        fields = ('firstname', 'lastname', 'username', 'discordtag', 'game', 'ingame_name', 'email',  'team', 'state', 'region',  'birthday', 'shirt_size')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'age': forms.TextInput(attrs={'class': 'input'}),
        }

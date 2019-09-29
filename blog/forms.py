from django import forms # импортирт формы Django
from .models import Post # импорт модели Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post # определяем, какая модель будет использоваться для создания формы
        fields = ('title', 'text',) # указываем, какие поля должны присутствовать в нашей форме
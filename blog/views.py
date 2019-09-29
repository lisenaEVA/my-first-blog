
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):  #собирает шаблон страницы
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    # Для получения записи из блога (используем QuerySet)
    return render(request, 'blog/post_list.html', {'posts': posts}) 
    # Функция post_list,  принимает request в качестве аргумента и возвращает результат работы функции render, 
    # которая уже соберftn  шаблон страницы blog/post_list.html 

def post_detail(request, pk): 
    post = get_object_or_404(Post, pk=pk) # отображение страницы ошибки,если не существует экземпляра объекта Post с заданным pkа
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):  # добавление нового поста
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid(): # проверка содержимого формы
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()   #сохраняем изменения  и создаем новую запись
            return redirect('post_detail', pk=post.pk) # переход на страницу записи
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})  
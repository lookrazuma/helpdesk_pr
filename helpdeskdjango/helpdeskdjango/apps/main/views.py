from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


def manage_view(request):
    tasks = Task.objects.all() 
    return render(request, 'main/manager.html', context={'tasks': tasks})

def manage_detail(request, task_id):
    try:
        task = Task.objects.get(pk = task_id)
    except Task.DoesNotExist:
        raise Http404('Задача не найдена')
    return render(request, 'main_app/employee_details.html', context= {'task': task})

# Возвращает значение страницы
def main(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

@permission_required('main.can_mark_returned')
def task_show(request):
    tasks = Task.objects.filter(author=request.user)
    #context_dict = {'favorites': favorites_list}
    #Дополнительная переменная воизбежание ошибок
    error = ''
    #Запись в БД через метод "Пост"
    if request.method == 'POST':
        form = TaskForm(request.POST)
        #Если форма доступа, то записываем имя юзера-автора и сохраняем в БД
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Ссылка добавлена')
            form.save()
            #возвращаем переадресацию пользователя на опр. страницу
            return redirect('/')
        #Если форма отправки некорректная, то
        else:
            error = 'Форма была неверной'

 
    #Получение информации из forms.py класса TaskForm
    form = TaskForm()
    context = {
        'form': form,
        'error': error,
        'tasks': tasks,
    }
    return render(request, 'main/task_show.html', context,)




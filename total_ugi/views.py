from django.shortcuts import render


def first_page(request):
    """Выводит домашнюю страницу"""

    content = {'title': 'CS AmidA'}
    return render(request, 'total_ugi/first_page.html', content)


def home(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Домашня сторінка CS AmidA',
        'name': 'User'
               }
    return render(request, 'total_ugi/home.html', content)


def login(request):
    """Выводит домашнюю страницу"""

    content = {'title': 'Вхід до CS AmidA'}
    return render(request, 'total_ugi/login.html', content)


def logout(request):
    """Выводит домашнюю страницу"""

    content = {'title': 'CS AmidA'}
    return render(request, 'total_ugi/first_page.html', content)


def telephone_directory(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Довідник',
        'name': 'User'
    }
    return render(request, 'total_ugi/telephone_directory.html', content)


def app_guide(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Інструкція',
        'name': 'User'
    }
    return render(request, 'total_ugi/app_guide.html', content)

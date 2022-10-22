from django.shortcuts import render, redirect


def all_materials_vsr(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Загальний облік матеріалів',
        'name': 'User'
    }
    return render(request, 'stat_vsr/toolbar_sider/bd_vsr/all_materials_vsr.html', content)


def investigations_vsr(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Службові розслідування ВСР',
        'name': 'User'
    }
    return render(request, 'stat_vsr/toolbar_sider/bd_vsr/investigations_vsr.html', content)


def policemen_vsr(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Працівники ВСР',
        'name': 'User'
    }
    return render(request, 'stat_vsr/toolbar_sider/bd_vsr/policemen_vsr.html', content)


def id_vsr(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Інформаційні довідки ВСР',
        'name': 'User'
    }
    return render(request, 'stat_vsr/toolbar_sider/bd_vsr/id_vsr.html', content)


def current_work_vsr(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Поточне навантаження ВСР',
        'name': 'User'
    }
    return render(request, 'stat_vsr/toolbar_sider/reports_vsr/current_work_vsr.html', content)


def general_report_vsr(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Загальний звіт ВСР',
        'name': 'User'
    }
    return render(request, 'stat_vsr/toolbar_sider/reports_vsr/general_report_vsr.html', content)


def investigations_report_vsr(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Дисциплінарні стягнення ВСР',
        'name': 'User'
    }
    return render(request, 'stat_vsr/toolbar_sider/reports_vsr/investigations_report_vsr.html', content)


def detailed_report_vsr(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Детальний звіт ВСР',
        'name': 'User'
    }
    return render(request, 'stat_vsr/toolbar_sider/reports_vsr/detailed_report_vsr.html', content)


def map_vsr(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Мапа ВСР',
        'name': 'User'
    }
    return render(request, 'stat_vsr/toolbar_sider/map_vsr.html', content)

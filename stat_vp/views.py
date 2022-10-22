from django.shortcuts import render


def all_materials_vp(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Матеріали ВП',
        'name': 'User'
    }
    return render(request, 'stat_vp/bd_vp/all_materials_vp.html', content)


def inspections_results_vp(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Перевірки ВП',
        'name': 'User'
    }
    return render(request, 'stat_vp/bd_vp/inspections_results_vp.html', content)


def policemen_vp(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Працівники ВП',
        'name': 'User'
    }
    return render(request, 'stat_vp/bd_vp/policemen_vp.html', content)


def id_vp(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Інформаційні довідки ВП',
        'name': 'User'
    }
    return render(request, 'stat_vp/bd_vp/id_vp.html', content)


def memorandums_about_inspections_vp(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Доповідні записки ВП',
        'name': 'User'
    }
    return render(request, 'stat_vp/bd_vp/memorandums_about_inspections_vp.html', content)


def certificates_about_inspections_vp(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Довідки ВП',
        'name': 'User'
    }
    return render(request, 'stat_vp/bd_vp/certificates_about_inspections_vp.html', content)


def investigations_vp(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Облік СР ВП',
        'name': 'User'
    }
    return render(request, 'stat_vp/bd_vp/investigations_vp.html', content)


def general_report_vp(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Загальний звіт ВП',
        'name': 'User'
    }
    return render(request, 'stat_vp/reports_vp/general_report_vp.html', content)


def current_work_vp(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Поточне навантаження ВП',
        'name': 'User'
    }
    return render(request, 'stat_vp/reports_vp/current_work_vp.html', content)


def investigations_report_vp(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Службові розслідування ВП',
        'name': 'User'
    }
    return render(request, 'stat_vp/reports_vp/investigations_report_vp.html', content)


def detailed_report_vp(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Детальний звіт ВП',
        'name': 'User'
    }
    return render(request, 'stat_vp/reports_vp/detailed_report_vp.html', content)


def map_vp(request):
    """Выводит домашнюю страницу"""

    content = {
        'title': 'Мапа перевірок ВП',
        'name': 'User'
    }
    return render(request, 'stat_vp/map_vp.html', content)

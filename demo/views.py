from django.shortcuts import render

from core.menu import MenuItem


def view_index(request):
    return render(request, 'demo/index.html', {
        'main_title': 'Página incial',
        'menu': MenuItem.get_menu(request)
    })


def view_calendar(request):
    return render(request, 'demo/calendario.html', {
        'main_title': 'Calendário',
        'menu': MenuItem.get_menu(request)
    })


def view_manutencao(request):
    return render(request, 'demo/atividade.html', {})


def view_helpdesk(request):
    return render(request, 'demo/helpdesk.html', {})

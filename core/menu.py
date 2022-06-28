from django.utils.translation import gettext as _


class MenuItem:
    def __init__(self, nome, icone, subitens=None, href=None):
        self.nome = nome
        self.icone = icone
        self.subitens = subitens
        self.href = href

    @classmethod
    def get_menu(cls, request):
        menu = []

        if request.user.is_superuser:
            menu.append(cls(_('menu pagina inicial'), 'bx bxs-home', subitens=[('Teste 1', 'template/index.html'), ('Teste 2', 'template/calendar.html')]))

        if request.user.is_superuser:
            menu.append(cls(_('menu calendario'), 'bx bx-calendar', href='template/calendar.html'))

        if request.user.is_superuser:
            menu.append(cls(_('menu mensagens'), 'bx bxs-message-rounded-detail', href='template/message.html'))

        return menu

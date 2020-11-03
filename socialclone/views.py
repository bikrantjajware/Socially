from django.views.generic import TemplateView


class homepage(TemplateView):
        template_name = 'index.html'


class thankyou(TemplateView):
        template_name = 'thankyou.html'


class login(TemplateView):
        template_name = 'login.html'
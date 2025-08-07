from pydoc import text
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import csv
import os
from django.conf import settings



class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Главная'
        context['content'] = "Услуги разработчика"
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        file_path = os.path.join(settings.BASE_DIR,'main/about.csv')
        data = {}
        
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data[row['section']] = row['text']
        except FileNotFoundError:
            data = {
                'title': 'Про нас',
                'content': 'Привет!',
                'text_on_page': 'Текст временно недоступен.'
            }
        
        context['title'] = data.get('title', 'Про нас')
        context['content'] = data.get('content', 'Про нас')
        context['text_on_page'] = data.get('text_on_page', '')
        
        return context



# def index(request):

#     context = {
#         'title': 'Home - Главная',
#         'content': "Магазин мебели HOME",
#     }

#     return render(request, 'main/index.html', context)


# def about(request):
#     context = {
#         'title': 'Home - О нас',
#         'content': "О нас",
#         'text_on_page': "Текст о том почему этот магазин такой классный, и какой хороший товар."
#     }

#     return render(request, 'main/about.html', context)

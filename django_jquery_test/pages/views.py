import time
from django.http import JsonResponse
from django.views.generic import TemplateView, View


class PageView(TemplateView):
    template_name = 'page.html'


class TaskView(View):

    def post(self, request, *args, **kwargs):
        post_data = request.POST
        someKey = post_data.get('someKey', None)
        print('Value of someKey in POST:', someKey)

        for i in range(10):
            time.sleep(0.5)
            print(f'slept for {0.5*(i+1)}s')
        return JsonResponse({'info': 'All good!'})


class RedirectedPageView(TemplateView):
    template_name = 'redirected_page.html'

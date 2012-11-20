import django.views.generic
from collections import OrderedDict


class GetToPostView(django.views.generic.TemplateView):
    
    template_name = 'get_to_post.html'
    
    def get_context_data(self, **kwargs):
        context_data = super(GetToPostView, self).get_context_data(**kwargs)
        
        if 'url' not in self.request.GET:
            raise django.http.Http404
        
        post_url = self.request.GET['url']
        post_data = OrderedDict([(key, value) for key, value in
                                 self.request.GET.items() if key != 'url'])
        
        context_data.update({'post_url': post_url,
                             'post_data': post_data,})
        return context_data
        
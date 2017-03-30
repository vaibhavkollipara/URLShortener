from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import View
from .models import ShortURL
from .forms import URLInputForm
from .utils import validate_url
from analytics.models import Click
# Create your views here.


class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})

    def post(self,request,*args,**kwargs):
        form = URLInputForm(request.POST or None)
        context ={
            'form' : form
        }
        if (form.is_valid()):
            url = form.cleaned_data["url"]
            url = validate_url(url)
            obj, created = ShortURL.objects.get_or_create(url=url)
            context['url'] = obj.url
            context['redirect'] = obj.shorturl
            if created:
                Click.objects.create_event(instance=obj)
            else:
                context['count'] = obj.click.count


        return render(request, 'index.html' , context)


class URLRedirect(View):

    def get(self,request,shorturl=None,*args,**kwargs):
        #print("shorturl : {}".format(shorturl))
        obj = get_object_or_404(ShortURL, shorturl=shorturl)
        print(Click.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
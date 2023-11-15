from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from boutique.models import Article
from django.shortcuts import redirect
from django.urls import reverse
from .forms import FormConnexion
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
# Create your views here.
def homepage(request):
    art = Article.objects.all().values()
    template= loader.get_template('home.html')
    context={
        'art' :art
    }
    return HttpResponse(template.render(context,request))

def add(request):
    art = Article.objects.all().values()
    template = loader.get_template('add.html')
    context = {
    'art': art,
}
    return HttpResponse(template.render(context, request))

def add_prod(request):
    pp=request.POST['prod']
    p =request.POST['prix']
    s =request.POST['stat']
    da =request.POST['dateCmd']

    article = Article(prod=pp, prix=p,stat=s, dateCmd=da)
    article.save()
    return redirect('/boutique')
   # return HttpResponseRedirect(reverse('boutique'))

def del_art(request,id):
    article = Article.objects.get(id=id)
    article.delete()
    return HttpResponseRedirect(reverse('homepage'))


def update_typ(request, id):
    art = Article.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
    'art': art,
    }
    return HttpResponse(template.render(context, request))


def update(request, id):
    pp = request.POST['prod']
    p = request.POST['prix']
    s = request.POST['stat']
    da =request.POST['dateCmd']
    article = Article.objects.get(id=id)
    article = Article(prod=pp, prix=p,stat=s, dateCmd=da)
    article.save()
    return HttpResponseRedirect(reverse('boutique'))



def connect (request):
    connect_form = FormConnexion ()
    return render(request, 'connexion.html', {'connect_form' :connect_form})
   


def signIn(request):
    username = request.POST['login']
    password = request.POST['mot2pass']
    user = authenticate(request, username=username,password=password)
    if user is not None:
        login(request, user)
        request.session['username'] = username
        return redirect('/boutique')

    else:
        print("Login et/ou mot de passe incorrect")
        return render(request,'connexion.html')
        #return HttpResponseRedirect(reverse('connect'))


def signOut(request):
    logout(request)
    return redirect('connect')


#def search (request):
   # article=article.objects.all()

    #if request.method=="GET":
    #    prod=request.GET.get('rechercher')
   #     if prod is not None:
       #     article=Article.objects.filter(name=prod)

#context={
   #     'article' :Article
  #  }
#return render(request,'article/home.html',context)
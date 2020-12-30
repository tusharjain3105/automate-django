import os
import sys
import webbrowser
# launching the app


def launch(project, app):
    virtual = f'{project}-VE'
    setting = f'''


#Additional Required Setting
import os
INSTALLED_APPS+=["{app}"]
TEMPLATES[0]["DIRS"]=[os.path.join(BASE_DIR,"templates")]
STATICFILES_DIRS = [
os.path.join(BASE_DIR, "static")
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"'''



    urls = f'''
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('{app}.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'''

    urls2 = f'''
from . import views
from django.urls import path
urlpatterns = [
    path('', views.index),
]
    '''
    views = '''
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
'''

    template = '''
<html>
<head>
    <title>Wecome to CODEVER</title>
</head>
<body>
    <h1>Thanks to learn from CODEVER<h1>
    <h2>Hope you enjoyed the tutorial. Don't forget to rate and comment.</h2>
</body>
</html>
    '''


    cd = os.getcwd()
    os.system('pip install virtualenv')
    os.system(f'virtualenv {virtual}')
    os.system('call virtual\Scripts\activate')
    os.chdir(virtual)
    os.system('pip install django')
    os.system(f'django-admin startproject {project}')
    os.chdir(project)
    os.system(f'django-admin startapp {app}')
    os.system('python manage.py migrate')
    os.system('python manage.py createsuperuser --username admin')
    os.chdir(os.path.join(cd,f'{virtual}/{project}'))
    os.mkdir(os.path.join(cd,f'{virtual}/{project}/templates'))
    os.mkdir(os.path.join(cd, f'{virtual}/{project}/static'))
    os.chdir(os.path.join(cd, f'{virtual}/{project}/{project}'))
    with open('settings.py', 'a+',encoding='utf-8') as f:
        f.write(setting)
    with open('urls.py','w',encoding='utf-8') as f:
        f.write(urls)
    os.chdir(f'../{app}')
    with open('urls.py', 'w+', encoding='utf-8') as f:
        f.write(urls2)
    with open('views.py', 'w+', encoding='utf-8') as f:
        f.write(views)
    os.chdir(os.path.join(cd, f'{virtual}/{project}/templates'))
    with open('index.html','w+',encoding='utf-8') as f:
        f.write(template)
    os.chdir('..')
    webbrowser.open('http:127.0.0.1:8000')
    os.system('python manage.py runserver')


project = str(input("Your Project Name: "))
app = str(input("Your App Name: "))
launch(project, app)

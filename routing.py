import webbrowser
import os 

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>This is your new HTML page. Change the file content in templates folder</h1>
</body>
</html>
'''

def createHTML(project, app, path, view=False):
    root = os.getcwd()
    if(view):
        urls=f'''+path({path},views.{path.capitalize}{view.capitalize}.as_view()
        '''
        with open(f'{root}/{project}-VE/{project}/{app}/views.py','a+',enccoding='utf-8') as f:
            if(f.read().index(f'from django.views.generic.{view}') == -1):
                f.seek(0)
                f.write(f'''
from django.views.generic.{view} import {view.capitalize()}View\n
                ''')
                f.seek(len(f.read()))
                f.write(f'''\n\n
class {path.capitalize}{view.capitalize}({view.capitalize()}View):
    template = '{path}.html'
                ''')
    else:
        urls = f'''
    path('{path}',views.{path}),
]
        '''
        views = f'''\n
def {path}(request):
    return render(request,'{path}.html')
        '''
        with open(f'{root}/{project}-VE/{project}/{app}/views.py', 'a+', encoding='utf-8') as f:
            f.write(views)
    os.system(f'call {project}-VE/Scripts/activate')
    os.chdir(os.path.join(root,f'{project}-VE/{project}/templates'))
    with open(f'{path}.html','w+',encoding='utf-8') as f:
        f.write(html)
    os.chdir(f'../{app}')
    with open('urls.py','r+',encoding='utf-8') as f:
        _ = f.read().replace(']',urls)
    with open('urls.py', 'w', encoding='utf-8') as f:
        f.write(_)
    os.chdir(os.path.join(root, f'{project}-VE/{project}'))
    webbrowser.open(f'http://127.0.0.1:8000/{path}')
    os.system('python manage.py runserver')



project = input('Project: ')
app = input('App: ')
page = input('Page: ')
createHTML(project, app, page)

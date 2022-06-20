from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Forms
from console.forms.request_form import RequestForm
from console.forms.login_form import LoginForm
from console.forms.create_client_form import CreateClientForm
from console.forms.client_upload_form import ClientUploadForm

# Usecases
from console.usecases.usecases import Usecases

# Custom wrapper for authenticating id
from console.wrappers import login_required

# Global usecase object.
usecases = Usecases()

def index(response):
    if response.method == 'POST':
        form = LoginForm(response.POST)
        if form.is_valid():
            id = usecases.login(form.clean())            
            return HttpResponseRedirect(f'/manager/{id}/console')
    else:
        form = LoginForm()
        return render(response, 'index.html', {'form': form})        

@login_required
def console(response, rm_id):
    requests = usecases.get_request_list()
    form_data = {
        'request_url': 'create_request/',
        'create_client_url': 'create_client/',
        'client_list_url':'client_list/',
        'req_list':requests
    }
    
    return render(response, 'console.html', form_data)

@login_required
def create_client(response, rm_id):
    '''
    Create new client usingthe form data.
    '''
    if response.method == 'POST':
        form = CreateClientForm(response.POST)
        if form.is_valid():
            # Input values into form data
            client = usecases.create_client_usecase(form.clean())
            
            return HttpResponseRedirect('/console/')
    else:
        client_form = CreateClientForm()
        form = {
            'console_url': f'manager/{rm_id}/console',
            'form': client_form
        }
        return render(response, 'create_client.html', form)

@login_required
def client_list(response, rm_id):
    '''Creates a client list and passes it to a html form.'''
    form = usecases.get_client_list()
    form['console_url'] = f'manager/{rm_id}/console'
    return render(response, 'client_list.html', form)

@login_required
def create_request(response, rm_id):
    if response.method == 'POST':
        form = RequestForm(response.POST)
        if form.is_valid():
            usecases.create_request_usecase(form.clean(), rm_id)
            return HttpResponseRedirect('')
        else:
            return HttpResponse(response, {'message': 'The form is not valid'})
    else:
        request_form = RequestForm()
        drop_down = usecases.storage.get_clients()
        rm = usecases.storage.get_rm(rm_id)
        form = {
            'console_url': f'manager/{rm_id}/console',
            'rm': rm.to_dict(),
            'client_list': drop_down,
            'request': request_form
        }
        return render(response, 'request_form.html', form)

def client_upload(request, client_url):
    # Check client url is 
    if request.method == 'POST':
        form = ClientUploadForm(request.POST, request.FILES)
        if form.is_valid():
            usecases.upload_client_file(form.files['file'], client_url)

    else:
        if not usecases.is_client_url_active(client_url):
            return HttpResponseRedirect('error/', {'error': 'The URL you are using is no longer active'})
        
        client = usecases.get_client_by_url(client_url)
        client_upload_form = ClientUploadForm()
        form = {
            'client': client,
            'client_upload': client_upload_form
        }
        return render(request, 'client_upload.html', form)
    return render(request, 'client_upload.html')
    

def server_error(request):
    return render(request, 'error.html')
    
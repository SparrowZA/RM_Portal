from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail

# Forms
from console.forms.request_form import RequestForm
from console.forms.login_form import LoginForm
from console.forms.create_client_form import CreateClientForm
from console.forms.client_upload_form import ClientUploadForm

# Usecases
from console.usecases.usecases import Usecases

# Response util
from console.utils.response_builder import ResponseBuilder

# Request builder
from console.requests.login_request import (build_login_request, LoginInvalidRequest, LoginValidRequest)

# Storage adapter
from console.adapters.django_storage import DjangoStorage

# Custom wrapper for authenticating id
from console.wrappers import login_required

# Global usecase object.
usecases = Usecases(DjangoStorage(), ResponseBuilder())

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login_request = build_login_request(form.clean())
            response = usecases.login(login_request)   
            if response.is_success():
                rm_id = response.data['rm_id']
                return HttpResponseRedirect(f'/manager/{rm_id}/console')
            else:
                data = {
                    'response': response.to_dict(),
                    'form': LoginForm()
                }
                return render(request, 'index.html', data)
        else:
            data = {
                'response': {'result': 'error', 'error_message': 'Incorrect credentials.'},
                'form': LoginForm()
            }
            return render(request, 'index.html', data)
    else:
        form = LoginForm()
        return render(request, 'index.html', {'form': form})        

@login_required(usecases.storage)
def console(request, rm_id):
    requests = usecases.get_request_list()
    form_data = {
        'request_url': 'create_request/',
        'create_client_url': 'create_client/',
        'client_list_url':'client_list/',
        'req_list':requests
    }
    
    return render(request, 'console.html', form_data)

@login_required(usecases.storage)
def create_client(request, rm_id):
    '''
    Create new client using the form data.
    '''
    if request.method == 'POST':
        form = CreateClientForm(request.POST)
        if form.is_valid():
            # Input values into form data
            response = usecases.create_client(form.clean())
            data = {
                'console_url': f'manager/{rm_id}/console',
                'response': response.to_dict(),
                'form': CreateClientForm()
            }
            
            return render(request, 'create_client.html', data)
        else:
            response = {'result': 'error', 'error_message': 'Invalid form data.'}
            data = {
                'console_url': f'manager/{rm_id}/console',
                'response': response,
                'form': CreateClientForm()
            }
            
            return render(request, 'create_client.html', data)
    else:
        client_form = CreateClientForm()
        form = {
            'console_url': f'manager/{rm_id}/console',
            'form': client_form
        }
        return render(request, 'create_client.html', form)

@login_required(usecases.storage)
def client_list(request, rm_id):
    '''Creates a client list and passes it to a html form.'''
    response = usecases.get_client_list()
    data = {
                'console_url': f'manager/{rm_id}/console',
                'response': response.to_dict()
            }

    return render(request, 'client_list.html', data)

@login_required(usecases.storage)
def create_request(request, rm_id):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            response = usecases.create_request(form.clean(), rm_id)

            if response.is_success():
                try:
                    send_mail(
                        response.data['email'].subject,
                        response.data['email'].message,
                        response.data['email'].sender,
                        response.data['email'].recipient, 
                        fail_silently=False
                    )
                except Exception as e:
                    response.result = 'error'
                    response.error_message = e

            data = {
                'console_url': f'manager/{rm_id}/console',
                'rm': usecases.storage.get_rm(rm_id).to_dict(),
                'client_list': usecases.storage.get_clients(),
                'response': response.to_dict(),
                'form': RequestForm()
            }
            
            return render(request, 'request_form.html', data)
        else:
            response = {'result': 'error', 'error_message': 'Invalid form data.'}
            data = {
                'console_url': f'manager/{rm_id}/console',
                'rm': usecases.storage.get_rm(rm_id).to_dict(),
                'client_list': usecases.storage.get_clients(),
                'response': response,
                'form': RequestForm()
            }
            return render(request, 'request_form.html', data)
    else:
        request_form = RequestForm()
        drop_down = usecases.storage.get_clients()
        rm = usecases.storage.get_rm(rm_id)
        form = {
            'console_url': f'manager/{rm_id}/console',
            'rm': rm.to_dict(),
            'client_list': drop_down,
            'form': request_form
        }
        return render(request, 'request_form.html', form)

def client_upload(request, client_url):
    if request.method == 'POST':
        form = ClientUploadForm(request.POST, request.FILES)
        if form.is_valid():
            doc = usecases.upload_client_file(form.files['file'], client_url)
            return HttpResponseRedirect('client_post_upload/')
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

def client_post_upload(request):
    return render(request, 'client_post_upload.html')
    
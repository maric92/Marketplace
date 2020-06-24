import requests
from django.shortcuts import render
from .models import Company
from .models import Product
from .forms import CompanyForm
from .forms import ProductForm


def validate_manifest(company, manifest_url):
    response = company.validate_manifest(manifest_url)
    if response.status_code == 201:
        return {'success': True,
                'message': 'Validation issued, '
                           'id: %s' % (response.content)['id']}
    return {'success': False,
            'message': 'FAILED to issue validation. '
                       'Status code: %d' % response.status_code}


def is_manifest_valid(company, manifest_id):
    response = company.is_manifest_valid(manifest_id)
    if response is None:
        return {'success': True,
                'message': "Your manifest hasn't been processed yet"}
    if response is True:
        return {'success': True,
                'message': 'Your manifest is valid! '
                           'You can now add your app to the marketplace'}
    return {'success': True,
            'message': 'Your manifest is not valid:\n%s' % response}


def create(company, manifest_id):
    response = company.create(manifest_id)
    if response.status_code == 201:
        return {'success': True,
                'message': ('Your product has been added to marketplace!\n'
                            'id: %s, slug: %s') % (content['id'],
                                                   content['slug'])}
    else:
        return {'success': False,
                'message': response.content}


def delete(company, name_prod):
    response = company.delete(name_prod)
    if response.status_code != 204:
        return {'success': False,
                'message': 'Error, status code: %d, \nMessage: %s'}
    return {'success': True,
            'message': 'App deleted'}


def list_prod(company):
    response = company.list_prod()
    if response.status_code == 200:
        return {'success': True,
                'message': content}
    else:
        return {'success': False,
                'message': response.content}



def add_content_ratings(company, name_prod):
    response = company.add_content_ratings(name_prod)
    if response.status_code != 201:
        return {'success': False,
                'message': 'Error, status code: %d, \nMessage: %s' % (
                    response.status_code, response.content)}
    return {'success': True,
            'message': 'Content ratings added'}



def get_categories(company):
    response = company.get_categories()
    if response.status_code != 200:
        return {'success': False,
                'message': 'Error, status code: %d, \nMessage: %s' % (
                    response.status_code, response.content)}
    message = ''
    for desc in content['objects']:
        message += '%s: %s\n' % (desc['name'], desc['price'])
    return {'success': True,
            'message': message}


def prod_state(company, name_prod, status=None):
    #try to realize order for buying with status, but think it not working
    response = company(name_prod, status)
    if response.status_code != 202:
        return {'success': False,
                'message': 'Error, status code: %d, \nMessage: %s' % (
                    response.status_code, response.content)}
    return {'success': True,
            'message': '\n'.join(
                [ (k, v) for k, v in content.items()])}

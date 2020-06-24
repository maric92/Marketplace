from django.contrib import admin
from .models import Company, Product

COMMANDS = {'validate_manifest': commands.validate_manifest,
            'is_manifest_valid': commands.is_manifest_valid,
            'create': commands.create,
            'delete': commands.delete,
            'list_prod': commands.name_prod,
            'add_content_ratings': commands.add_content_ratings,
            'get_categories': commands.get_categories,
            'prod_state': commands.prod_state}

admin.site.register(Marketplace)


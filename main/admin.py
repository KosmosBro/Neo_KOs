from django.contrib import admin

from main.models import Category, Company, Contact, Branch

admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Branch)

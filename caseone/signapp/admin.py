#coding:utf-8
from django.contrib import admin
from signapp.models import Sign,Project,Environment,Interface,Case,Plan,Report

# Register your models here.

class SignAdmin(admin.ModelAdmin):
	list_display = ['sign_id','sign_name','description']

class ProjectAdmin(admin.ModelAdmin):
	list_display = ['prj_name','sign','description']

class EnvAdmin(admin.ModelAdmin):
	list_display = ['env_name','project','description','url']

class InterfaceAdmin(admin.ModelAdmin):
	list_display = ['if_name','url','method','data_type','project','is_sign','request_header_param','request_body_param',
	'response_header_param','response_body_param']

class CaseAdmin(admin.ModelAdmin):
	list_display = ['case_name','project','content']

class PlanAdmin(admin.ModelAdmin):
	list_display = ['plan_name','project','environment','content']

admin.site.register(Sign,SignAdmin)
admin.site.register(Project)
admin.site.register(Environment)
admin.site.register(Interface)
admin.site.register(Case)
admin.site.register(Plan)
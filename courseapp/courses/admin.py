from django.contrib import admin
from .models import Category, Course


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    list_select_related = True
    list_per_page = 200
    list_max_show_all = 150
    search_fields = ['name']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'subject']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course)



from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.safestring import mark_safe

from .models import Category, Course, Lesson, Tag
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CourseAppAdminSite(admin.AdminSite):
    site_header = 'iSuccess'

    def get_urls(self):
        return [path('course-stats/', self.stats_view)] + super().get_urls()

    def stats_view(self, request):
        return TemplateResponse(request, 'admin/stats.html')


admin_site = CourseAppAdminSite(name='myapp')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    list_select_related = True
    list_per_page = 200
    list_max_show_all = 150
    search_fields = ['name']


class CourseForm(forms.ModelForm):
    descriptions = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonInlineAdmin(admin.StackedInline):
    model = Lesson
    fk_name = 'course'  # tên khoá ngoại (tuỳ chọn)


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ['img']
    form = CourseForm
    inlines = [LessonInlineAdmin]

    def img(self, course):
        if course:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'.format(url=course.image.name)
            )

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }


admin_site.register(Category, CategoryAdmin)
admin_site.register(Course, CourseAdmin)
admin_site.register(Lesson)
admin_site.register(Tag)

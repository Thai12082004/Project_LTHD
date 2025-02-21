from django.contrib import admin
from courses.models import Course, Category, Lesson
from django.utils.html import mark_safe

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'category']
    readonly_fields = ['image_view']
    list_editable = ['subject']

    def image_view(self, course):
        return mark_safe(f"<img src='/static/{course.image.name}' width='150' />")


class MyLessonAdmin(admin.ModelAdmin):
    form = LessonForm

class CourseAppAdminSite(admin.AdminSite):
    site_header = 'Hệ thống khoá học trực tuyến'

admin_site = CourseAppAdminSite(name='myadmin')

admin_site.register(Category)
admin_site.register(Course, MyCourseAdmin)
admin_site.register(Lesson, MyLessonAdmin)

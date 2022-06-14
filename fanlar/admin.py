from django.contrib import admin
from .models import AboutPage, Kurslar, Cantact,Section, Teachers, Registered_students
admin.site.register(Kurslar)
admin.site.register(Section)
admin.site.register(Cantact)
admin.site.register(Teachers)
admin.site.register(Registered_students)

admin.site.register(AboutPage)




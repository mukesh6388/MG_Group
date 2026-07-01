from django.contrib import admin
from .models import Contact
from .models import PropertyInquiry
from .models import Job
from .models import JobCategory
from .models import JobApplication


# Register your models here.

admin.site.register(Contact)
admin.site.register(PropertyInquiry)
admin.site.register(Job)
admin.site.register(JobCategory)
admin.site.register(JobApplication)
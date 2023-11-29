from django.contrib import admin
from .models import UserProfile, Company, Skill, JobListing, Applicant, News, Comment


admin.site.register(UserProfile)
admin.site.register(Company)
admin.site.register(Skill)
admin.site.register(JobListing)
admin.site.register(Applicant)
admin.site.register(News)
admin.site.register(Comment)

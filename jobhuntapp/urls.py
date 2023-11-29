from django.urls import path
from .views import (UserRegistrationView,
                    UserProfileList, UserProfileDetail,
                    CompanyList, CompanyDetail,
                    SkillList, SkillDetail,
                    JobListingList, JobListingDetail,
                    ApplicantList, ApplicantDetail,
                    NewsList, NewsDetail,
                    CommentList, CommentDetail
                    )

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('user-profiles/', UserProfileList.as_view(), name='userprofile-list'),
    path('user-profiles/<int:pk>/', UserProfileDetail.as_view(),
         name='userprofile-detail'),

    path('companies/', CompanyList.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetail.as_view(), name='company-detail'),

    path('skills/', SkillList.as_view(), name='skill-list'),
    path('skills/<int:pk>/', SkillDetail.as_view(), name='skill-detail'),

    path('job-listings/', JobListingList.as_view(), name='joblisting-list'),
    path('job-listings/<int:pk>/', JobListingDetail.as_view(),
         name='joblisting-detail'),

    path('applicants/', ApplicantList.as_view(), name='applicant-list'),
    path('applicants/<int:pk>/', ApplicantDetail.as_view(), name='applicant-detail'),

    path('news/', NewsList.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news-detail'),

    path('comments/', CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
]

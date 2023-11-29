from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile, Company, Skill, JobListing, Applicant, News, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'bio', 'profile_picture',)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'location', 'website')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name')


class JobListingSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    skills = SkillSerializer(many=True)

    class Meta:
        model = JobListing
        fields = ('id', 'title', 'description', 'company',
                  'skills', 'posted_at', 'deadline', 'is_active')


class ApplicantSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()
    applied_job = JobListingSerializer()

    class Meta:
        model = Applicant
        fields = ('id', 'user_profile', 'applied_job',
                  'applied_at', 'cover_letter', 'resume')


class NewsSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer()

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'author', 'pub_date', 'image')


class CommentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'user', 'news', 'text', 'pub_date')

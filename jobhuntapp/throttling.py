from rest_framework.throttling import SimpleRateThrottle, BaseThrottle
from django.contrib.auth.models import User
import random
import throttling


class UserRateThrottle(BaseThrottle):

    def allow_request(self, request, view):
        return request.user and request.user.is_authenticated

    def wait(self):
        return 10 if not self.allow_request(self.request, self.view) else super().wait()


class CustomThrottle(SimpleRateThrottle):

    def allow_request(self, request, view):
        return request.user and request.user.is_authenticated

    def wait(self):
        return 10 if not self.allow_request(self.request, self.view) else super().wait()


class RandomRateThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        return random.randint(1, 10) != 1

from django.contrib import admin

# Register your models here.
from .models import Subscription, MessageForm, Blog
admin.site.register(Subscription)
admin.site.register(MessageForm)
admin.site.register(Blog)
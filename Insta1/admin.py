from django.contrib import admin
from Insta1.models import Post,testModel, InstaUser,Like,UserConnection
# Register your models here.
admin.site.register(Post)
admin.site.register(testModel)
admin.site.register(InstaUser)
admin.site.register(Like)
admin.site.register(UserConnection)
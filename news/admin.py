from django.contrib import admin

from .models import Post, Category, Author

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Category)

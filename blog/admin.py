from django.contrib import admin

# Register your models here.


from blog.models import Category , Post

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post , PostAdmin)
admin.site.register(Category , CategoryAdmin)


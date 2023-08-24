from django.contrib import admin

# Register your models here.

from .models import Books

#admin.site.register(Books)


##

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'borrowed_by_display', 'borrow_date')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset

    def borrowed_by_display(self, obj):
        if obj.borrowed_by is None:
            return "Available to Borrow"
        else:
            return obj.borrowed_by
    borrowed_by_display.short_description = 'Borrowed By'

admin.site.register(Books, BooksAdmin)
from django.contrib import admin
from app1.models import Client, Product, Order


@admin.action(description="Сбросить количество")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(amount=0)


class ClientAdmin (admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    ordering = ['name']
    list_filter = ['reg_date']
    search_fields = ['name']
    search_help_text = 'Поиск по имени (name)'
    readonly_fields = ['reg_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Домашний адрес',
                'fields': ['address'],
            },
        )
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'amount']
    ordering = ['title', '-amount']
    list_filter = ['add_date', 'price']
    search_fields = ['title']
    search_help_text = 'Поиск по полю Наименование (title)'
    actions = [reset_quantity]
    # fields = ['title', 'price', 'amount', 'add_date']
    readonly_fields = ['add_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробное описание товара',
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'amount'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['add_date'],
            }
        ),
    ]


# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)

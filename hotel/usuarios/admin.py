from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('telefono', 'direccion')}),
    )
    list_display = ('username', 'email', 'telefono', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'telefono')

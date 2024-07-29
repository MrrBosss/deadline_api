from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


from .forms import UserAdminChangeForm
from .forms import UserAdminCreationForm
from .models import User, Department

admin.site.register(Department)

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email", "department", "avatar")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["get_avatar", "name", "department", "is_superuser"]
    search_fields = ["name"]
    list_display_links =  ['name','get_avatar']
    
    def get_avatar(self, obj):
        avatar = obj.avatar.url if obj.avatar else ""
        return mark_safe(
            f'<img src="{avatar}" width="128" height="128"/>'  # if obj.logo_light else '<div>Rasmsiz</div>'
        )

    get_avatar.short_description = 'Логотип'
    get_avatar.allow_tags = True
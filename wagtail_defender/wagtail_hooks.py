from defender.models import AccessAttempt
from wagtail import hooks
from wagtail.admin.viewsets.base import ViewSetGroup
from wagtail.admin.viewsets.model import ModelViewSet


class AccessAttemptViewSet(ModelViewSet):
    model = AccessAttempt
    form_fields = []
    list_display = ["username", "ip_address", "attempt_time", "login_valid"]
    icon = "key"
    inspect_view_enabled = True
    menu_order = 300


class AccessAttemptViewSetGroup(ViewSetGroup):
    items = [
        AccessAttemptViewSet,
    ]
    add_to_admin_menu = True
    menu_order = 8999
    menu_label = "Defender"
    menu_icon = "lock"


@hooks.register("register_admin_viewset")
def register_viewset():
    return AccessAttemptViewSetGroup()



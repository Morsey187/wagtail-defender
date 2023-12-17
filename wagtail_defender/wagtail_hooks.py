from defender.models import AccessAttempt
from django.utils.translation import gettext_lazy as _
from wagtail import hooks
from wagtail.admin.ui.tables import BulkActionsCheckboxColumn
from wagtail.admin.views.bulk_action import BulkAction
from wagtail.admin.views.generic import IndexView
from wagtail.admin.viewsets.base import ViewSetGroup
from wagtail.admin.viewsets.model import ModelViewSet


@hooks.register("register_bulk_action")
class CustomDeleteBulkAction(BulkAction):
    display_name = _("Delete")
    aria_label = _("Delete selected objects")
    action_type = "delete"
    template_name = "wagtail_defender/wagtailadmin/confirm_bulk_delete.html"
    models = [AccessAttempt]

    @classmethod
    def execute_action(cls, objects, **kwargs):
        num_parent_objects = len(objects)
        cls.get_default_model().objects.filter(
            pk__in=[obj.pk for obj in objects]
        ).delete()
        return num_parent_objects, 0


class IndexViewWithBulkActions(IndexView):
    """
    Override the IndexView's get_columns method to append a bulk actions checkbox column
    """

    def get_columns(self):
        return [
            BulkActionsCheckboxColumn("checkbox", accessor=lambda obj: obj),
            *super().get_columns(),
        ]


class AccessAttemptViewSet(ModelViewSet):
    model = AccessAttempt
    form_fields = []
    list_display = ["username", "ip_address", "attempt_time", "login_valid"]
    icon = "key"
    inspect_view_enabled = True
    menu_order = 300
    # Support bulk actions
    index_template_name = (
        "wagtail_defender/wagtailadmin/access_attempt_view_set_index.html"
    )
    index_view_class = IndexViewWithBulkActions


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



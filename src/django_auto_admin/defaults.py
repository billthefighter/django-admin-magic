# The app_label of the app to auto-register models for.
APP_LABEL = None

# Terms to exclude from list_display when auto-generating it.
DEFAULT_EXCLUDED_TERMS = ["_ptr", "uuid", "poly", "baseclass", "basemodel", "histo", "pk", "id", "search"]

# Model names to exclude from registration. Useful for excluding historical models.
DEFAULT_DO_NOT_REGISTER_FILTER_STRING_LIST = ["Historical"]

# Admin attributes that are often tuples but need to be lists for modification.
ADMIN_TUPLE_ATTRIBUTES_TO_LIST = ["list_display", "list_filter", "search_fields", "readonly_fields"]

# Whether to reorder linkify fields to avoid them being first in list_display
# This prevents issues with clicking on the first column in admin changelist views
REORDER_LINKIFY_FIELDS = True 
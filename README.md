# Django Auto Admin

A simple Django app to automatically register your models with the admin site.

## Installation

Install the package from PyPI:

```bash
pip install django-auto-admin
```

Then, add it to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # ...
    "django_auto_admin",
    # ...
]
```

## Demo

A full-featured demo app is included in this repository to showcase all features of Django Auto Admin, including:
- Automatic admin registration for a variety of model types
- Sample data for all models
- Auto-generated superuser for instant login
- Landing page listing all registered models

**Quickstart:**

```bash
python demo_app/setup_demo.py
python demo_app/manage.py runserver
```

- Main demo: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/ (login: `admin` / `admin123`)

See [demo/README.md](demo/README.md) for full demo instructions, troubleshooting, and customization tips.

## Configuration

This library needs to know which of your apps to register models for. Specify the `app_label` in your `settings.py`:

```python
AUTO_ADMIN_APP_LABEL = "my_app"
```

### Advanced Configuration

You can override the default settings by adding them to your `settings.py` with the `AUTO_ADMIN_` prefix.

-   `DEFAULT_EXCLUDED_TERMS`: A list of strings to exclude from the `list_display` when it's auto-generated.
-   `DEFAULT_DO_NOT_REGISTER_FILTER_STRING_LIST`: A list of strings. Any model whose name contains one of these strings will not be registered.
-   `ADMIN_TUPLE_ATTRIBUTES_TO_LIST`: A list of admin attributes that are typically tuples but need to be lists for modification (e.g., `list_display`, `list_filter`).
-   `REORDER_LINKIFY_FIELDS`: Boolean flag (default: `True`) that controls whether linkify fields should be reordered to avoid being the first column in admin changelist views. This prevents issues with clicking on the first column, which is often used for row selection checkboxes.

### Linkify Field Reordering

By default, Django Auto Admin automatically reorders `list_display` fields to ensure that linkify functions (foreign key links) are not the first column in admin changelist views. This is because the first column in Django admin is often used for row selection checkboxes, and having a clickable link there can interfere with the selection functionality.

**Example:**
```python
# Without reordering (problematic):
list_display = [linkify('parent'), 'name', 'created_at']

# With reordering (fixed):
list_display = ['name', linkify('parent'), 'created_at']
```

You can disable this behavior by setting:
```python
AUTO_ADMIN_REORDER_LINKIFY_FIELDS = False
```

## Usage

Once installed and configured, the library will automatically register all the models in the specified app with the admin site.

### Customizing the Admin

You can still customize the admin classes after they've been registered. The `AdminModelRegistrar` instance provides several methods for this purpose. You can get the registrar instance from the `apps` registry.

```python
from django.apps import apps

# Get the registrar instance
registrar = apps.get_app_config("django_auto_admin").registrar

# Get the admin class for a model
MyModelAdmin = registrar.return_admin_class_for_model(MyModel)

# Customize the admin class
MyModelAdmin.list_display.append("my_custom_field")
```

### Available Methods

-   `append_list_display(model, list_display)`
-   `prepend_list_display(model, list_display)`
-   `remove_list_display(model, list_display_to_remove)`
-   `append_filter_display(model, list_filter)`
-   `add_search_fields(model, search_fields)`
-   `update_list_select_related(model, list_select_related)`
-   `add_admin_method(model, method_name, method_func, short_description=None, is_action=False)`
-   `append_inline(model, inline_class)`

## Polymorphic Models

This library automatically detects if `django-polymorphic` is installed and will use the appropriate admin classes for polymorphic models. There is no extra configuration required. 
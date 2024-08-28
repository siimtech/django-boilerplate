from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

unfold_settings = {
    "SITE_TITLE": True,
    "SITE_HEADER": True,
    "SITE_URL": "/",
    # "SITE_ICON": lambda request: static("icon.svg"),  # both modes, optimise for 32px height
    # "SITE_ICON": {
    #     "light": lambda request: static("icon-light.svg"),  # light mode
    #     "dark": lambda request: static("icon-dark.svg"),  # dark mode
    # },
    # "SITE_LOGO": lambda request: static("logo.svg"),  # both modes, optimise for 32px height
    # "SITE_LOGO": {
    #     "light": lambda request: static("logo-light.svg"),  # light mode
    #     "dark": lambda request: static("logo-dark.svg"),  # dark mode
    # },
    "SITE_SYMBOL": "speed",  # symbol from icon set
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("favicon.svg"),
        },
    ],
    "SHOW_HISTORY": True,  # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": True,  # show/hide "View on site" button, default: True
    # "ENVIRONMENT": ["Production", "danger", "info", "danger", "warning", "success"],
    "DASHBOARD_CALLBACK": "newproject.views.dashboard_callback",
    # "THEME": "dark", # Force theme: "dark" or "light". Will disable theme switcher
    "LOGIN": {
        # "image": lambda request: static("sample/login-bg.jpg"),
        # "redirect_after": lambda request: reverse_lazy("admin:APP_MODEL_changelist"),
    },
    "STYLES": [
        lambda request: static("css/style.css"),
    ],
    "SCRIPTS": [
        lambda request: static("js/script.js"),
    ],
    "COLORS": {
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "fr": "🇫🇷",
                "nl": "🇧🇪",
            },
        },
    },
    "SIDEBAR": {
        "show_search": True,  # Search in applications and models names
        "show_all_applications": False,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _("사용자 관리"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("관리자"),
                        "icon": "shield_person",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:users_admin_changelist"),
                        "permission": "newproject.views.admin_permission_callback",
                    },
                    {
                        "title": _("사용자"),
                        "icon": "person",
                        "link": reverse_lazy("admin:users_appuser_changelist"),
                        "badge": "newproject.views.user_badge_callback",
                    },
                    {
                        "title": _("소셜 계정"),
                        "icon": "groups_3",
                        "link": reverse_lazy("admin:users_socialaccount_changelist"),
                    },
                    {
                        "title": _("그룹"),
                        "icon": "group",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
            #         "title": _("Navigation"),
            #         "separator": True,  # Top border
            #         "collapsible": True,  # Collapsible group of links
            #         "items": [
            #             {
            #                 "title": _("Dashboard"),
            # #                 "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
            #                 "link": reverse_lazy("admin:index"),
            # #                 # "badge": "sample_app.badge_callback",
            # #                 # "permission": lambda request: request.user.is_superuser,
            #             },
            # #             {
            # #                 "title": _("Users"),
            # #                 "icon": "people",
            # #                 # "link": reverse_lazy("admin:users_user_changelist"),
            # #             },
            #         ],
        ],
    },
    # "TABS": [
    #     {
    #         "models": [
    #             "app_label.model_name_in_lowercase",
    #         ],
    #         "items": [
    #             {
    #                 "title": _("Your custom title"),
    #                 "link": reverse_lazy("admin:app_label_model_name_changelist"),
    #                 "permission": "sample_app.permission_callback",
    #             },
    #         ],
    #     },
    # ],
}

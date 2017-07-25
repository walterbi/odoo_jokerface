# -*- coding: utf-8 -*-

{
    'name': 'Membership',
    'version': '1.0',
    'category': 'Tools',
    'description': """
Membership
=========================================================================
    """,
    'depends': ['base', 'web', 'website_sale', 'website_portal'],
    'data': [
        'views/membership_menu.xml',
        'views/membership_information_view.xml',
        'views/card_information_view.xml',
        'views/membership_type_view.xml',
        'views/website_portal_sale_view.xml',
    ],
    'application': True,
}

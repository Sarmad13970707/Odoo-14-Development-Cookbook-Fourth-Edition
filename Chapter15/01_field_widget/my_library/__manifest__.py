# -*- coding: utf-8 -*-
{
        'name': "My Library",  # Module title
    'summary': "Manage books easily",  # Module subtitle phrase
    'description': """
Manage Library
==============
Description related to library.
    """,  # Supports reStructuredText(RST) format
    'author': "Parth Gajjar",
    'website': "http://www.example.com",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['base', 'web'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/templates.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'my_library/static/src/js/field_widget.js',
            'my_library/static/src/scss/field_widget.scss'
        ],
    }
    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}

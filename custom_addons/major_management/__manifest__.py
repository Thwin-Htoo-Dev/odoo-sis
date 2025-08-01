{
    'name': 'Major Management',
    'version': '1.0',
    'depends': ['base', 'openeducat_core'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/sequence_data.xml',
    ],
    'installable': True,
    'application': False,
    'assets': {
        'web.assets_backend': [
            'major_management/static/src/css/image_styles.css',
        ],
    }
}

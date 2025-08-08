{
    "name": "Faculty Qualification",
    "version": "1.0",
    "depends": ["base", "openeducat_core"],
    "author": "Your Name",
    "category": "SIS",
    "description": "Faculty Qualification inside SIS",
    "data": [
        "security/ir.model.access.csv",
        "views/faculty_views.xml",
        "data/sequence.xml",
        'report/report_faculty_qualification.xml',
        'report/report_faculty_qualification_template.xml',
    ],
    # 'assets': {
    # 'web.report_assets_common': [
    #     'faculty_qualification/static/fonts/NotoSansMyanmar-Regular.ttf',
    #     ],
    # },

    "installable": True,
    "application": True,
}

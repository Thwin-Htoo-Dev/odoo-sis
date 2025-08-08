{
    "name": "Faculty Major Extension",
    "version": "1.0",
    "category": "Education",
    "summary": "Add Major Field to Faculty",
    "description": """
        This module extends OpenEduCat Faculty model to include a relation to Course Major.
    """,
    "author": "Your Name",
    "depends": ["base", "openeducat_core"],
    "data": [
        "views/views.xml",  # adjust path if different
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}

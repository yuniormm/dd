# -*- coding: utf-8 -*-
{
    'name': "GDU-Evaluacion",

    'summary': """
        GDU-Evaluacion""",

    'description': """
        GDU-Evaluacion
    """,

    'author': "Raul Rolando Jardinot Gonzalez and Mildrey Mustelier Bandera",
    'category': 'Uncategorized',
    'version': '13.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'gdu_base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_evaluation.xml',
        'views/view_category_evaluation.xml',
        'views/menu.xml',

        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
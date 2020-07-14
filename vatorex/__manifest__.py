# -*- encoding: utf-8 -*-
{
    'name': 'Vatorex',
    'category': 'Hidden',
    'sequence': 7,
    'summary': 'Vatorex Training',
    'version': '0.1',
    'description': '',
    'depends': [
        'website_mail',
        'website_form',
        'website_blog',
        'website_crm',
    ],
    'images': [
        'static/description/website_theme_screenshot.jpg',
    ],

    'data': [

        # data
        'data/menu.xml',


        # assets

        # layout



        #backend
        'views/backend/blog_post_form.xml',
        'views/backend/res_partner_form.xml',


        # pages
        'views/frontend/blog_template.xml',
        'views/frontend/simple_form.xml',
        'views/frontend/Qweb_example.xml',

        # generic views

    ],

}

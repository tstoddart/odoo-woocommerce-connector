# -*- coding: utf-8 -*-
{
    'name': "WooCommerce Connector",
    'summary': """This module enables users to connect woocommerce api to odoo modules of sales, partners and inventory""",
    'description': """
        Following are the steps to use this module effectively:
        1) Put in the KEY and SECRET in the connection menu.
        2) Click Sync Button on the list.
        3) Orders, Customers and Products will be Imported from WooCommerce to Odoo.
        Data will be displayed on the WooCommerce Connector App as well as the odoo modules.
        
        More updates will be pushed frequently. Contributors are invited and appreciated.
        This is a free module and for more information contact on WhatsApp +923340239555.
    """,
    'author': "Saad Mujeeb - ISAA TECH",
    'website': "https://www.isaatech.com",
    'category': 'Connectors',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': [],
    'images': ['static/description/banner.png'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/views.xml',
        'views/orders.xml',
        'views/products.xml',
        'views/customers.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}

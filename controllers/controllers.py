# -*- coding: utf-8 -*-
# from odoo import http


# class WoocommerceConnector(http.Controller):
#     @http.route('/woocommerce_connector/woocommerce_connector/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/woocommerce_connector/woocommerce_connector/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('woocommerce_connector.listing', {
#             'root': '/woocommerce_connector/woocommerce_connector',
#             'objects': http.request.env['woocommerce_connector.woocommerce_connector'].search([]),
#         })

#     @http.route('/woocommerce_connector/woocommerce_connector/objects/<model("woocommerce_connector.woocommerce_connector"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('woocommerce_connector.object', {
#             'object': obj
#         })

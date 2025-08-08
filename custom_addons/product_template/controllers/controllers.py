# -*- coding: utf-8 -*-
# from odoo import http


# class ProductTemplate(http.Controller):
#     @http.route('/product_template/product_template', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_template/product_template/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_template.listing', {
#             'root': '/product_template/product_template',
#             'objects': http.request.env['product_template.product_template'].search([]),
#         })

#     @http.route('/product_template/product_template/objects/<model("product_template.product_template"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_template.object', {
#             'object': obj
#         })


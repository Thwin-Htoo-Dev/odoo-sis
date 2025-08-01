# -*- coding: utf-8 -*-
# from odoo import http


# class CombineTwomodule(http.Controller):
#     @http.route('/combine_twomodule/combine_twomodule', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/combine_twomodule/combine_twomodule/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('combine_twomodule.listing', {
#             'root': '/combine_twomodule/combine_twomodule',
#             'objects': http.request.env['combine_twomodule.combine_twomodule'].search([]),
#         })

#     @http.route('/combine_twomodule/combine_twomodule/objects/<model("combine_twomodule.combine_twomodule"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('combine_twomodule.object', {
#             'object': obj
#         })


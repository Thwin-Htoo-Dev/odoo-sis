# -*- coding: utf-8 -*-
# from odoo import http


# class MajorManagement(http.Controller):
#     @http.route('/major__management/major__management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/major__management/major__management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('major__management.listing', {
#             'root': '/major__management/major__management',
#             'objects': http.request.env['major__management.major__management'].search([]),
#         })

#     @http.route('/major__management/major__management/objects/<model("major__management.major__management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('major__management.object', {
#             'object': obj
#         })


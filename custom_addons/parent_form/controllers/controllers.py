# -*- coding: utf-8 -*-
# from odoo import http


# class ParentForm(http.Controller):
#     @http.route('/parent_form/parent_form', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parent_form/parent_form/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('parent_form.listing', {
#             'root': '/parent_form/parent_form',
#             'objects': http.request.env['parent_form.parent_form'].search([]),
#         })

#     @http.route('/parent_form/parent_form/objects/<model("parent_form.parent_form"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parent_form.object', {
#             'object': obj
#         })


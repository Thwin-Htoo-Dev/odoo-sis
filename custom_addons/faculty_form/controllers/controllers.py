# -*- coding: utf-8 -*-
# from odoo import http


# class FacultyForm(http.Controller):
#     @http.route('/faculty_form/faculty_form', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/faculty_form/faculty_form/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('faculty_form.listing', {
#             'root': '/faculty_form/faculty_form',
#             'objects': http.request.env['faculty_form.faculty_form'].search([]),
#         })

#     @http.route('/faculty_form/faculty_form/objects/<model("faculty_form.faculty_form"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('faculty_form.object', {
#             'object': obj
#         })


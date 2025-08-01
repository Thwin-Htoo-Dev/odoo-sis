# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAddons/facultyQualification(http.Controller):
#     @http.route('/custom_addons/faculty_qualification/custom_addons/faculty_qualification', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_addons/faculty_qualification/custom_addons/faculty_qualification/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_addons/faculty_qualification.listing', {
#             'root': '/custom_addons/faculty_qualification/custom_addons/faculty_qualification',
#             'objects': http.request.env['custom_addons/faculty_qualification.custom_addons/faculty_qualification'].search([]),
#         })

#     @http.route('/custom_addons/faculty_qualification/custom_addons/faculty_qualification/objects/<model("custom_addons/faculty_qualification.custom_addons/faculty_qualification"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_addons/faculty_qualification.object', {
#             'object': obj
#         })


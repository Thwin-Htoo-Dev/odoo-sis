# -*- coding: utf-8 -*-
# from odoo import http


# class CourseInvoices(http.Controller):
#     @http.route('/course_invoices/course_invoices', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/course_invoices/course_invoices/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('course_invoices.listing', {
#             'root': '/course_invoices/course_invoices',
#             'objects': http.request.env['course_invoices.course_invoices'].search([]),
#         })

#     @http.route('/course_invoices/course_invoices/objects/<model("course_invoices.course_invoices"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('course_invoices.object', {
#             'object': obj
#         })


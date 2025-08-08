from odoo import models, fields

class SisCourse(models.Model):
    _name = 'sis.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    code = fields.Char(string='Course Code')
    price = fields.Float(string='Course Price')
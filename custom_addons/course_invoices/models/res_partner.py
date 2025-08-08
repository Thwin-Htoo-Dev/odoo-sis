from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    course_id = fields.Many2one('sis.course', string="Course")

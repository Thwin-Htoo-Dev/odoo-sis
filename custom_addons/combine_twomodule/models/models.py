from odoo import models, fields

class Faculty(models.Model):
    _inherit = 'op.faculty'  # Inherit OpenEduCat Faculty model

    major_id = fields.Many2one('course.major', string='Major')

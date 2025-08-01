from odoo import models, fields

class Faculty(models.Model):
    _inherit = 'op.faculty'

    custom_note = fields.Char(string="Custom Note")
    emp_id = fields.Many2one('hr.employee',string='HR Employee',invisible=True)
    visa_info = fields.Char(string="Visa Info",invisible=True)
    mobile = fields.Char(string="Mobile", invisible=True)

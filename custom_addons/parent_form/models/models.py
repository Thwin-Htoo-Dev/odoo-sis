from odoo import models, fields

class OpParent(models.Model):
    _inherit = 'op.parent'

    mobile = fields.Char(string='Mobile', readonly=False)
   

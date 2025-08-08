from odoo import fields,models,api

class Product(models.Model):
    _inherit = 'product.template'

    name = fields.Char("Name", index="trigram", required=True, translate=True, default="Product")

    course_name = fields.Many2one('op.course',string='Product',required=True)
    @api.onchange('course_name')
    def _onchange_course_name(self):
        if self.course_name:
            self.name = self.course_name.name

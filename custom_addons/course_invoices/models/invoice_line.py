from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    course_id = fields.Many2one('sis.course', string="Course")

    @api.onchange('course_id')
    def _onchange_course_id(self):
        for line in self:
            if line.course_id:
                line.name = line.course_id.name
                line.price_unit = line.course_id.price
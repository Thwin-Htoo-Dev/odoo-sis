from odoo import models, fields, api


class Faculty(models.Model):
    _inherit = "op.faculty"  # Inherit OpenEduCat Faculty model

    major_id = fields.Many2one("course.major", string="Major")


# class ProductTemplate(models.Model):
#     _inherit = "product.template"

#     name = fields.Char(
#         "Name", index="trigram", required=True, translate=True, default="Name"
#     )

#     course_name = fields.Many2one("op.course", string="Course Name")

#     @api.depends("course_name")
#     def _compute_display_name(self):
#         for rec in self:
#             if rec.course_name:
#                 rec.display_name = rec.course_name.name

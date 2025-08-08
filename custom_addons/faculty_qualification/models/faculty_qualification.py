from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.osv import expression
import logging
_logger = logging.getLogger(__name__)

class FacultyQualification(models.Model):
    _name = 'sis.faculty.qualification'
    _description = 'Faculty Qualification'

    name = fields.Char("Qualification Name", required=True)
    qualification_code = fields.Char("Qualification Code", readonly=True, copy=False)
    level = fields.Selection([
        ('မန္တလေးတက္ကသိုလ်', 'မန္တလေးတက္ကသိုလ်'),
        ( 'ဒဂုံတက္ကသိုလ်', 'ဒဂုံတက္ကသိုလ်'),
        ('ရန်ကုန်တက္ကသိုလ်', 'ရန်ကုန်တက္ကသိုလ်'),
        ('ပဲခူးတက္ကသိုလ်', 'ပဲခူးတက္ကသိုလ်'),
        ('ဟင်္သာတတက္ကသိုလ်', 'ဟင်္သာတတက္ကသိုလ်'),
    ], string="University", required=True)
    university_text = fields.Char("University Text", compute="_compute_university_text", store=True)
    field_of_study = fields.Char("Field of Study")
    institution_name = fields.Char("Institution Name")
    country_id = fields.Many2one('res.country', string="Country")
    start_date = fields.Date("Start Date")
    end_date = fields.Date("End Date")
    grade = fields.Char("Grade/Score")
    certificate_file = fields.Binary("Document Upload")
    certificate_filename = fields.Char("File Name")
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], string="Status", default="active")
    remarks = fields.Text("Remarks/Notes")

    @api.depends('level')
    def _compute_university_text(self):
        for rec in self:
            rec.university_text = rec.level or ''

    @api.model
    def create(self, vals):
        if not vals.get('qualification_code'):
            vals['qualification_code'] = self.env['ir.sequence'].next_by_code('sis.faculty.qualification') or 'QUAL0000'
        return super().create(vals)

    @api.constrains('start_date', 'end_date')
    def _check_date_range(self):
        for record in self:
            if record.start_date and record.end_date and record.end_date < record.start_date:
                raise ValidationError("End Date cannot be earlier than Start Date.")
            
    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        domain = expression.OR([
            [('name', operator, name)],
            [('qualification_code', operator, name)],
            [('university_text', operator, name)],
            [('institution_name', operator, name)]
        ])
        records = self.search(expression.AND([args, domain]), limit=limit)
        return records.name_get()

    def name_get(self):
        return [(rec.id, f"{rec.qualification_code or ''} - {rec.name or ''}") for rec in self]
    
    def print_report(self):
        return self.env.ref('faculty_qualification.report_faculty_qualification').report_action(self)
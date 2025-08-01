# from odoo import models, fields, api


# class CourseMajor(models.Model):
#     _name = "course.major"
#     _description = "Course Major"

#     name = fields.Char("Major Name", required=True)
#     code = fields.Char("Code", readonly=True)
#     description = fields.Text("Description")
#     image = fields.Image("Image")

#     schedule_ids = fields.One2many(
#         "major.schedule",
#         "major_id",
#         string="Schedules",
#         ondelete="cascade"  # THIS ENSURES schedules are deleted when major is deleted
#     )

#     subject_list = fields.Char(string="Subject(s)", compute="_compute_subject_list", store=True)

#     @api.depends('schedule_ids.subject')
#     def _compute_subject_list(self):
#         for record in self:
#             subjects = list(set(
#                 dict(self.env['major.schedule'].fields_get(allfields=['subject'])['subject']['selection'])[s.subject]
#                 for s in record.schedule_ids if s.subject
#             ))
#             record.subject_list = ", ".join(subjects)

#     @api.model
#     def create(self, vals):
#         if not vals.get("code") and vals.get("name"):
#             base_code = "".join(word[0] for word in vals["name"].split()).upper()
#             existing = self.search_count([("code", "ilike", base_code + "%")])
#             vals["code"] = f"{base_code}-{existing + 1:02d}"
#         return super().create(vals)


# class MajorSchedule(models.Model):
#     _name = "major.schedule"
#     _description = "Major Schedule"

#     instructor_id = fields.Many2one(
#         "op.faculty",
#         string="Instructor",
#         required=False,  # must be optional if ondelete='set null'
#         ondelete="set null"  # Prevent error when instructor is deleted
#     )

#     major_id = fields.Many2one(
#         "course.major",
#         string="Major",
#         required=True,
#         ondelete="cascade"  # Delete schedule if major is deleted
#     )


#     subject = fields.Selection(
#         [
#             ("myanmar", "Myanmar"),
#             ("english", "English"),
#             ("math", "Math"),
#             ("chemistry", "Chemistry"),
#             ("physics", "Physics"),
#             ("biology", "Biology"),
#         ],
#         string="Subject",
#         required=True,
#     )

from odoo import models, fields, api


class CourseMajor(models.Model):
    _name = "course.major"
    _description = "Course Major"

    name = fields.Char("Major Name", required=True)
    code = fields.Char("Code", readonly=True)
    description = fields.Text("Description")
    image = fields.Image("Image")

    schedule_ids = fields.One2many(
        "major.schedule",
        "major_id",
        string="Schedules",
        ondelete="cascade"
    )

    subject_list = fields.Char(string="Subject(s)", compute="_compute_subject_list", store=True)

    @api.depends('schedule_ids.subject')
    def _compute_subject_list(self):
        for record in self:
            subject_names = list({s.subject.name for s in record.schedule_ids if s.subject})
            record.subject_list = ", ".join(subject_names)

    @api.model
    def create(self, vals):
        if not vals.get("code") and vals.get("name"):
            base_code = "".join(word[0] for word in vals["name"].split()).upper()
            existing = self.search_count([("code", "ilike", base_code + "%")])
            vals["code"] = f"{base_code}-{existing + 1:02d}"
        return super().create(vals)


class MajorSchedule(models.Model):
    _name = "major.schedule"
    _description = "Major Schedule"

    instructor_id = fields.Many2one(
        "op.faculty",
        string="Instructor",
        ondelete="set null"
    )

    major_id = fields.Many2one(
        "course.major",
        string="Major",
        required=True,
        ondelete="cascade"
    )

    subject = fields.Many2one(
        "op.subject",
        string="Subject",
        required=True
    )

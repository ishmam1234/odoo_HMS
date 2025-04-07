from odoo import api, models, fields
from datetime import date


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit=['mail.thread']
    _description = 'Patient Master'

    name = fields.Char(
        string="Name", required=True, tracking=True
    )
    date_of_birth = fields.Date(string="Date of Birth")

    age = fields.Integer(string="Age", compute="_compute_age")

    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                today = date.today()
                rec.age = today.year - rec.date_of_birth.year - (
                        (today.month, today.day) < (rec.date_of_birth.month, rec.date_of_birth.day)
                )
            else:
                rec.age = 0

    description = fields.Text(string="Description")
    gender = fields.Selection(
        [('male','Male'), ('female', 'Female')],
        string="Gender"
    )

    tag_ids = fields.Many2many(
        'patient.tag', 'patient_tag_rel', 'patient_id', 'tag_id', string="Tags"
    )

    product_ids = fields.Many2many(
        'product.product',string="Products"
    )


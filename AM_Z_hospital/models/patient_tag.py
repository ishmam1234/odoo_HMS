from email.policy import default

from odoo import api, models, fields


class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'
    _order = 'sequence,id'
    name = fields.Char(
        string="Name", required=True
    )
    sequence = fields.Integer(default=10)
    # date_of_birth = fields.Date(string="Date of Birth")
    # description = fields.Text(string="Description")
    # gender = fields.Selection(
    #     [('male','Male'), ('female', 'Female')],
    #     string="Gender")



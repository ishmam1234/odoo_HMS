from odoo import api, models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit=['mail.thread']
    _description = 'Patient Master'

    name = fields.Char(
        string="Name", required=True, tracking=True
    )
    date_of_birth = fields.Date(string="Date of Birth")
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


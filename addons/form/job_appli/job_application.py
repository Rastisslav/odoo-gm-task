from odoo import models, fields, api

class JobApplication(models.Model):
    _name = 'job.application'
    _description = 'Job Application Form'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone')
    introduction = fields.Text(string='Short Introduction')
    cv = fields.Binary(string='CV')

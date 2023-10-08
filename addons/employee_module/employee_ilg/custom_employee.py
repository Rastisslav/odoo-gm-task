from odoo import models, fields, api

class HREmployee(models.Model):
    _inherit = "hr.employee"

    i_love_gb = fields.Boolean(string="I love GymBeam")
    salary = fields.Integer(string="Salary")
    tax = fields.Integer(string="Tax")
    total_salary = fields.Integer(string='Total Salary', compute='_compute_total_salary', store=True)

    @api.depends('salary', 'tax')
    def _compute_total_salary(self):
        for employee in self:
            employee.total_salary = employee.salary + employee.tax
    
    special_phone = fields.Char(string='Special Phone', default='0901123456', required=True)

    
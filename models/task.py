from odoo import models, fields

class Task(models.Model):
    _name='task.manager'
    _description = 'Task Manager'

    name= fields.Char(string='Task Name', required=True)
    description= fields.Text(string='Description')
    deadline= fields.Date(string='Deadline')
    priority=fields.Selection([
        ('low','Low'),
        ('medium','Medium'),
        ('high','High')
    ],string='Priority', default='low')
    done = fields.Boolean(string='Done',defualt=False)
    assigned_to=fields.Many2one('res.users',string='Assigned To')

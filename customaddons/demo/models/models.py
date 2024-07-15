# -*- coding: utf-8 -*-

from odoo import models, fields, api

class demo(models.Model):    
    
    _name = 'demo.demo'
    _description = 'demo.demooooooooo'

    Fruit_name = fields.Char()
    value = fields.Integer()
    description = fields.Text()




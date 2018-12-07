# -*- coding: utf-8 -*-

from odoo import api, fields, models

class training_subject(Models.model):
    
    _name = 'training.subject'
    _rec_name = 'name'
    
    name = fields.Char(u'名称',
                      size=64,
                      default=u'默认科目')
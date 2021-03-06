# -*- coding: utf-8 -*-
 from openerp.osv import fields, osv
 
 class test1_lesson(osv.osv):
     _name = 'test1.lesson'
     _discription = 'test1 demo'
     _columns = {
        'name':fields.Char( u'课程名',size=64,select=True),
        'date_start':fields.date(u'开始日期',select=True),
        'total_day':fields.float(u'总天数',digits=(16,1)),
        'teacher':fields.many2one('res.users',u'授课老师'),
        'students':fields.many2many('res.partner',string=u'学生'),
        'price':fields.float(u'价格',digits=(16,2)),
         }
 test1_lesson()
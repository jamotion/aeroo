# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2014 Therp BV (<http://therp.nl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv.orm import Model
from openerp.osv import fields

class Report(Model):
    _inherit = 'report'

    def _get_replacing_report(self, cr, report_name):
        cr.execute('''
        select report_replace.report_name
        from ir_act_report_xml report_org
            join ir_act_report_xml report_replace
            on report_org.id = report_replace.replace_report_id
        where report_org.report_name=%s''', (report_name,))
        new_report_name = report_name
        for name, in cr.fetchall():
            new_report_name = name
        return new_report_name

    def get_action(self, cr, uid, ids, report_name, datas=None, context=None):
        return super(Report, self).get_action(
            cr, uid, ids,
            self._get_replacing_report(cr, report_name), datas=datas, context=context)

# -*- coding: utf-8 -*-
# LICENSE

from openerp.osv import fields, osv
from openerp.tools.translate import

class res.partner(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _colum= {
        "hola": fields.boolean('hola'),
    }
    res.partner()
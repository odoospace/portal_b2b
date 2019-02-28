# -*- coding: utf-8 -*-

from openerp import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _get_partner_id(self):
        if self.env.user.has_group('base.group_portal'):
            return self.env.user.partner_id
    
    partner_id = fields.Many2one(
        'res.partner', string='Customer', readonly=True,
        default=_get_partner_id,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True,
        track_visibility='always')

"""
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_portal = fields.Boolean()
"""
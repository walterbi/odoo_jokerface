# -*- coding: utf-8 -*-

from odoo import fields, api, models


class ProductAvailability(models.Model):

    _inherit = "product.template"

    availability = fields.Selection(selection_add=[('out_of_stock', 'Out of Stock')])

    @api.multi
    def default_availability(self):
        stock_product_change = self.env['stock.change.product.qty'].search([('product_id', '=', self.id)])
        on_hand = len(stock_product_change)
        if on_hand == 0:
            self.availability = 'out_of_stock'
            # test abc

# -*- coding: utf-8 -*-

from odoo import fields, api, models


class ProductAvailability(models.Model):

    _inherit = "product.template"

    availability = fields.Selection(selection_add=[('out_of_stock', 'Out of Stock')])

    @api.model
    def default_availability(self):

        stock_product_change = self.env['stock.change.product.qty'].search([(
            'product_id', '=', self.product_id,
        )])
        print stock_product_change
        print "break point here"

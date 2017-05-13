# -*- coding: utf-8 -*-

from odoo import fields, api, models


class ProductAvailability(models.Model):

    _inherit = "product.template"

    availability = fields.Selection(selection_add=[('out_of_stock', 'Out of Stock')])
    description_sale = fields.Html('Description Quotations')
    is_shirt = fields.Boolean('Checking T-Shirt product', default=False, compute="_compute_shirt")

    @api.multi
    def default_availability(self):
        stock_product_change = self.env['stock.change.product.qty'].search([('product_id', '=', self.id)])
        on_hand = len(stock_product_change)
        if on_hand == 0:
            self.availability = 'out_of_stock'

    @api.depends()
    def _compute_shirt(self):
        if u"Áo Thun" in self.categ_id.name:
            self.is_shirt = True
            print "Is Shirt"

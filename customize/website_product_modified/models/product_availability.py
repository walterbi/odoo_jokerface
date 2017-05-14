# -*- coding: utf-8 -*-

from odoo import fields, api, models


class ProductAvailability(models.Model):

    _inherit = "product.template"

    availability = fields.Selection(selection_add=[('out_of_stock', 'Out of Stock')],
                                    default="out_of_stock",
                                    compute="_default_availability")
    description_sale = fields.Html('Description Quotations')
    is_shirt = fields.Boolean('Checking T-Shirt product', default=False, compute="_compute_shirt", store=True)

    @api.depends()
    def _default_availability(self):
        if len(self) > 1:
            for item in self:
                stock_qty = item.env["stock.quant"].search([('product_id', '=', item.id)])
                item_qty = stock_qty.qty
                if item_qty > 0:
                    item.availability = "in_stock"
        else:
            stock_qty = self.env["stock.quant"].search([('product_id', '=', self.id)])
            if len(stock_qty) == 0:
                self.availability = "out_of_stock"
            else:
                for item in stock_qty:
                    if item.qty > 0:
                        self.availability = "in_stock"
                    else:
                        self.availability = "out_of_stock"

    @api.depends()
    def _compute_shirt(self):
        if len(self) > 1:
            for item in self:
                if u"Áo Thun" in item.categ_id.name:
                    item.is_shirt = True
        else:
            if u"Áo Thun" in self.categ_id.name:
                self.is_shirt = True

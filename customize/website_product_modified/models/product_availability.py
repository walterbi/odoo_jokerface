# -*- coding: utf-8 -*-

from odoo import fields, api, models
import unicodedata


class ProductAvailability(models.Model):

    _inherit = "product.template"

    availability = fields.Selection(selection_add=[('out_of_stock', 'Out of Stock')],
                                    default="out_of_stock",
                                    compute="_default_availability", store=True)
    description_sale = fields.Html('Description Quotations', default="")
    is_shirt = fields.Boolean('Checking T-Shirt product', default=False, compute="_compute_shirt", store=True)
    ascii_name = fields.Char('ASCII name for products', default="", compute="_compute_ascii_name", store=True)
    ascii_description_sale = fields.Char('ASCII description sale for products', default="", store=True)

    @api.depends("qty_available")
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

    @api.depends("name")
    def _compute_shirt(self):
        if len(self) > 1:
            for item in self:
                if u"Áo Thun" in item.categ_id.name:
                    item.is_shirt = True
        else:
            if u"Áo Thun" in self.categ_id.name:
                self.is_shirt = True

    @api.depends("name")
    def _compute_ascii_name(self):
        if self.name:
            if len(self) > 1:
                for item in self:
                    item.ascii_name = unicodedata.normalize('NFKD', item.name).encode('ascii', 'ignore')
            else:
                self.ascii_name = unicodedata.normalize('NFKD', self.name).encode('ascii', 'ignore')

    @api.depends("description_sale")
    def _compute_ascii_name(self):
        if not self.description_sale:
            self.description_sale = u""
        if self.description_sale:
            if len(self) > 1:
                for item in self:
                    item.ascii_description_sale = unicodedata.normalize('NFKD', item.description_sale).encode(
                        'ascii', 'ignore')
            else:
                self.ascii_description_sale = unicodedata.normalize('NFKD', self.description_sale).encode('ascii', 'ignore')

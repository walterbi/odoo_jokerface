# -*- coding:utf-8 -*-

from odoo import api, fields, models


class ProductFeatureAdditional(models.Model):
    _inherit = "product.product"

    @api.model
    def create(self, vals):
        res = super(ProductFeatureAdditional, self).create(vals)
        product_id = res.id
        print res.product_variant_id
        print "break"

        return res

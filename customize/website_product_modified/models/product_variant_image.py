# -*- coding: utf-8 -*-
from odoo import models, api, fields


class ProductVariantImage(models.Model):
    _inherit = "product.image"

    variants = fields.Many2one("product.attribute.value")

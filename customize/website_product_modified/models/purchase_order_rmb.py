# -*- coding:utf-8 -*-

from odoo import api, models, fields


class PurchaseOrderRmb(models.Model):
    _inherit = "purchase.order.line"

    x_rmb = fields.Monetary(string="RMB")
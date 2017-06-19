# -*- coding: utf-8 -*-

from odoo import api, models, fields


class DeliveryConnector(models.Model):
    _name = "delivery.connector"
    _description = 'Delivery Acquirer'
    _order = 'sequence'

    name = fields.Char(string="Delivery Partner")

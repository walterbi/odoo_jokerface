# -*- coding: utf-8 -*-

from odoo import api, fields, models


class GHNConnector(models.Model):
    _name = "ghn.connector"

    name = fields.Char()

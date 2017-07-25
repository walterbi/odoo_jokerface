# -*- coding: utf-8 -*-

from odoo import api, models, fields


class CardInformation(models.Model):
    _name = "card.information"

    user_info = fields.Many2one("membership.information")
    name = fields.Char(string="Mã số thẻ")
    type = fields.Char(string="Loại thẻ")

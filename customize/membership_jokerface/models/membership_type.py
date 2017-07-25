# -*- coding: utf-8 -*-

from odoo import api, models, fields


class MembershipType(models.Model):
    _name = "membership.type"

    name = fields.Char(string="Loại thành viên")
    discount = fields.Float(string="Giảm giá (%)")
    saved_percent = fields.Float(string="Phần trăm tích điểm")

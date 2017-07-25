# -*- coding: utf-8 -*-

from odoo import api, models, fields


class MembershipInformation(models.Model):
    _name = "membership.information"

    name = fields.Char(string="Chủ sở hữu")
    related_user = fields.Many2one("res.partner", required=True)
    earn_point = fields.Integer(string="Điểm tích luỹ")
    used_point = fields.Integer(string="Điểm đã sử dụng")
    type = fields.Many2one("membership.type")
    card_id = fields.Many2one("card.information")

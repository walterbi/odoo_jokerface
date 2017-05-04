# -*- coding: utf-8 -*-

from odoo import api, fields, models


class UserAdditionalInfo(models.Model):

    _inherit = "res.users"

    # Basic information
    gender = fields.Char(string="Users Gender")
    birthday = fields.Date(string="Users Birthday")
    status = fields.Integer(string="Users Status")
    level = fields.Integer(string="Users Level")
    point = fields.Integer(string="Users Point to Use")

    # Expanding information
    verified_email = fields.Boolean(string="Checking email verified")
    verified_phone = fields.Boolean(string="Checking phone verified")

class UserPartnerInfo(models.Model):

    _inherit = "res.partner"

    birthday = fields.Date(string="Users Birthday")
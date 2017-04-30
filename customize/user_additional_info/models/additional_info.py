# -*- coding: utf-8 -*-

from odoo import api, fields, models


class UserAdditionalInfo(models.Model):

    _inherit = "res.users"

    # Basic information
    gender = fields.Char(string="Users Gender", required=True)
    birthday = fields.Date(string="Users Birthday", required=True)
    status = fields.Integer(string="Users Status")
    level = fields.Integer(string="Users Level")
    point = fields.Integer(string="Users Point to Use")

    # Expanding information
    verified_email = fields.Boolean(string="Checking email verified")
    verified_phone = fields.Boolean(string="Checking phone verified")

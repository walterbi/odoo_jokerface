# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError
import requests, json


class DeliveryConnector(models.Model):
    _name = "delivery.connector"
    _description = 'Delivery Acquirer'

    name = fields.Char(string="Vendor")
    api_key = fields.Char(string="API Key")
    api_secret = fields.Char(string="API Secret")
    client_id = fields.Char(string="Client ID")
    client_pwd = fields.Char(string="Password")

    @api.multi
    def test_api(self):
        url_services = "https://testapipds.ghn.vn:9999/external/b2c/"
        parameters = {
            "ApiKey": str(self.api_key),
            "ApiSecretKey": str(self.api_secret),
            "ClientID": int(self.client_id),
            "Password": str(self.client_pwd),
        }

        res = requests.post(url_services + "Signin", json=parameters)
        if res.json().get("ErrorMessage") is None:
            raise UserError(_("Connection successful"))
        else:
            raise UserError(_("Connection failed"))

# -*- coding: utf-8 -*-

from odoo import http, tools, _
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.website.models.website import slug
from odoo.addons.website.controllers.main import QueryURL
from odoo.http import request


class WebsiteSaleProduct(WebsiteSale):
    def _get_search_order(self, post):
        return 'is_shirt asc, availability desc, write_date desc'

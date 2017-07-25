# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http, _
from odoo.exceptions import AccessError
from odoo.http import request

from odoo.addons.website_portal.controllers.main import website_account


class website_account(website_account):

    @http.route("/my/membership", type='http', auth="user", website=True)
    def portal_my_membership(self, date_begin=None, date_end=None, **kw):
        membership = request.env['membership.information'].search([('related_user', '=', request.env.user.id)])

        values = ({
            'user': request.env.user,
            'membership': membership,
            'default_url': "/my/membership",
        })
        print membership.name
        return request.render("membership_jokerface.portal_my_membership", values)

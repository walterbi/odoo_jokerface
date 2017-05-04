# -*- coding: utf-8 -*-

from odoo import http, _
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.addons.website_portal.controllers.main import website_account


class UserAdditionalInfo(AuthSignupHome):

    def do_signup(self, qcontext):
        """ Shared helper that creates a res.partner out of a token """
        print "are you right now???"
        values = { key: qcontext.get(key) for key in ('login', 'name', 'password', 'phone', 'street', 'birthday') }
        assert values.values(), "The form was not properly filled in."
        assert values.get('password') == qcontext.get('confirm_password'), "Passwords do not match; please retype them."
        supported_langs = [lang['code'] for lang in request.env['res.lang'].sudo().search_read([], ['code'])]
        if request.lang in supported_langs:
            values['lang'] = request.lang
        self._signup_with_values(qcontext.get('token'), values)
        request.env.cr.commit()

class WebsiteAccount(website_account):

    @http.route()
    def details(self, redirect=None, **post):
        self.MANDATORY_BILLING_FIELDS.append("birthday")
        res = super(WebsiteAccount, self).details(redirect=None, **post)
        return res

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http, _
from odoo.exceptions import AccessError
from odoo.http import request

from odoo.addons.website_portal.controllers.main import website_account
from odoo.addons.website_sale.controllers.main import WebsiteSale


class website_account(website_account):
    @http.route("/my/membership", type='http', auth="user", website=True)
    def portal_my_membership(self, date_begin=None, date_end=None, **kw):
        partner_id = request.env['res.users'].search([('id', '=', request.env.user.id)])
        if partner_id:
            membership = request.env['membership.information'].search([('related_user', '=', partner_id.partner_id.id)])

        values = ({
            'user': request.env.user,
            'membership': membership,
            'default_url': "/my/membership",
        })
        # print membership.type
        return request.render("membership_jokerface.portal_my_membership", values)


class WebsiteSale(WebsiteSale):
    @http.route(['/shop/payment'], type='http', auth="public", website=True)
    def payment(self, **post):
        
        sale_order = request.env['sale.order']

        order = request.website.sale_get_order()

        redirection = self.checkout_redirection(order)
        if redirection:
            return redirection

        shipping_partner_id = False
        if order:
            if order.partner_shipping_id.id:
                shipping_partner_id = order.partner_shipping_id.id
            else:
                shipping_partner_id = order.partner_invoice_id.id

        values = {
            'website_sale_order': order
        }
        values['errors'] = sale_order._get_errors(order)
        values.update(sale_order._get_website_data(order))
        if not values['errors']:
            acquirers = request.env['payment.acquirer'].search(
                [('website_published', '=', True), ('company_id', '=', order.company_id.id)]
            )
            values['acquirers'] = []
            for acquirer in acquirers:
                acquirer_button = acquirer.with_context(submit_class='btn btn-primary',
                                                        submit_txt=_('Pay Now')).sudo().render(
                    '/',
                    order.amount_total,
                    order.pricelist_id.currency_id.id,
                    values={
                        'return_url': '/shop/payment/validate',
                        'partner_id': shipping_partner_id,
                        'billing_partner_id': order.partner_invoice_id.id,
                    }
                )
                acquirer.button = acquirer_button
                values['acquirers'].append(acquirer)

            values['tokens'] = request.env['payment.token'].search(
                [('partner_id', '=', order.partner_id.id), ('acquirer_id', 'in', acquirers.ids)])

            partner_id = request.env['res.users'].search([('id', '=', request.env.user.id)])
            if partner_id:
                membership = request.env['membership.information'].search(
                    [('related_user', '=', partner_id.partner_id.id)])
                values.update({
                    'membership': membership,
                })
                membership_settings = request.env['membership.type'].search([('id', '=', membership.type.id)])
                percent_save = membership_settings.saved_percent
                values['point_saving'] = (percent_save * order.amount_total / 100) / 1000

        return request.render("website_sale.payment", values)

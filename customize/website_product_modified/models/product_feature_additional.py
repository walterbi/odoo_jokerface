# -*- coding:utf-8 -*-

from odoo import api, fields, models

MAX_CODE_LENGTH = 4
MAX_VARIANT_LENGTH = 3
DEFAULT_FIRST_DIGIT = 9


class ProductFeatureAdditional(models.Model):
    _inherit = "product.template"

    # @api.onchange('name')
    # def _compute_default_code(self):
    #     _default_code = self.default_code
    #     if not _default_code:
    #         _default_code = str(DEFAULT_FIRST_DIGIT)
    #         # Request the latest product id
    #         res = self.env['product.template'].search([])
    #         latest_id = max(res.ids)
    #
    #         for i in range(MAX_CODE_LENGTH - len(str(latest_id))):
    #             _default_code += '0'
    #         _default_code += str(latest_id)
    #         self.default_code = _default_code + '-000'
    #         self.barcode = _default_code+ '-000'

    @api.model
    def create(self, vals):
        _default_code = self.default_code
        if not _default_code:
            _default_code = str(DEFAULT_FIRST_DIGIT)

            # Request the latest product id
            _res = self.env['product.template'].search([])
            latest_id = max(_res.ids) + 1
            for i in range(MAX_CODE_LENGTH - len(str(latest_id))):
                _default_code += '0'
            _default_code += str(latest_id)
            vals.update({
                'default_code': _default_code + '-000',
                'barcode': _default_code + '-000',
            })
        res = super(ProductFeatureAdditional, self).create(vals)

        # Get product_template information
        tmpl_default_code = res.default_code

        product_product = self.env['product.product'].search([('product_tmpl_id', '=', res.id)])

        # Compute default code for variants
        variant_count = 0
        for item_product_product in product_product:
            if not item_product_product.default_code:
                product_default_code = tmpl_default_code.split("-")[0] + '-' + '0' * (
                    MAX_VARIANT_LENGTH - len(str(variant_count))) + str(variant_count)

                item_product_product.default_code = product_default_code
                item_product_product.barcode = product_default_code
            variant_count += 1

        return res

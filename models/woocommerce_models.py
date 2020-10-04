
from odoo import models, fields, api, _


class woocommerce_orders(models.Model):
    _name = 'woocommerce.orders'
    _description = 'woocommerce.orders'

    order_seq = fields.Char(string='Order Seq', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    order_id = fields.Integer(string='ID')
    parent_id = fields.Integer()
    number = fields.Integer()
    order_key = fields.Char()
    created_via = fields.Char()
    version = fields.Char()
    status = fields.Char()
    currency = fields.Char()
    date_created = fields.Char()
    date_created_gmt = fields.Char()
    date_modified = fields.Char()
    date_modified_gmt = fields.Char()
    discount_total = fields.Char()
    discount_tax = fields.Char()
    shipping_total = fields.Char()
    shipping_tax = fields.Char()
    cart_tax = fields.Char()
    total = fields.Char()
    total_tax = fields.Char()
    prices_include_tax = fields.Char()
    customer_id = fields.Char()
    customer_ip_address = fields.Char()
    customer_user_agent = fields.Char()
    customer_note = fields.Char()
    payment_method = fields.Char()
    payment_method_title = fields.Char()
    transaction_id = fields.Char()
    date_paid = fields.Char()
    date_paid_gmt = fields.Char()
    date_completed = fields.Char()
    date_completed_gmt = fields.Char()
    cart_hash = fields.Char()
    # billing_id = fields.Many2one('woocommerce.orders.billing', string='Billing', required=False)

    @api.model
    def create(self, vals):
        existing_records = self.env['woocommerce.orders'].search([('order_id', '=', vals['order_id'])])
        if len(existing_records) >= 1:
            print('Field value must be unique')
            # raise Warning('Field value must be unique')
        else:
            if vals.get('order_seq', _('New')) == _('New'):
                vals['order_seq'] = self.env['ir.sequence'].next_by_code('woocommerce.orders.sequence') or _('New')
            result = super(woocommerce_orders, self).create(vals)
            return result


class woocommerce_orders_billing(models.Model):
    _name = 'woocommerce.orders.billing'
    _description = 'woocommerce.orders.billing'

    # billing_id = fields.Integer()
    first_name = fields.Char()
    last_name = fields.Char()
    company = fields.Char()
    address_1 = fields.Char()
    address_2 = fields.Char()
    city = fields.Char()
    state = fields.Char()
    postcode = fields.Char()
    country = fields.Char()
    email = fields.Char()
    phone = fields.Char()


class woocommerce_products(models.Model):
    _name = 'woocommerce.products'
    _description = 'woocommerce.products'

    product_seq = fields.Char(string='Product Seq', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    product_id = fields.Integer(string='ID')
    name = fields.Char()
    slug = fields.Char()
    permalink = fields.Char()
    date_created = fields.Char()
    date_created_gmt = fields.Char()
    date_modified = fields.Char()
    date_modified_gmt = fields.Char()
    type = fields.Char()
    status = fields.Char()
    featured = fields.Char()
    catalog_visibility = fields.Char()
    description = fields.Char()
    short_description = fields.Char()
    sku = fields.Char()
    price = fields.Char()
    regular_price = fields.Char()
    sale_price = fields.Char()
    date_on_sale_from = fields.Char()
    date_on_sale_from_gmt = fields.Char()
    date_on_sale_to = fields.Char()
    date_on_sale_to_gmt = fields.Char()
    price_html = fields.Char()
    on_sale = fields.Char()
    purchasable = fields.Char()
    total_sales = fields.Char()
    virtual = fields.Char()
    downloadable = fields.Char()
    downloads = fields.Char()
    download_limit = fields.Char()
    download_expiry = fields.Char()
    external_url = fields.Char()
    button_text = fields.Char()
    tax_status = fields.Char()
    tax_class = fields.Char()
    manage_stock = fields.Char()
    stock_quantity = fields.Char()
    stock_status = fields.Char()
    backorders = fields.Char()
    backorders_allowed = fields.Char()
    backordered = fields.Char()
    sold_individually = fields.Char()
    weight = fields.Char()
    shipping_required = fields.Char()
    shipping_taxable = fields.Char()
    shipping_class = fields.Char()
    shipping_class_id = fields.Char()
    reviews_allowed = fields.Char()
    average_rating = fields.Char()
    rating_count = fields.Char()
    parent_id = fields.Char()
    purchase_note = fields.Char()

    @api.model
    def create(self, vals):
        existing_records = self.env['woocommerce.products'].search([('product_id', '=', vals['product_id'])])
        if len(existing_records) >= 1:
            print('Field value must be unique')
            # raise Warning('Field value must be unique')
        else:
            if vals.get('product_seq', _('New')) == _('New'):
                vals['product_seq'] = self.env['ir.sequence'].next_by_code('woocommerce.products.sequence') or _('New')
            result = super(woocommerce_products, self).create(vals)
            return result


class woocommerce_customers(models.Model):
    _name = 'woocommerce.customers'
    _description = 'woocommerce.customers'

    customer_seq = fields.Char(string='Customer Seq', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    customer_id = fields.Integer(string='ID')
    date_created = fields.Char()
    date_created_gmt = fields.Char()
    date_modified = fields.Char()
    date_modified_gmt = fields.Char()
    email = fields.Char()
    first_name = fields.Char()
    last_name = fields.Char()
    role = fields.Char()
    username = fields.Char()
    city = fields.Char()
    country = fields.Char()
    phone = fields.Char()
    zip = fields.Char()
    street = fields.Char()
    street2 = fields.Char()
   
    @api.model
    def create(self, vals):
        existing_records = self.env['woocommerce.customers'].search([('customer_id', '=', vals['customer_id'])])
        if len(existing_records) >= 1:
            print('Field value must be unique')
            # raise Warning('Field value must be unique')
        else:
            if vals.get('customer_seq', _('New')) == _('New'):
                vals['customer_seq'] = self.env['ir.sequence'].next_by_code('woocommerce.customers.sequence') or _('New')
            result = super(woocommerce_customers, self).create(vals)
            return result

from odoo import fields, models


class AccountPayment(models.Model):
    _inherit = "account.payment"
    _order = "create_date"

    loan_id = fields.Many2one("account.loan", "Account Loan")
    partner_id = fields.Many2one("res.partner", "Payment Partner")

from odoo import fields, models


class AccountPayment(models.Model):
    _name = "coop.payment"
    _order = "create_date"

    loan_id = fields.Many2one("account.loan", "Account Loan", readonly=True)
    partner_id = fields.Many2one("res.partner", "Payment Partner")
    communication = fields.Char("Memo")
    payment_method = fields.Selection(
        [
            ("cashier", "Cashier"),
            ("transference", "Transference"),
            ("online", "Online"),
        ],
        "Method",
    )
    amount = fields.Float("Amount")

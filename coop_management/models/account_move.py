from odoo import fields, models


class AccountMoveLine(models.Model):
    _name = "account.account.move"
    _order = "create_date"

    type = fields.Selection(
        [
            ("own_accounts", "Between Own Accounts"),
            ("third_payments", "Third Payments"),
            ("other_bank", "Other Banks"),
        ]
    )
    account_id = fields.Many2one("account.account", "Account")
    account_dest_id = fields.Many2one("account.account", "Destination Account")
    debit_amount = fields.Float("Debit")
    credit_amount = fields.Float("Credit")
    balance = fields.Float("Balance")

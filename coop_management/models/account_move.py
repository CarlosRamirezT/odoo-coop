from odoo import fields, models


class AccountMoveLine(models.Model):
    _name = "coop.move"
    _order = "create_date"

    type = fields.Selection(
        [
            ("internal", "Internal"),
            ("own_accounts", "Between Own Accounts"),
            ("third_payments", "Third Payments"),
            ("other_bank", "Other Banks"),
        ]
    )
    account_id = fields.Many2one("account.account", "Account", required=True, readonly=True)
    account_dest_id = fields.Many2one("account.account", "Destination Account")
    debit_amount = fields.Float("Debit")
    credit_amount = fields.Float("Credit")
    balance = fields.Float("Balance", readonly=True)

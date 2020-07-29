from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    type = fields.Selection(
        [
            ("own_accounts", "Between Own Accounts"),
            ("third_payments", "Third Payments"),
            ("other_bank", "Other Banks"),
        ]
    )
    account_dest_id = fields.Many2one("account.account", "Destination Account")

from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _name = "coop.move"
    _order = "create_date"

    type = fields.Selection(
        [
            ("internal", "Internal"),
            ("own_accounts", "Between Own Accounts"),
            ("third_payments", "Third Payments"),
            ("other_bank", "Other Banks"),
        ],
        required=True,
    )
    account_id = fields.Many2one(
        "account.account", "Account", required=True, readonly=True
    )
    account_dest_id = fields.Many2one("account.account", "Destination Account")
    debit_amount = fields.Float("Debit")
    credit_amount = fields.Float("Credit")
    balance = fields.Float("Balance", readonly=True)

    @api.onchange("type")
    def _onchange_type(self):
        self.account_dest_id = False
        domain = [
            (
                "partner_id",
                self.type == "own_accounts" and "=" or "!=",
                self.account_id.partner_id.id,
            )
        ]
        return {"domain": {"account_dest_id": domain}}

    @api.model
    def create(self, vals):
        res = super(AccountMoveLine, self).create(vals)
        if not vals.get("balance"):
            res.balance = res.account_id.balance
        return res

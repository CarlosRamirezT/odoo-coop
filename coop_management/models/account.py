from odoo import api, fields, models


class AccountAccount(models.Model):
    _inherit = "account.account"

    type = fields.Selection(selection_add=[("savings", "Savings")])
    balance = fields.Float("Current Balance", compute="_compute_balance")
    open_balance = fields.Float("Opening Balance")
    move_line_ids = fields.One2many(
        "account.move.line",
        "account_id",
        string="Account Moves",
    )

    @api.depends("balance")
    def _compute_balance(self):
        # TODO: Implement balance computation
        self.balance = self.balance

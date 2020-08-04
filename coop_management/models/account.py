from odoo import api, fields, models


class AccountAccount(models.Model):
    _inherit = "account.account"

    name = fields.Char(required=False)
    user_type_id = fields.Many2one(required=False)
    type = fields.Selection([("savings", "Savings")])
    balance = fields.Float("Current Balance", compute="_compute_balance", store=True)
    open_balance = fields.Float("Opening Balance")
    move_line_ids = fields.One2many(
        "account.account.move",
        "account_id",
        string="Account Moves",
    )

    @api.depends("balance")
    def _compute_balance(self):
        # TODO: Implement balance computation
        self.balance = self.balance

    @api.multi
    def name_get(self):
        result = []
        for account in self:
            name = account.code
            result.append((account.id, name))
        return result

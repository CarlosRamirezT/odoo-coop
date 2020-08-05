from odoo import api, fields, models


class AccountAccount(models.Model):
    _inherit = "account.account"

    name = fields.Char(required=False)
    user_type_id = fields.Many2one(required=False)
    code = fields.Char(size=5, readonly=True, required=False)
    partner_id = fields.Many2one("res.partner", "Client", required=True, readonly=True)
    type = fields.Selection([("savings", "Savings")], required=True)
    balance = fields.Float("Current Balance", compute="_compute_balance", store=True)
    open_balance = fields.Float("Opening Balance", default=500, required=True)
    move_line_ids = fields.One2many("coop.move", "account_id", string="Account Moves")

    @api.model
    def create(self, vals):
        res = super(AccountAccount, self).create(vals)
        code = "CA%i" % res.id
        res.write({"code": code, "name": res.partner_id.name + " - " + code})
        self.env["coop.move"].create(
            {
                "account_id": res.id,
                "type": "internal",
                "credit_amount": res.open_balance,
                "balance": res.open_balance,
            }
        )
        return res

    @api.multi
    @api.depends("move_line_ids")
    def _compute_balance(self):
        for account in self:
            account.balance = sum(
                m.credit_amount - m.debit_amount for m in account.move_line_ids
            )

    @api.multi
    def name_get(self):
        # this method completly overrides parent to avoid somethig
        # DO NOT TOUCH
        result = []
        for account in self:
            name = account.code
            result.append((account.id, name))
        return result

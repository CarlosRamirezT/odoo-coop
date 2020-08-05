from odoo import api, fields, models


class AccountPayment(models.Model):
    _name = "coop.payment"
    _order = "create_date"

    loan_id = fields.Many2one("account.loan", "Account Loan", readonly=True, required=True)
    partner_id = fields.Many2one("res.partner", "Payment Partner", required=True)
    communication = fields.Char("Memo")
    payment_method = fields.Selection(
        [
            ("cashier", "Cashier"),
            ("transference", "Transference"),
            ("online", "Online"),
        ],
        "Method",
        default="cashier",
        required=True,
    )
    amount = fields.Float("Amount", required=True)
    due_amount = fields.Float("Due", readonly=True)

    @api.model
    def create(self, vals):
        res = super(AccountPayment, self).create(vals)
        if not vals.get("due_amount"):
            res.due_amount = res.due_amount
        return res

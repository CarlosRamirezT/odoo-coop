from odoo import api, fields, models


class AccountLoan(models.Model):
    _name = "account.loan"
    _description = "Account Loan"

    partner_id = fields.Many2one("res.partner", "Partner", required=True, readonly=True)
    currency_id = fields.Many2one("res.currency", "Currency")
    type = fields.Selection([("personal", "Personal")])
    initial_amount = fields.Float("Initial Amount")
    due_amount = fields.Float("Due Amount")
    rate = fields.Float("Interest Rate %")
    payment_terms = fields.Selection([("monthly", "Monthly Payment")])
    next_payment_date = fields.Date("Next Payment Date")
    payment_ids = fields.One2many("coop.payment", "loan_id")
    name = fields.Char(string="code", size=64, required=True, index=True)

    @api.depends("due_amount")
    def _compute_due_amount(self):
        # TODO: implement this function
        pass

    def _compute_next_payment_date(self):
        # TODO: implement this function
        # TODO: add computation to this field
        pass

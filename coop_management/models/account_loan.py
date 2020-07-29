from odoo import api, fields, models


class AccountLoan(models.Model):
    _name = "account.loan"
    _description = "Account Loan"

    partner_id = fields.Many2one("res.partner", "Partner")
    currency_id = fields.Many2one("res.currency", "Currency")
    type = fields.Selection([("personal", "Personal")])
    initial_amount = fields.Float("Initial Amount")
    due_amount = fields.Float("Due Amount", "_compute_due_amount", store=True)
    rate = fields.Float("Rate")
    payment_terms = fields.Selection([("monthly", "Monthly Payment")])
    next_payment_date = fields.Date("Next Payment Date")
    payment_ids = fields.One2many("account.payment", "loan_id")

    @api.depends("due_amount")
    def _compute_due_amount(self):
        # TODO: implement this function
        self.due_amount = self.due_amount

    def _compute_next_payment_date(self):
        # TODO: implement this function
        # TODO: add computation to this field
        pass

from odoo import api, fields, models


class AccountLoan(models.Model):
    _name = "account.loan"
    _description = "Account Loan"

    partner_id = fields.Many2one("res.partner", "Partner", required=True, readonly=True)
    currency_id = fields.Many2one("res.currency", "Currency", required=True)
    type = fields.Selection([("personal", "Personal")], required=True)
    initial_amount = fields.Float("Initial Amount", required=True)
    due_amount = fields.Float(
        "Due Amount", compute="_compute_due_amount", store=True, readonly=True
    )
    rate = fields.Float("Interest Rate %", required=True)
    payment_terms = fields.Selection([("monthly", "Monthly Payment")], required=True)
    next_payment_date = fields.Date("Next Payment Date")
    payment_ids = fields.One2many("coop.payment", "loan_id")
    name = fields.Char(string="Code", size=10, required=False, index=True)

    @api.model
    def create(self, vals):
        res = super(AccountLoan, self).create(vals)
        res.name = "CL%i" % res.id
        return res

    @api.multi
    @api.depends("payment_ids")
    def _compute_due_amount(self):
        for loan in self:
            loan.due_amount = loan.initial_amount - sum(
                [p.amount for p in loan.payment_ids]
            )

    def _compute_next_payment_date(self):
        # TODO: implement this function
        # TODO: add computation to this field
        pass

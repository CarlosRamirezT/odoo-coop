from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    document_number = fields.Char(
        "ID Document",
        required=True,
    )
    account_ids = fields.Many2many(
        "account.account",
        "partner_has_account",
        "partner_id",
        "account_id",
    )
    loan_ids = fields.Many2many(
        'account.loan',
        'partner_has_loan',
        'partner_id',
        'loan_id',
    )
    property_account_receivable_id = fields.Many2one(
        required=False,
    )
    property_account_payable_id = fields.Many2one(
        required=False,
    )

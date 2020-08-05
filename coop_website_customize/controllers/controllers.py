from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website


class Website(Website):

    @http.route('/', type='http', auth="public", website=True)
    def index(self, **kw):
        return request.render('coop_website_customize.coop_layout')

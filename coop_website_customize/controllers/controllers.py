# -*- coding: utf-8 -*-
from odoo import http

# class CoopWebsiteCustomize(http.Controller):
#     @http.route('/coop_website_customize/coop_website_customize/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/coop_website_customize/coop_website_customize/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('coop_website_customize.listing', {
#             'root': '/coop_website_customize/coop_website_customize',
#             'objects': http.request.env['coop_website_customize.coop_website_customize'].search([]),
#         })

#     @http.route('/coop_website_customize/coop_website_customize/objects/<model("coop_website_customize.coop_website_customize"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('coop_website_customize.object', {
#             'object': obj
#         })
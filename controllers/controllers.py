# -*- coding: utf-8 -*-
from openerp import http

# class PortalB2b(http.Controller):
#     @http.route('/portal_b2b/portal_b2b/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/portal_b2b/portal_b2b/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('portal_b2b.listing', {
#             'root': '/portal_b2b/portal_b2b',
#             'objects': http.request.env['portal_b2b.portal_b2b'].search([]),
#         })

#     @http.route('/portal_b2b/portal_b2b/objects/<model("portal_b2b.portal_b2b"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('portal_b2b.object', {
#             'object': obj
#         })
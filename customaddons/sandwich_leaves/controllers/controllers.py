# -*- coding: utf-8 -*-
# from odoo import http


# class SandwichLeaves(http.Controller):
#     @http.route('/sandwich_leaves/sandwich_leaves', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sandwich_leaves/sandwich_leaves/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sandwich_leaves.listing', {
#             'root': '/sandwich_leaves/sandwich_leaves',
#             'objects': http.request.env['sandwich_leaves.sandwich_leaves'].search([]),
#         })

#     @http.route('/sandwich_leaves/sandwich_leaves/objects/<model("sandwich_leaves.sandwich_leaves"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sandwich_leaves.object', {
#             'object': obj
#         })


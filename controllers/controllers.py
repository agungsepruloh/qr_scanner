# -*- coding: utf-8 -*-
from odoo import http


class QrScanner(http.Controller):
    @http.route('/qr_scanner', auth='public')
    def index(self, **kw):
        return http.request.render('qr_scanner.index', {})

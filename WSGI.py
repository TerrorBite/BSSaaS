#!/usr/bin/python3

from bssaas import app as bssaas
from bssaas_api import app as bssaas_api

app = DispatcherMiddleware(bssaas, {'/api': bssaas_api})

if __name__ == '__main__':
    bssaas.debug = True
    bssaas_api.debug = True
    run_simple('127.0.0.1', 5000, app, use_reloader=True, use_debugger=True, use_evalex=True)

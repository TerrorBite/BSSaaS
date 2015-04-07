require 'newrelic'

path = require 'path'
BSSAAS = require path.resolve(__dirname,'bssaas')

bssaas = new BSSAAS({
  renderersPath: path.resolve(__dirname,'renderers')
  filtersPath: path.resolve(__dirname,'filters')
  operationsPath: path.resolve(__dirname,'operations')
})

port = process.env.PORT || 5000

bssaas.start(port)

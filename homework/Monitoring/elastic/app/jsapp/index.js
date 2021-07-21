// index.js
    // запускаем apm agent
    var apm = require('elastic-apm-node').start({
        serviceName: 'jsApp',
        serverUrl: 'http://apm-server:8200'
      })
      // код приветствия
      const express = require('express')
      const app = express()
      app.get('/', (req, res) => {
       res.send('Hello World!')
      })
      app.listen(3000, () => console.log('Server running on port 3000'))
  
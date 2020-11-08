const port = 80;
const hostname = '0.0.0.0';
const endpoint = '/.well-known/acme-challenge/lTtG_Gr_dwcHNcUucN-8-MYdYuQ0qN1o_xXPSqJQOhM';
const toServe = 'lTtG_Gr_dwcHNcUucN-8-MYdYuQ0qN1o_xXPSqJQOhM.UGxa30kE1WhZWoiBWnwNmpmHasZXnx9h4L4-ox6l1OU';

require('http').createServer(function(request, response) {
   response.writeHead(200, {'Content-Type': 'text/plain'});
   response.end(toServe);
}).listen(port, hostname);
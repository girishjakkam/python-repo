import http.client
conn = http.client.HTTPSConnection("localhost", 80)
conn.set_tunnel("www.google.com")
conn.request("HEAD","/index.html")

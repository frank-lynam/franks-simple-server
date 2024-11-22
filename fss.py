import sys, os, http.server

httpath = "."

class fss(http.server.BaseHTTPRequestHandler):
  # This is the webserver

  def do_GET(s):
    path = s.path.split("..")[-1]
    if path.endswith("/"):
      path += "index.html"
    if os.path.isfile(httpath + path):
      s.send_response(200)
      if path.endswith("svg"):
        s.send_header("Content-type", "image/svg+xml")
      s.end_headers()
      with open(httpath + path, 'br') as fl:
        s.wfile.write(fl.read())
    else:
      s.send_response(404)
      s.end_headers()
      s.wfile.write(b"File not found")

if __name__=="__main__":
  # Starts a server based on command line args
  #   if any are given

  port = 8000
  for arg in sys.argv[1:]:
    if os.path.isdir(arg):
      httpath = arg
    if arg.isnumeric():
      port = int(arg)

  if httpath.endswith("/"):
    httpath = httpath[:-1]

  print(f"Frank's Simple Server Serving {httpath} "
      + f"on {port}.\nPress Ctrl+C to exit.")

  try:
    http.server.HTTPServer(('', port), fss).serve_forever()
  except KeyboardInterrupt:
    print("\rBye!")

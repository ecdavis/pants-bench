def application(environ, start_response):
    status = "200 OK"
    output = "0123456789"
    
    response_headers = [("Content-Type", "text/plain"),
                        ("Content-Length", str(len(output)))]
    start_response(status, response_headers)
    
    return [output]


import server

server.app.config['TESTING'] = True
client = server.app.test_client()

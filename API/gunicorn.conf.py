# Gunicorn config for production
bind = "0.0.0.0:8000"   # listen on all interfaces
workers = 2             # adjust based on CPU (2 x cores is a good start)
threads = 2             # lightweight concurrency for I/O-bound Flask apps
timeout = 60            # kill workers stuck longer than 60s
loglevel = "info"

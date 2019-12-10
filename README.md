Forwarder
---

This isn't ready for use. 

Forwarder is a simple project that allows you to create URL forwarders in flask-admin.

To use:
 
```
docker build . -t forwarder
docker run --rm -e ADMIN_USERNAME=something -e ADMIN_PASSWORD=something -e SECRET_TOKEN=something -p 8080:8080 -dit forwarder
```

The goal of this project is to replace the ~300 301s in zifnab.net's nginx configuration with a sane(ish) fallback for some paths. 

# Search whois
# By Busyman.Inc

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Debian or Ubuntu : sudo apt install whois

import whois 

domain = input("Enter your domain: ")
info = whois.whois(domain)
for key, value in info.items():
  print(key, ":", value)

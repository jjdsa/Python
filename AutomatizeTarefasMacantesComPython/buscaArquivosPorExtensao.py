#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:40:58 2020

@author: jario
"""
import os
os.listdir("/")
for filename in os.listdir("/home/jario/Documentos/"):
    if filename.endswith(".txt"):
        print(f"Arquivo encontrado {filename}")
        #os.unlink(filename)
print("Fim...".upper())

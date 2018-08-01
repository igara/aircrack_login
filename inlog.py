# -*- coding: utf-8 -*-
import re
from ftplib import FTP

f1 = open('log-01.csv', 'r')

fr = open('data1.js', 'r')
fr1 = fr.read()
cw = open('data2.js', 'w')
cw.write(fr1)
cw.close()

fw = open('data1.js', 'w')
for line in f1:
  # 対象の端末のMACアドレス
  if line.find('XX:XX:XX:XX:XX:XX') == 0:
    m = re.match('(..:..:..:..:..:..), (....-..-.. ..:..:..), (....-..-.. ..:..:..)', line)
    fw.write('document.write("<tr><td>igarashi</td><td>' + m.group(3) + '</td></tr>");\n')

f1.close()
fw.close()
fr.close()

fr = open('data1.js', 'r')
fw = open('data1.js', 'a+')

list = fr.read()

f1 = open('data2.js', 'r')

for line1 in f1:
  if list.find('igarashi') == -1:
    if line1.find('document.write("<tr><td>igarashi') == 0:
      fw.write(line1)

fr.close()
fw.close()
f1.close()

# 転送先
ftp = FTP('example.com', 'user', 'password')
f3 = open('data1.js', 'rb')
ftp.storlines('STOR /public_html/lab/data1.js', f3)
ftp.close()
f3.close()

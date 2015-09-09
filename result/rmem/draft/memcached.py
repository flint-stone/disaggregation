## numpy is used for creating fake data
import numpy as np 
import sys

import matplotlib.pyplot as plt

## Create data
data_str = '''814.512692928,805.787099123,807.823414087,815.199899912,803.538271904,852.285706043,800.320816994,834.052583933,798.978534937,835.671580076
828.004467964,819.586351871,823.335016012,853.712955952,840.663994074,824.262460947,828.078200102,829.114959955,823.919537067
823.156402111,861.82999897,833.751718998,839.901721001,833.846718073,819.431621075,840.255042076,841.145338058,837.141942024,824.254596949
904.494776011,919.379874945,917.76657486,929.73090601,914.500874043,905.561417103,899.091776848,913.616204023,909.526441097,913.997371912
890.83898592,899.074194908,913.341281891,887.919260979,905.187704086,914.437013865,899.143232107,882.5137918,884.739445925,895.915899038
902.8798094,916.2505864,941.6585999,917.7094912,904.6765448,903.966376,903.4805372,903.0239206,895.617965,944.6782562
975.378188848,980.63097477,994.025326014,993.807728052,970.451400995,1004.99139619,969.168493032,973.541966915,975.949682951,983.820743084
984.250060081,980.541732073,975.24669385,1000.15665913,975.925162077,976.268400908,979.240569115,979.988501072,984.506896973
985.076126099,979.193781137,978.887554884,989.009644032,975.010838985,971.242088079,984.52594614,973.171686172,974.989675045,1000.30177808
1069.48140621,1104.65247703,1109.18607306,1080.75039411,1085.86406207,1069.80704808,1065.21329188,1064.285954,1074.48384094,1074.76742196'''

data = map(lambda l: map(float, l.split(",")), data_str.split("\n"))
pos = [1, 3, 4, 5, 7, 8, 9, 11, 12, 13]
fig = plt.figure(1, figsize=(8,6))
ax = fig.add_subplot(111)
bp = ax.boxplot(data, positions = pos)
ax.set_xticks(pos)
ax.set_xticklabels(['Local','1us\n100G','1us\n40G','1us\n10G', '5us\n100G','5us\n40G','5us\n10G','10us\n100G','10us\n40G', '10us\n10G'])
plt.ylabel("Application Runtime (s)")
plt.title(sys.argv[0])
plt.savefig(sys.argv[0].replace(".py", ".png"))
plt.show()
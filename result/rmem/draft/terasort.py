## numpy is used for creating fake data
import numpy as np 
import sys

import matplotlib.pyplot as plt

## Create data
data_str = '''1707.6570549,1718.68220997,1721.84889603,1705.74547911,1727.69878316,1797.78105402,1711.72263503,1721.72242904,1707.79481506
1996.88759708,1717.73735213,1704.75005698,1719.6478889,1715.77209091,1714.65470409,1748.83402109,1729.88757086,1727.72138715
1796.15947104,1725.71437502,1736.69012403,1747.91762805,1739.78179193,1741.74371505,1745.68718004,1717.66394711,1706.83957386
1863.08534098,1861.99892402,1840.81925392,1818.94233894,1844.84654784,1823.00672507,1794.74968195,1907.9262681,1848.79874516
1717.7405901,1776.74388289,1761.74961591,1760.68226814,1713.15354705,1812.80290794,1789.79628897,1789.76529884,1786.83424497,1788.75359917
1824.45407,1760.54579,1791.452111,1886.187317,1791.413416,1806.15811,1834.94805,1782.856614,1824.776397,1808.603686
1846.45768189,1925.93296194,1844.87856102,1887.87248015,1935.91399002,1852.88762021,1849.78102303,1894.45782995,1843.92981219
1777.71088219,1820.78279185,1828.74560308,1767.74858308,1765.66745496,1810.84394503,1795.9290781,1820.85914993,1794.83732605
1798.71000791,1828.83561802,1846.16396785,1815.08243394,1848.90680385,1804.74996305,1873.97998381,1858.84297609,1820.81722498,1828.87999821
1909.82479405,1959.00047398,1909.91820383,1974.91715312,1913.89416814,1888.62918496,1949.87473917,1951.99533296,1900.86390305,1903.16293597'''

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
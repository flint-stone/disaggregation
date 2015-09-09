## numpy is used for creating fake data
import numpy as np 
import sys

import matplotlib.pyplot as plt

## Create data
def run(data_strs, exp_names):
	
	N = len(data_strs)
        data =  [map(lambda l: map(float, l.split(",")), data_str.split("\n")) for data_str in data_strs]
        data_normalized = [ [ [ r/np.median(app[0]) for r in setting] for setting in app] for app in data]

        stats = [ [ (np.median(setting), np.std(setting)) for setting in app] for app in data_normalized]

	print stats

	ind = np.arange(N)
	fig, ax = plt.subplots(figsize=(20,4))
	rects = []

	settings =       ['Local','1us/100G','1us/40G','1us/10G', '5us/100G','5us/40G','5us/10G','10us/100G','10us/40G', '10us/10G']
        setting_colors = ['black', 'darkgreen', 'green', 'lightgreen', 'darkblue', 'blue', 'lightblue', 'darkred', 'red', 'lightcoral']
        shift = 0.02
        setting_shifts = [ i * shift for i in [0, 1, 1, 1, 2, 2, 2, 3, 3, 3]]
	for i in range(0, len(settings)):
		means = [ apps[i][0] for apps in stats]
		std =   [ apps[i][1] for apps in stats]
		width = 0.08
		#print setting_colors[i]
		rects.append( ax.bar( 0.06 + ind + i * width + setting_shifts[i], means, width, color=setting_colors[i], yerr=std) )

	# add some text for labels, title and axes ticks
	ax.set_ylabel('Normalized Application Performance')
	ax.set_xticks(ind+width * len(settings) / 2)
	ax.set_xticklabels( exp_names )

	ax.legend( rects, settings, loc = 2, mode="expand", ncol = 10)

        plt.ylim( [0,2])	

	def autolabel(rects):
	    # attach some text labels
	    for rect in rects:
		height = rect.get_height()
		ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
		        ha='center', va='bottom')

#        for rect in rects:
#		autolabel(rect)
	
        plt.savefig(sys.argv[0].replace(".py", ".eps"))
        plt.savefig(sys.argv[0].replace(".py", ".png"))
	plt.show()

wordcount_str = '''1879.75496292,1873.08624315,1901.13909006,1883.51990199,1917.22369885,1982.25912499,1911.33951998,1925.3154881,1807.74851894,1887.18198514
1939.84849691,1955.05288386,1972.77829695,2069.92901802,1990.09658408,1968.7973609,1966.64373899,1983.64825201,1932.51552987,1964.56686115
1951.71992111,2074.70645809,1978.51379585,1947.08102703,1990.16550112,2083.44694901,1956.41240311,2123.26809311,1956.50741601,1946.41535711
2364.39395499,2375.94588709,2383.58227801,2381.58760285,2406.00737596,2399.91129303,2385.26837993,2573.21627903,2390.95383906,2375.07716393
2174.92440701,2173.12085986,2191.82519698,2191.08855605,2221.55244684,2212.07079816,2179.23702002,2239.24658895,2178.0722909,2184.077595
2186.72631478,2187.13785601,2171.45909381,2181.36524701,2213.52223897,2064.13407397,2177.76368093,2226.94757509,2159.3511939,2187.05886793
2683.58941007,2683.24713397,2678.11567903,2795.13196111,2698.03965187,2743.8863821,2575.22711706,2738.64955997,2674.77619195,2695.76858401
2597.17139792,2597.87125301,2575.68938589,2633.41101313,2602.58175993,2615.15579796,2632.39323616,2621.62625289,2674.91038084,2636.98531699
2393.64198899,2603.88502502,2598.936625,2632.32886481,2775.75096393,2625.44418907,2603.23689508,2595.76791978,2608.55437088,2588.48885393
3164.08223987,3193.42797685,3162.60116601,3196.74643898,3184.81652403,3192.52596116,3451.28412199,3180.14833999,3291.06327915,3176.37036896'''

terasort_str = '''1707.6570549,1718.68220997,1721.84889603,1705.74547911,1727.69878316,1797.78105402,1711.72263503,1721.72242904,1707.79481506
1996.88759708,1717.73735213,1704.75005698,1719.6478889,1715.77209091,1714.65470409,1748.83402109,1729.88757086,1727.72138715
1796.15947104,1725.71437502,1736.69012403,1747.91762805,1739.78179193,1741.74371505,1745.68718004,1717.66394711,1706.83957386
1863.08534098,1861.99892402,1840.81925392,1818.94233894,1844.84654784,1823.00672507,1794.74968195,1907.9262681,1848.79874516
1717.7405901,1776.74388289,1761.74961591,1760.68226814,1713.15354705,1812.80290794,1789.79628897,1789.76529884,1786.83424497,1788.75359917
1824.45407,1760.54579,1791.452111,1886.187317,1791.413416,1806.15811,1834.94805,1782.856614,1824.776397,1808.603686
1846.45768189,1925.93296194,1844.87856102,1887.87248015,1935.91399002,1852.88762021,1849.78102303,1894.45782995,1843.92981219
1777.71088219,1820.78279185,1828.74560308,1767.74858308,1765.66745496,1810.84394503,1795.9290781,1820.85914993,1794.83732605
1798.71000791,1828.83561802,1846.16396785,1815.08243394,1848.90680385,1804.74996305,1873.97998381,1858.84297609,1820.81722498,1828.87999821
1909.82479405,1959.00047398,1909.91820383,1974.91715312,1913.89416814,1888.62918496,1949.87473917,1951.99533296,1900.86390305,1903.16293597'''

graphlab_str = '''2276.07445908,2228.95552087,2314.92777205,2350.37122607,2379.97146511,2199.88685107,2191.828197,2253.69685817,2314.43491578,2316.3313241
2303.02900696,2284.68100619,2318.06077814,2339.32927012,2371.090065,2234.01861215,2198.05593109,2331.06982493,2351.00229812,2314.62422299
2334.01140404,2268.71974182,2358.96642399,2367.28536892,2367.16391802,2168.95250988,2216.70767808,2345.13234806,2346.64270806,2331.44336414
2396.36017299,2399.27219701,2440.85237718,2501.36106205,2305.53371692,2320.22943807,2365.9066329,2462.17564106,2437.73292804,2440.32287002
2333.59062004,2388.03117299,2402.21757984,2433.71182609,2275.17680001,2290.80467892,2241.902318,2355.41909409,2353.72018719,2373.73811412
2393.95039296,2381.35945702,2374.31200886,2428.08276582,2265.558424,2395.51611304,2265.43544698,2368.52569818,2372.55004978,2380.72121
2448.1635139,2456.06476903,2453.63716888,2544.15957713,2397.13749909,2850.83267808,2382.48261619,2460.83282495,2466.02190685,2506.81523299
2416.07203603,2474.78062892,2427.69328022,2492.81861997,2434.7611618,2408.249933,2316.0971539,2441.949646,2454.10155988,2339.72024202
2493.90304,2472.487506,2446.786961,2527.929897,2370.756289,2380.270556,2378.030151,2481.578581,2454.215707,2451.326411
2501.43097901,2631.62551093,2507.52497101,2622.16060805,2435.04244995,2479.58187294,2449.75596905,2645.65060806,2547.84484601,2443.48755097'''

memcached_str = '''814.512692928,805.787099123,807.823414087,815.199899912,803.538271904,852.285706043,800.320816994,834.052583933,798.978534937,835.671580076
828.004467964,819.586351871,823.335016012,853.712955952,840.663994074,824.262460947,828.078200102,829.114959955,823.919537067
823.156402111,861.82999897,833.751718998,839.901721001,833.846718073,819.431621075,840.255042076,841.145338058,837.141942024,824.254596949
904.494776011,919.379874945,917.76657486,929.73090601,914.500874043,905.561417103,899.091776848,913.616204023,909.526441097,913.997371912
890.83898592,899.074194908,913.341281891,887.919260979,905.187704086,914.437013865,899.143232107,882.5137918,884.739445925,895.915899038
902.8798094,916.2505864,941.6585999,917.7094912,904.6765448,903.966376,903.4805372,903.0239206,895.617965,944.6782562
975.378188848,980.63097477,994.025326014,993.807728052,970.451400995,1004.99139619,969.168493032,973.541966915,975.949682951,983.820743084
984.250060081,980.541732073,975.24669385,1000.15665913,975.925162077,976.268400908,979.240569115,979.988501072,984.506896973
985.076126099,979.193781137,978.887554884,989.009644032,975.010838985,971.242088079,984.52594614,973.171686172,974.989675045,1000.30177808
1069.48140621,1104.65247703,1109.18607306,1080.75039411,1085.86406207,1069.80704808,1065.21329188,1064.285954,1074.48384094,1074.76742196'''


run([wordcount_str, terasort_str, graphlab_str, memcached_str], ["wordcount", "terasort", "graphlab", "memcached"])
#run(terasort_str, "terasort", "Normalized Application Runtime (s)")
#run(graphlab_str, "graphlab", "Normalized Application Runtime (s)")
#run(graphlab_str, "memcached", "Normalized Latency (us)")

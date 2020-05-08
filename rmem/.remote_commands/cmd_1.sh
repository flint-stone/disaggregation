
      cd /mydata/lexu/disaggregation/rmem

      mkdir -p swap;
      insmod rmem.ko npages=5790760 get_record=0;
      mkswap /dev/rmem0;
      swapon /dev/rmem0;
      echo 0 > /proc/sys/fs/rmem/read_bytes;
      echo 0 > /proc/sys/fs/rmem/write_bytes;

      echo 40000000000 > /proc/sys/fs/rmem/bandwidth_bps;
      echo 5000 > /proc/sys/fs/rmem/latency_ns;
      echo 0 > /proc/sys/fs/rmem/end_to_end_latency_ns;
      echo 0 > /proc/sys/fs/rmem/inject_latency;

      pid=$(ps aux | grep kswapd0 | grep -v grep | tr -s ' ' | cut -d ' ' -f 2)
      taskset -cp 7 $pid
      
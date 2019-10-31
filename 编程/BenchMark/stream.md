``` bash
cd ~/mem
ps aux | grep 'stream_omp_exe' | awk '{print $2}' |xargs  kill -9
max_stream_array_size='20000000000'
stream_array_size=$(echo "scale=2;`free -m | grep Mem | awk '{print $4}'` * 1024 * 1024 / 32" | bc | cut -d'.' -f 1)
gcc -O stream.c -fopenmp -DSTREAM_ARRAY_SIZE=${stream_array_size} -DNTIME=30 -mcmodel=medium -o stream_omp_exe >./mem_res_multi.stream
sleep 1
for count in 1 2 3 4;do
    for i in `seq 1000`;do
        for j in `seq $count`;do
            ./stream_omp_exe >> mem_res_multi.stream &
        done
        now_time=`date +%s`
        next_run_time=$[$[$[$now_time/60]+1]*60]
        sleep $[$next_run_time-$now_time]
    done
done
```


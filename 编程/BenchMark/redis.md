

redis-benchmark



```bash
#!/usr/bin/env bash

get_local_ip(){
  local_ip=` cat /root/local_ip 2>/dev/null || ifconfig | grep 'inet' | grep -v '127.0.0.1' | grep -v 'inet6' | cut -d: -f2  | awk '{print $2}'`
  echo $local_ip
}
server_ip='172.17.146.151'
local_ip=`get_local_ip`
request_total_number=4000000
concurrence_test_number=1
redis_case='get'
#request_total_number=10000000
per_request_size=${redis_per_request_size:-32}

server_cpu_number=`ssh ${server_ip}  "cat /proc/cpuinfo | grep process | wc -l"`
start_port=7001
end_port=$(($start_port+$server_cpu_number))
cpu_c=`cat /proc/cpuinfo | grep process | wc -l`
concurrence_threads=${redis_concurrence_threads:-$cpu_c*2}
redis_request_per_thread=${redis_request_per_thread:-1500000}
request_total_number=${redis_request_total_number:-$((${concurrence_threads}*$redis_request_per_thread))}

for port in $(seq $start_port $end_port)
do
    redis-benchmark -h ${server_ip} -p ${port} -t ${redis_case} -r 10000000 -n ${request_total_number} -c ${concurrence_threads} -d ${per_request_size}  > ./c${local_ip}_s${server_ip}_${port}.redis &
done

redis-benchmark -h 172.17.146.151 -p 7001 -t get -r 10000000 -n 24000000 -c 16 -d 32
```



```shell
redis-benchmark -h 172.17.146.151 -p 7001 -t get -r 10000000 -n 24000000 -c 16 -d 32
for port in $(seq 7001 7009)
do
    redis-benchmark -h ${server_ip} -p ${port} -t ${redis_case} -r 10000000 -n ${request_total_number} -c ${concurrence_threads} -d ${per_request_size}  > ./c${local_ip}_s${server_ip}_${port}.redis &
done
```





```shell

for port in $(seq 7001 7032)
do
	redis-benchmark -h 172.17.146.151 -p 7001 -t get -r 10000000 -n 240000000 -c 16 -d 32  > ./${port}.redis &
done

```



```shell
for port in $(seq 7001 7032)
do
	/usr/local/redis/bin/redis-benchmark -h 172.17.146.151 -p ${port} -t get -r 10000000 -n 240000000 -c 64 -d 32  > ./${port}.redis &
done


```


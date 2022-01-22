#!/usr/bin/env bash
ip=("173.194.222.113" "192.168.0.1" "87.250.250.242")
da=$(date)
nul=

while ((1==1))
do
 for i in ${ip[@]}
 do
  er=$(nc -vzw5 $i 80 2>&1 | grep 'time')
  if [ "$nul" !=  "$er" ]
  then
   echo $da $i $er >> error.log	  
   exit
  fi   
  sleep 2
 done 
done 


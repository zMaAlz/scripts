#!/usr/bin/env bash

date > curl.log

while ((1==1))
do
 curl http://localhost:80
 if (($? != 0))
 then
  date >> curl.log
  sleep 5
 elif (($? == 1))
 then
  date >> curl.log
  exit
 fi
done

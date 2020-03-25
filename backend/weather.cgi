#!/bin/bash

ENDPOINT="api.openweathermap.org/data/2.5/weather?q="
#QUERY_STRING="city=cleveland&state=ohio"

function setup_keys(){
    source <(cat $(find . -name "weather.key"))
}

function query_map {
    saveIFS=$IFS
    IFS='=&'
    query=($QUERY_STRING)
    IFS=$saveIFS

    declare -A query_map
    for ((i=0; i<${#query[@]}; i+=2))
    do
        query_map[${query[i]}]=${query[i+1]}
    done
    echo ${query_map[@]}
}

function join_by { local IFS="$1"; shift; echo "$*"; }

function weather_data {
    param=$(query_map)
    location=`join_by , $param`
    query="${ENDPOINT}$location&appid=${API_KEY}"
    echo $(curl -sS $query)
}

echo "Content-Type: application/json"
echo
setup_keys
weather_data
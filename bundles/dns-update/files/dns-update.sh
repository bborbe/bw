#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

server="$1"
key="$2"
zone="$3"
node="$4"
ip=`curl -s $5`

echo "update ${zone}.${node} with $ip started"

ttl='60'
class='A'
tmpfile=$(mktemp)
cat >$tmpfile <<END
server $server
update delete ${node}.${zone} $ttl $class
update add ${node}.${zone} $ttl $class $ip
send
END
nsupdate -k $key -v $tmpfile
rm -f $tmpfile

echo "update ${zone}.${node} with $ip finished"

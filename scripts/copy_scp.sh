#!/bin/bash
# Copying Velti-MIG logs from proxynz server.
#scp -r root@116.90.133.227:/usr/local/mobileactive/logs/sms-gateway/ /tmp/velti
#echo "finished copying files"
#sleep 5
#echo "Starting archiving"
#rsync -r admin@58.162.142.237:/data2 /data
ssh admin@58.162.142.237 'tar czf /tmp/archive-`date +%y-%m-%d-%H`.tar /data'
rsync --remove-source-files admin@58.162.142.237:/tmp/archive-* /data
echo "Finished Archiving"

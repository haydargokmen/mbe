#!/bin/bash
# Copying Velti-MIG logs from proxynz server.
scp -r root@116.90.133.227:/usr/local/mobileactive/logs/sms-gateway/ /tmp/velti
# "Start archiving"
tar cvf /tmp/velti-mig-logs-`date +%y-%m-%d`.tar /tmp/velti
# "Finished Archiving"

# Upload to S3 bucket Production

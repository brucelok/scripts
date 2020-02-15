#!/bin/sh
# lok.bruce@gmail.com
# the script run with cron job to audit any change of user db
# 1 * * * *  audit_userdb.sh
LC_ALL=C
DATEFORMAT=`date '+%Y-%m-%d %H:%M:%S'`
USERDB="/etc/passwd"
LOGFILE="/var/log/current_users"
LOGCHANGE="/var/log/user_changes"
TMP="/tmp/tmp_pwd"

touch -a $TMP
touch -a $LOGFILE
touch -a $LOGCHANGE

# f1 is username, f6 is user directory
while IFS=: read -r f1 f2 f3 f4 f5 f6 f7
do
  # outputs username and directory to a temp file
  if [[ ! $f1 =~ ^# ]]; then
    echo "$f1:$f6" >> $TMP
  fi
done < $USERDB

# get md5 hash to log file
OLD_HASH=`tail -1 $LOGFILE`
NEW_HASH=`cat $TMP | md5`

# log when md5 is different
if [ $NEW_HASH != $OLD_HASH ]; then
  echo "$DATEFORMAT  users database /etc/passwd was changed"
fi

# log the md5 hash anyway
echo $NEW_HASH >> $LOGFILE
# clean up
rm -f $TMP

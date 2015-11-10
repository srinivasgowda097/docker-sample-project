#!/bin/bash

export ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe
export PATH=$ORACLE_HOME/bin:$PATH
export ORACLE_SID=XE

/u01/app/oracle/product/11.2.0/xe/bin/sqlplus system/oracle@localhost @/tmp/init.sql


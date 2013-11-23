#!/bin/sh

rand=`expr $RANDOM % 1000000`

usleep $rand

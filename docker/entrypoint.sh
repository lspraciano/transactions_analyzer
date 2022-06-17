#!/bin/sh
if [ "$PORT" = "" ]
then
    gunicorn --workers=4 --threads=2  -b :5001 "run:run_server()"

else
    gunicorn --workers=4 --threads=2  -b :$PORT "run:run_server()"
fi
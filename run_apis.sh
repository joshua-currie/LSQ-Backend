#!/bin/bash

cd API-Service

python3 blogsAPI.py &
python3 feedsAPI.py &
python3 monthlySalesAPI.py &
python3 topCardsAPI.py &
python3 topCustomersAPI.py &

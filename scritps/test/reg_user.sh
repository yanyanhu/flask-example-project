#!/bin/bash

curl -v -X POST -H "Content-Type: application/json" -d '{"username": "user1", "password": "pass1"}' localhost:8088/auth/register

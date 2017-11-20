#!/bin/bash

export FLASK_APP=src
export FLASK_DEBUG=true
pip install -e .
flask run

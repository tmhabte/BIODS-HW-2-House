#!/bin/bash

yes | conda create --name house python=3.9.12
eval "$(conda shell.bash hook)"
echo "Conda house environment is installed."

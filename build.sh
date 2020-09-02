#!/bin/bash
BASEPATH=$(cd "$(dirname $0)" || exit; pwd)
cd $BASEPATH || exit
rm -rf build
python setup.py bdist_wheel
mv dist MindSporeHub.egg-info build

#!/bin/bash
#
# @brief   gen_rpc
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2020
# @company None, free software to use 2020
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf new_simple_test/ full_simple/ latest/ empty_simple_test/
python3 -m coverage run -m --source=../gen_rpc unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html

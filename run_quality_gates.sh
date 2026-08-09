#!/bin/bash
#
# @brief   gen_rpc
# @version v1.0.5
# @date    Sun Aug 09 07:55:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 gates/gates/interfaces_checker.py gen_rpc
python3 gates/gates/isp_checker.py gen_rpc
python3 gates/gates/limits_checker.py gen_rpc
python3 gates/gates/srp_checker.py gen_rpc

echo "Done"

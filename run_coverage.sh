#!/bin/bash
#
# @brief   gen_rpc
# @version 1.0.5
# @date    Sun Aug 09 07:55:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_rpc
pylint gen_rpc > gen_rpc.report
echo "Done"

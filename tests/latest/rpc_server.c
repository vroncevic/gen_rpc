/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * server.c
 * Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
 * 
 * latest is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * latest is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */

#include <rpc/rpc.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "rpc_square.h"

square_out *square_process_1_svc(square_in *inp, struct svc_req *rqstp)
{
     static square_out out;
     out.res1= inp->arg1 * inp->arg1;
     return(&out);
}


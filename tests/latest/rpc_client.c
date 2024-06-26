/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * client.c
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

#include <errno.h>
#include <rpc/rpc.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "rpc_square.h"

int main(int argc,char **argv)
{
    CLIENT *cl;
    square_in in;
    square_out *outp;

    if(argc != 3)
    {
        printf("\nerror: insufficient arguments!!!\n");
        exit(-1);
    }

    cl = clnt_create(argv[1], SQUARE_PROGRAM, SQUARE_VERSION, "tcp");
    in.arg1 = atol(argv[2]);

    if(cl == NULL)
    {
        printf("\nerror: %s\n", strerror(errno));
        exit(-1);
    }

    if((outp = square_process_1(&in, cl))==NULL) {
        printf("\nerror: %s\n", clnt_sperror(cl, argv[1]));
        exit(-1);
    }

    printf("\nresult is: %ld\n", outp->res1);

    exit(0);
}


struct square_in {
    /* input arg */
    long arg1;
};

struct square_out {
    /* op result */
    long res1;
};

program SQUARE_PROGRAM {
    version SQUARE_VERSION {
        square_out SQUARE_PROCESS(square_in) = 1; /* process number */
    } = 1; /* version number */
} = 0x31230000; /* program number */

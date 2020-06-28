# rk-fit

Curve fitting of ternary Redlich-Kister equation.

## Redlich-Kister equation

@TODO: write a section about Redlich-Kister equation.

## Requirements

**rk-fit** depends on the `lmfit` python library. It performs Levenberg-Marquardt algorithm curve fitting algorithm and many more - take a look at their [site](http://cars9.uchicago.edu/software/python/lmfit/ "lmfit").

In order to install it type:

```
$ sudo apt-get install python-numpy python-scipy python-matplotlib ipython \
        ipython-notebook python-pandas python-sympy python-nose python-pip
$ sudo pip install lmfit
```

## Exec

There is an executable file called `rk-fit` that can run the **rk-fit** program. To run it specify an input config file:

`$ ./rk-fit <path_to_config_file>`

### Input samples

There are 4 samples of how to config **rk-fit**:

- `config/water_meg.json`
- `config/water_nacl.json`
- `config/meg_nacl.json`
- `config/ternary.json`

To test one of them do the following:

`$ ./rk-fit config/water_meg.json`

All output written to `stdout` will be write to `config/water_meg.out` file simultaneously.

Enjoy!


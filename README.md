# Ops

Some utilities for doing common tasks on remote computers.

## Installation

    git clone https://github.com/jonathanmarmor/ops.git
    pip install fabric

## Usage

To install and serve the "centaur" application on <hostname>

    cd ops
    fab -H <hostname> centaur.install

If you want to make a set of fab tasks for managing another application, look at centaur.py as an example.

# Ops

Some utilities for doing common tasks on remote computers.

## Installation

    git clone https://github.com/jonathanmarmor/ops.git
    cd ops
    pip install fabric

## Usage

To install and serve the "centaur" application on <hostname>

    fab -H <hostname> centaur.install

If you want to make a set of fab tasks for managing another application, look at centaur.py as an example.

Other tasks in fabfile can be used directly, but they're not all available at the moment becuase centaur.py is importing using the functions directly directly rather than using the clunkier execute('npm.install') syntax.  Maybe I'll fix this, but the primary use case of this is tool is creating new application-specific files in fabfile.

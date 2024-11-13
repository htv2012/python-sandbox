ROOT=$PWD
alias cdpkg='cd $ROOT/hvtext'
alias cdroot='cd $ROOT'
alias cdsam='cd $ROOT/hvtext/samples'
alias t='py.test $ROOT/hvtext/tests/*'

# Set up the development environment
function devenv() {
    source ~/.virtualenv/pytest/bin/activate
    python setup.py develop
}

echo Commands are: cdpkg, cdroot, cdsam, and t

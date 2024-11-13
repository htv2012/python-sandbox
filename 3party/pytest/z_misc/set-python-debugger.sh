if pip freeze | grep "^pudb" > /dev/null 2> /dev/null
then
    echo PUDB is installed
    export PYTHONBREAKPOINT="pudb.set_trace"
elif pip freeze grep "^ipdb" > /dev/null 2> /dev/null
then
    echo ipdb is installed
    export PYTHONBREAKPOINT="ipdb.set_trace"
fi


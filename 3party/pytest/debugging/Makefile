# --pdb: Invoke the debugger upon failure
# --pdbcls pudb.debugger:Debugger: Use the PUDB debugger
# --capture=no: let the debugger capture the IO
# --exitfirst: only debug the first failure, then end the tests
# --color=no: useful when debugging
.PHONY: help pudb ipython pdb clean

help:
	@echo Targets are: pudb, ipython, and clean

pudb:
	# Debug with pudb
	pytest --pdbcls=pudb.debugger:Debugger --pdb --capture=no --exitfirst --color=no

ipython:
	# Debug with ipython
	pytest --pdbcls=IPython.terminal.debugger:Pdb --pdb --capture=no --exitfirst --color=no

pdb:
	# Debug with the standard pdb
	pytest --pdb --capture=no --exitfirst --color=no

clean:
	-rm -fr __pycache__

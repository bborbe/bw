
default: precommit

precommit: test
	@echo "ready to commit"

test:
	bw test --ignore-missing-faults

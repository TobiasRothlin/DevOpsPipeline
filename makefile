setup: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install --upgrade pip &&\
		./venv/bin/pip install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf venv

test:
	./venv/bin/python3 test_BasicMathFunctions.py -v

style:
	./venv/bin/pylint --disable=R,C BasicMathFunctions.py
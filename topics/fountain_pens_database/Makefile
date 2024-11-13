run: lint
	# python3 csv2sqlite.py
	streamlit run dbui.py

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

clean:
	-rm data.csv data.sqlite

download:
	mv "${HOME}/Downloads/Pens and Papers Collection - Sheet1.csv" ./data.csv

show:
	sqlite3 data.sqlite 'select * from pen order by Brand, Model'
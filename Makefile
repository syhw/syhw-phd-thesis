all:
	pdflatex phdthesis
	bibtex phdthesis
	pdflatex phdthesis
	pdflatex phdthesis

clean:
	rm *.aux *.log *.blg *.bbl

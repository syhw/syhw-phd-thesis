all:
	pdflatex phdthesis
	bibtex phdthesis
	makeglossaries phdthesis
	pdflatex phdthesis
	pdflatex phdthesis

clean:
	rm *.aux *.log *.blg *.bbl *.glg *.glo *.gls *.ist *.toc chapters/*.aux

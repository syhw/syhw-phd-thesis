simple:
	pdflatex phdthesis

html:
	mk4ht htlatex youfile.tex 'xhtml,charset=utf-8,pmathml' ' -cunihtf -utf8 -cvalidate'

all:
	pdflatex phdthesis
	bibtex phdthesis
	makeglossaries phdthesis
	pdflatex phdthesis
	pdflatex phdthesis

clean:
	rm *.aux *.log *.blg *.bbl *.glg *.glo *.gls *.ist *.toc *.out *.xdy *.pdf *.mtc* *.lof *.lot *.brf *.maf *.4ct *.4tc *.dvi *.idv *.lg *.xref *.epub chapters/*.aux *.png *.html

simple:
	pdflatex phdthesis

html:
	#mk4ht htlatex phdthesis 'xhtml,charset=utf-8,pmathml' ' -cunihtf -utf8 -cvalidate'
	htlatex phdthesis myxhtml

bib:
	bibtex phdthesis
	makeglossaries phdthesis

all:
	pdflatex phdthesis
	bibtex phdthesis
	makeglossaries phdthesis
	pdflatex phdthesis
	pdflatex phdthesis

clean:
	rm *.aux *.log *.blg *.bbl *.glg *.glo *.gls *.ist *.toc *.out *.xdy *.mtc* *.lof *.lot *.brf *.maf *.4ct *.4tc *.dvi *.idv *.lg *.xref *.epub chapters/*.aux *.png 

total_clean:
	rm *.html *.pdf

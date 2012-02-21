\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{phdthesis}[2009/05/05 Standard LaTeX class]

\LoadClassWithOptions{thesis}
\RequirePackage{amsmath,amsthm}
\RequirePackage{float}
\RequirePackage{titlesec}
\RequirePackage{a4wide}
\RequirePackage{array}
\RequirePackage{url}
\RequirePackage{paralist}
\RequirePackage{xcolor}
\RequirePackage{makeidx}
\RequirePackage{textcomp}
\RequirePackage{ascii}
\RequirePackage{dingbat}
\RequirePackage{pifont}

% \renewcommand\labelitemi{\leftpointright}

% \makeatletter
% \newcommand\fs@myruled{\def\@fs@cfont{\bfseries}\let\@fs@capt\floatc@ruled
% \def\@fs@pre{}%\hrule height.8pt depth0pt \kern2pt}%
% \def\@fs@post{\kern2pt\hrule\relax}%
% \def\@fs@mid{\kern2pt\hrule\kern2pt}%
% \let\@fs@iftopcapt\iffalse}%\fi
% \makeatother


% \floatstyle{myruled}
% \restylefloat{figure}
% \restylefloat{table}

% \DeclareOption{allchapters}
% {\renewcommand\@schapter\par}
% \ProcessOptions

\setcounter{secnumdepth}{3}
\renewcommand{\thesubsubsection}{\thesubsection.\alph{subsubsection}}

\titleformat{\chapter}[display]
{\sffamily\bfseries\Huge}
{\raggedleft
\color[gray]{.5}{\MakeUppercase{\chaptertitlename} \fontsize{76}{80}\usefont{OT1}{pzc}{m}{n}\selectfont\thechapter}}
{60pt}
{\titlerule
\vspace{15pt}
\raggedleft
}[
\vspace{15pt}
\titlerule
]

\titleclass{\part}{page}
\titleformat{\part}[display]
{\centering\normalfont}
{\huge \sffamily \bfseries \partname~\thepart}
{20pt}
{
\Huge \sffamily \bfseries
}

\titleformat{\section}{\normalfont\Large\sffamily\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}{\normalfont\large\sffamily\bfseries}{\thesubsection}{1em}{}
\titleformat{\subsubsection}[runin]{\normalfont\normalsize\sffamily\bfseries}{\thesubsubsection}{1em}{}
\titleformat{\paragraph}[runin]{\normalfont\normalsize\sffamily}{\theparagraph}{1em}{}
\titleformat{\subparagraph}[runin]{\normalfont\normalsize\sffamily}{\thesubparagraph}{1em}{}

\titlespacing*{\chapter}{0pt}{80pt}{80pt}
\titlespacing*{\section}{0pt}{3.5ex plus 1ex minus .2ex}{2.3ex plus .2ex}
\titlespacing*{\subsection}{0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}
\titlespacing*{\subsubsection}{0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}
\titlespacing*{\paragraph}{0pt}{3.25ex plus 1ex minus .2ex}{1em}
\titlespacing*{\subparagraph}{\parindent}{3.25ex plus 1ex minus .2ex}{1em}

\input{ttlps.def}

\newpagestyle{main}{%
%\setmarks{\chapter}{\section}
\headrule
\sethead[\thepage][][\upshape\sffamily \raggedleft\chaptername\ \thechapter.\ \chaptertitle]
{\sffamily {\thesection.\ \sectiontitle}}{}{\thepage}
}

% \titlecontents{part}[2em]{\addvspace{20pt}\normalfont\large\bfseries}{\contentslabel{1.6em}}{\hspace*{-1.6em}}{\hfill\contentspage}
% \titlecontents{chapter}[1.5em]{\addvspace{11.8pt}\normalfont\normalsize\bfseries}{\contentslabel{1.3em}}{\hspace*{-1.3em}}{\hfill\contentspage}
% \dottedcontents{section}[3.8em]{\normalfont\normalsize}{2.3em}{1pc}
% \dottedcontents{subsection}[7em]{\normalfont\normalsize}{3.2em}{1pc}

% \let\@printindexbase\printindex
% \renewcommand{\printindex}
% {\chapter{Index}
% \@printindexbase
% }


\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[chapter]
\newtheorem{proposition}{Proposition}[chapter]
\newtheorem{propositiondefinition}[proposition]{Proposition-Definition}
\newtheorem{lemma}{Lemma}[chapter]
\newtheorem{claim}[lemma]{Claim}
\newtheorem{corollary}[proposition]{Corollary}
\newtheorem{invariant}{Invariant}[chapter]

\theoremstyle{definition}
\newtheorem{definition}{Definition}[chapter]

\theoremstyle{remark}
\newtheorem{remark}{Remark}[chapter]
\newtheorem{example}[remark]{Example}

\newcommand{\etal}{\textit{et al.}}
\newcommand{\etc}{\textit{etc}}

\newcolumntype{M}[1]{>{\centering}m{#1}}
\newcolumntype{P}[1]{>{\centering}p{#1}}
\newcolumntype{B}[1]{>{\centering}b{#1}}

\setlength{\pltopsep}{0.75ex}
\setlength{\plitemsep}{0.75ex}

\renewcommand{\contentsname}{Table of Contents}

\newcommand{\titlelogo}{
\begin{tikzpicture}
 \draw(0,0) node {\includegraphics[width=4cm]{EADS_Logo.png}};
 \draw(6,0) node {\includegraphics[width=3cm]{logo-ens-cachan.png}};
\end{tikzpicture}
}

%<*sample05>

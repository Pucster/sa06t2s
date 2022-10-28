\documentclass{article}

% if you need to pass options to natbib, use, e.g.:
%     \PassOptionsToPackage{numbers, compress}{natbib}
% before loading neurips_2019

% ready for submission
% \usepackage{neurips_2019}

% to compile a preprint version, e.g., for submission to arXiv, add add the
% [preprint] option:
%     \usepackage[preprint]{neurips_2019}

% to compile a camera-ready version, add the [final] option, e.g.:
\usepackage[final]{neurips_2019}

% to avoid loading the natbib package, add option nonatbib:
%     \usepackage[nonatbib]{neurips_2019}

\usepackage[utf8]{inputenc} % allow utf-8 input
\usepackage[T1]{fontenc}    % use 8-bit T1 fonts
\usepackage{hyperref}       % hyperlinks
\usepackage{url}            % simple URL typesetting
\usepackage{booktabs}       % professional-quality tables
\usepackage{amsfonts}       % blackboard math symbols
\usepackage{nicefrac}       % compact symbols for 1/2, etc.
\usepackage{microtype}      % microtypography
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{makecell}


\title{Initial report - Text detection and text recognition in images for Text2Speech modules}

% The \author macro works with any number of authors. There are two commands
% used to separate the names and addresses of multiple authors: \And and \AND.
%
% Using \And between authors leaves it to LaTeX to determine where to break the
% lines. Using \AND forces a line break at that point. So, if LaTeX puts 3 of 4
% authors names on the first line, and the last on the second line, try using
% \AND instead of \And before the third author name.

\author{%
 TEAM: SA06\_01
 \AND
 Eugen Leonid Cocalea Creoleanu (ELCC)\\
1408A
}
\begin{document}

\noindent\begin{minipage}{0.1\textwidth}% adapt widths of minipages to your needs
\includegraphics[width=1.1cm]{imagini/logo_AC.png}
\end{minipage}%
\hfill%
\begin{minipage}{1\textwidth}\raggedright
Technical University "Gheorghe Asachi", Iași\\
Faculty of Automatic Control and Computer Engineering\\
Image Processing
\end{minipage}
% \end{}

\maketitle

\section{Project overview}

The application we're going to develop is a Proof of Concept application that is attempting to identify text in images, recognize that text and output that in a format ready to be picked up by a 3rd party application.

Text detection and recognition applications can be used for a multitude of purposes like translating instructions (recipes, street directions, attraction descriptions, newspaper articles) written in a foreign language, helping visually impaired or illiterate people get around tasks that involve reading instructions, creating Augmented Reality applications that take information from the real world and present it to the user. The eventual end goal is to have the application run on portable / wearable computers that will accompany the user in the real world and continuously find information to work on in the surroundings.

The objective of the project is to achieve a reasonable rate of text detection and recognition in images that are already acquired and fed into the application while leaving its integration with 3rd party applications (like portable / wearable computers, translation engines, text2speech engines) for a later project.

Expected challenges are mostly related to the lack of field knowledge by the team and the scarcity of time to be allocated to the project.

Potential consumers: tourists, visually impaired people, illiterate people, kids learning to read, neglected kids that needs a story read to them one evening.

Competitors: Meta \cite{MetaARVR}, Apple \cite{AppleGlasses}, Google \cite{GoogleGlasses}


\section{Development approach}

\color{black}

\textbf{Task allocation}

\begin{center}
\begin{tabular}{ |c|c|c|c| }
 \hline
 \thead{Task ID} & \thead{Task description} & \thead{Team member} & \thead{Estimated time}\\
  \hline
 Research & Research on existing solutions and technologies &  ELCC & 8h \\
  \hline
 Design & \makecell{Application design \\ Choosing relevant technologies} &  ELCC & 8h\\
 \hline
 Implementation & \makecell{Application development \\ Application testing} & ELCC & 48h \\
 \hline
 Documentation & Writing application documentation & ELCC & 8h\\
 \hline
\end{tabular}
\end{center}

\textbf{Git repository:} \href{https://github.com/Pucster/sa06t2s}{https://github.com/Pucster/sa06t2s}

\medskip

\small
%Exemple de referințe,

\color{black}


\begin{thebibliography}{9}
\bibitem{MetaARVR}
\href{https://tech.fb.com/ar-vr/}{Meta AR/VR}

\bibitem{GoogleOCR}
\href{https://cloud.google.com/vision/docs/ocr}{Google OCR}

\bibitem{AppleGlasses}
\href{https://www.macrumors.com/roundup/apple-glasses/}{Apple Glasses}

\bibitem{GoogleGlasses}
\href{https://www.google.com/glass/start/}{Google Glasses}

\end{thebibliography}

\end{document}


%pentru a insera un tabel https://www.overleaf.com/learn/latex/tables#Creating_a_simple_table_in_LaTeX
%pentru a insera imagini https://www.overleaf.com/learn/how-to/Including_images_on_Overleaf

%\begin{figure}[htp]
%    \centering
%    \includegraphics[width=4cm]{imagini/logo_AC.png}
%    \caption{Logo AC}
%    \label{fig:logoAC}
%\end{figure}

%pentru a insera liste https://www.overleaf.com/learn/latex/Lists
%ordered 1, 2, 3, ..
%\begin{enumerate}
%  \item The labels consists of sequential numbers.
%  \item The numbers starts at 1 with every call to the enumerate environment.
%\end{enumerate}

%unordered
%\begin{itemize}
%  \item The individual entries are indicated with a black dot, a so-called bullet.
%  \item The text in the entries may be of any length.
%\end{itemize}

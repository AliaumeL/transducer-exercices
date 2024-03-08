# transducer-exercices

![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Inkscape](https://img.shields.io/badge/Inkscape-e0e0e0?style=for-the-badge&logo=inkscape&logoColor=080A13)
![LaTeX](https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white)
![Pandoc](https://img.shields.io/badge/pandoc-%231a1a1a.svg?style=for-the-badge&logo=pandoc&logoColor=white)
![Lua](https://img.shields.io/badge/lua-%232C2D72.svg?style=for-the-badge&logo=lua&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/AliaumeL/transducer-exercices)
![GitHub Release](https://img.shields.io/github/v/release/AliaumeL/transducer-exercices)
![GitHub deployments](https://img.shields.io/github/deployments/AliaumeL/transducer-exercices/github-pages)


Exercises for transducers classes of [MIMUW]. The lecture notes are available
on [the dedicated webpage][lecture-notes]. A web version of the sessions is
[deployed on github pages][ghpages].

[MIMUW]: https://www.mimuw.edu.pl
[lecture-notes]: https://www.mimuw.edu.pl/~bojan/2023-2024/przeksztalcenia-automatowe-transducers
[ghpages]: https://aliaumel.github.io/transducer-exercices


## Usage 

The exercises are written in *pandoc flavored markdown* and are compiled to
HTML and PDF using `make`. They are located in a `content/` subdirectory.
It is possible to produce a pdf version of one exercise sheet by simply
running the following command:

```bash
make latex/session-1.pdf
```

To produce a web version of the same exercise sheet, run the following command:

```
make site/session-1.html
```

Beware that web versions of the exercises are not *standalone*, and require
extra static elements (css, javascript) to be displayed properly. In
particular, it is often better to first build the whole website, and then only
use `make` to produce a particular exercise sheet.

```
make website
```

Similarly, to produce the PDFs of all sessions, run the following command:

```
make pdfs
```

Finally, the following command will produce a web version of the exercises, that
is automatically reloaded whenever a file is modified.  Note that this does not
start a web server, and you may have to open the files manually in your browser.

```bash
make watch 
```

If you have python installed, you can also use the following command to start
a webserver in the `site/` directory:

```bash
cd site && python3 -m http.server 8000
```

## Requirements

The following packages are required for the makefile to run smoothly:

- make
- git
- pandoc
- python3
- panflute
- a texlive installation
- the dosis font
- entr
- zip
- gnutar
- mathjax (node package)

# How to contribute

To contribute, please read the [CONTRIBUTING.md](CONTRIBUTING.md) file.

# Credits

The original design of the website is taken from [Arthur
Perret](https://www.arthurperret.fr/).


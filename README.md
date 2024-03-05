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

### How to compile to a PDF

```bash
make latex/session-1.pdf
```

### How to produce a web version of an exercise session

```
make site/session-1.html
```

### How to produce the whole web version locally

```
make website
```

### How to produce the PDFs of all sessions

```
make pdfs
```

### How to live preview

The following command will trigger a full rebuild when a markdown file is
edited[^ requires `entr`].

```bash
make watch 
```

## Requirements

- make
- pandoc
- python3
- panflute
- latex
- entr


# Credits

The original design of the website is taken from [Arthur
Perret](https://www.arthurperret.fr/).

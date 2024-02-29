# transducer-exercices

Exercices for transducers classes of [MIMUW].
The lecture notes are available on [the dedicated webpage][lecture-notes].

[MIMUW]: https://www.mimuw.edu.pl
[lecture-notes]: https://www.mimuw.edu.pl/~bojan/2023-2024/przeksztalcenia-automatowe-transducers

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

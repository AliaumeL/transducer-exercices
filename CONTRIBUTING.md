# Contributing

If you would like to contribute to this project, please open an issue or fork
the repository and submit a pull request.

## How to contribute

There are four main ways to contribute to this project, but if you have any
other ideas they are welcome:

1. Add translations of exercises in other languages.
2. Add hints and solutions to exercises.
3. Add new exercises.
4. Improve the generation of the website and pdf files.

## Writing Exercises

The repository is organized in the following way: for each exercise session
(thematically grouped, typically used for a one or two hours session), there is
a markdown file named `content/session-<number>.md`.

The file is written in classical "pandoc markdown" (see [pandoc's
guide](https://pandoc.org/MANUAL.html#pandocs-markdown)), and can use *some*
LaTeX commands. The typical shape of an exercise session file is the following:

1. First there is a preamble with metadata (title, subtitle, date, etc.),
2. Then there is a list of exercises,
3. Then, there is a list of homework,
4. Finally, there is a list of definitions and theorems (cheat sheet).

### Preamble

The format of the preamble is as follows:

```markdown
---
title: Transducers
subtitle: <name>
session: <number>
date: <YYYY-MM-DD>
email: <email>
lang: en-GB
---

<!-- START LaTeX commands --> 
\newcommand{\set}[1]{\{#1\}}
\newcommand{\Nat}{\mathbb{N}}
\newcommand{\vcount}[2][]{\left| #2 \right|_{#1}}
<!-- END   LaTeX commands -->
```

### Exercises

The format of an exercise is as follows:

```markdown
# Exercises

## First Exercice Name {.exercise}

Content of the first exercise.

## Second Exercice Name {.exercise}

Content of the second exercise.
```


### Hints and Solutions

It is possible to add hints and solutions to exercises by adding subsections
with the class `.hint` or `.solution`:

```markdown
## First Exercice Name {.exercise}

Content of the first exercise.

### First Hint Name {.hint}

Content of the first hint.

### Second Hint Name {.hint}

Content of the second hint.

### First Solution Name {.solution}

Content of the first solution.

### Second Solution Name {.solution}

Content of the second solution.
```

### Cheat Sheet

At the end of the document, it may be useful to have a list of definitions so
that the exercise session is self contained. This is done by adding a section
with the class `.cheat-sheet`, with thematic subsections containing
definitions and theorems as follows:

```markdown
# Cheat Sheet {.cheat-sheet}

## Topology

### What is a topological space? {.def}

A topology on a set $X$ is a collection $\mathcal{T}$ of subsets of $X$ such that …

### What is a continuous function? {.def}

A function $f : X \to Y$ between topological spaces is continuous if for every
open set $U \subseteq Y$, the preimage $f^{-1}(U)$ is open in $X$.

## Category Theory

### What is a category? {.def}

A category $\mathcal{C}$ consists of a collection of objects
$\text{Ob}(\mathcal{C})$ and for every pair of objects $X, Y \in
\text{Ob}(\mathcal{C})$, a set $\text{Hom}(X, Y)$ of morphisms from $X$ to $Y$ …
```

### Advanced options


#### Custom LaTeX commands

It is possible to add custom LaTeX commands to the document, by using
`\newcommand`. However, for it to work in the HTML export it is not possible to
use the `xparse` package (and its `\NewDocumentCommand`), nor to use "exotic"
LaTeX packages.

A limited subset of the `knowledge` package is available (implemented via
a filter) that works both in HTML and in LaTeX exports.
The syntax is the following:

```markdown

You can introduce "a knowledge", which is a word to which you can refer
afterwards. For instance by writing 'a knowledge'. It is possible to have
several equivalent ways to refer to a given knowledge, which is done as follows
'some knowledges'.

```

For the preprocessor to understand that `a knowledge` and `some knowledges` are
the same concept, you need to add to the metadata of the document
a `knowledge` field, as follows:

```yaml
knowledges:
    - synonyms: 
        - a knowledge
        - some  knowledges
    - ...
```

This should be written directly in the document metadata. A possibility that is
not yet explored is to use a `knowledge-file` field, that imports metadata from
a `yaml` file, but there is no such feature yet.

Furthermore, it is not yet possible to use the `knowledge` package in the
mathematical definitions. This would actually break the HTML export. 

#### Translations

A limited form of translations is available.
To add a translation to an exercise, you have two main possibilities.
The first one is to translate `inline` elements 
by writing `[ default content ]{data-lang-fr="Content in French"
                               data-lang-en="Content in English"
                               data-lang-pl="Content in Polish"}`
The second possibility is to use
block elements, and write:

```markdown

::: {data-lang-fr=true}

Only french content here

:::

```

There may be some better ways to put translations, and in particular this does
not play well with the `pdf` export yet, so it is reserved for the `index.md`.
Key issues are: LaTeX export should select a language, and the `knowledge`
package should not complain about multiple definitions of the same term in
different languages.

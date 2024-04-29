---
author: Aliaume LOPEZ
title: Transducers
subtitle: Linear Regular Functions
email: ad.lopez@uw.edu.pl
lang: en-GB
session: 8
date: 2024-04-08
refs: |
   ::: {#refs}
   :::
---

<!-- These are the latex command used in this document --->
\newcommand{\Nat}{\mathbb{N}}
\newcommand{\Real}{\mathbb{R}}
\newcommand{\Rel}{\mathbb{Z}}

\newcommand{\MSO}{\mathbb{MSO}}
\newcommand{\FO}{\mathbb{FO}}

\newcommand{\satisfies}{\models}

\newcommand{\Mat}[1]{\mathcal{M}_{#1}}

\newcommand{\PSet}[1]{\mathcal{P}(#1)}

\newcommand{\mealy}[1]{\mathcal{#1}}
\newcommand{\defined}{:=}
\newcommand{\emptyword}{\varepsilon}
\newcommand{\concat}{\mathrel{\cdot}}
\newcommand{\set}[1]{\{ #1 \}}
\newcommand{\setof}[2]{\left\{#1 \mid #2\right\}}
\newcommand{\seqof}[2]{\left(#1\right)_{#2}}
\newcommand{\Parts}{\mathop{\mathcal{P}}}
\newcommand{\preim}[2]{{#1}^{-1}\left(#2\right)}
\newcommand{\vcount}[2][]{\left| #2 \right|_{#1}}
\newcommand{\im}[2]{#1\left(#2\right)}
\newcommand{\graph}{\mathsf{graph}}
\newcommand{\topartial}{\rightharpoonup}
\newcommand{\tosurj}{\twoheadrightarrow}
\newcommand{\prefleq}{\mathrel{\sqsubseteq_{\mathsf{prefix}}}}

\newcommand{\card}[1]{\left| #1 \right|}
\newcommand{\countval}[1]{\# #1}

\newcommand{\Res}{\mathsf{Res}}
\newcommand{\resi}[2]{{#2}^{-1}{#1}}

\newcommand{\lowercaseExample}{\mathsf{lowercase}}
\newcommand{\expandtabs}{\mathsf{expandtabs}}
\newcommand{\sort}{\mathsf{sort}}
\newcommand{\swap}{\mathsf{swap}}

\newcommand{\toinj}{\hookrightarrow}

# Coding

## Using For-Transducers {.exercise}

Code the following functions 

- [ ] $w \mapsto w w$
- [ ] $w \mapsto w_{\text{odd}} w_{\text{even}}$
- [ ] $wa \mapsto aw$
- [ ] $(ab)^n \mapsto a^n b^n
- [ ] $x w y \mapsto (xy)^{|w|}$
- [ ] $\mathbf{1}_{L}$ where $L$ is a regular language
- [ ] $k$-nested map-reverse
- [ ] $w \mapsto \prod_{i,j \text{ lex}} w_i w_j$

Describe the number of nested loops used.

## First order ! {.exercise}

Let $L$ be a first-order definable language. White a *monotone* for-program
that computes $\mathbf{1}_{L}$, i.e., a for-program where the only possible
assignment of variables is $x := \top$.

## Polyblind {.exercise}

We define polyblind for-transducers are those where
only the innermost variable loop can be tested against.

1. Prove that those programs do not compose.
2. Prove that the squaring function (without underscores) is polyblind.
3. Prove that the squaring function (with underscores) is not polyblind.
4. Prove that the function that maps $i$ to $\sum_{j \leq i} j$ is polyblind.
5. Prove that the function that maps $i$ to $\sum_{j \leq i} j$ can be realised
   by a *monotone* for-program.
6. Can the function $i \mapsto \sum_{j \leq i} j$ be realised by a *blind*
   **and** *monotone* for-program?

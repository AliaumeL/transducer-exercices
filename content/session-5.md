---
author: Aliaume LOPEZ
title: Transducers
subtitle: Linear Regular Functions
email: ad.lopez@uw.edu.pl
lang: en-GB
session: 5
date: 2024-03-18
refs: |
   ::: {#refs}
   :::
---

<!-- These are the latex command used in this document --->
\newcommand{\Nat}{\mathbb{N}}
\newcommand{\Real}{\mathbb{R}}
\newcommand{\MSO}{\mathbb{MSO}}
\newcommand{\FO}{\mathbb{FO}}

\newcommand{\satisfies}{\models}

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

\newcommand{\Res}{\mathsf{Res}}
\newcommand{\resi}[2]{{#2}^{-1}{#1}}

\newcommand{\lowercaseExample}{\mathsf{lowercase}}
\newcommand{\expandtabs}{\mathsf{expandtabs}}
\newcommand{\sort}{\mathsf{sort}}
\newcommand{\swap}{\mathsf{swap}}

\newcommand{\Atoms}{\mathbb{A}}

<!-- end of the custom commands -->


# Atomisation and Deatomisation

## Deatomisation of Bimachines {.exercise}

We define "atom bimachines" as follows.
We say that a function $f$ is deatomisable if there exists a (usual) bimachine $A$
such that for all *codes* $c \colon \Atoms \toinj \langle 1^* \rangle$,
the following commutes

$$
c \circ f = A \circ c \quad .
$$

Prove that the following are equivalent:

1. A function $f$ is deatomisable,
2. It is realisable by an atomic bimachine.


## Atomic Bimachines {.exercise}

Prove that the following are not computable by atomic bimachines.

1. The reverse function.
2. The duplicate function.
3. The "unzip" function.

Conclude that those cannot be performed by *bimachines* in general.

## Deatomisation of Sweeping Transducers {.exercise}

??

# Pumping Lemmas

## Pumping Bimachines {.exercise}

Let $f$ be computed by a bimachine. We extend the function $f$ by considering
$f(w_1 [w] w_2)$ to be the word *produced by the bimachine* when reading $w$,
under the context $w_1$ and $w_2$. 

1. Prove that $f(w_1 w [w]^{X \times n!} w  w_2)$ is of the form $\alpha
   \beta^X \gamma$ for some $\alpha, \beta, \gamma$, where $n$ is the number of
   states of the automata in the bimachine.
2. Conclude that reverse, duplicate and unzip are not computable by bimachines.

## Pumping 2DFTs {.exercise}

??

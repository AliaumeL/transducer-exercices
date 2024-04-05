---
author: Aliaume LOPEZ
title: Transducers
subtitle: Linear Regular Functions
email: ad.lopez@uw.edu.pl
lang: en-GB
session: 6
date: 2024-04-08
knowledges:
    - synonyms:
        - rational series
    - synonyms:
        - weighted automata
        - weighted automaton
    - synonyms:
        - counting formulas
        - counting formula
    - synonyms:
        - recursive invisible pebble
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


# Commutativity

This section is inspired by the Ph.D. thesis of @Gaetan2023, and particularly
of its Chapter 5 called *Polyregular functions with commutative outputs* on
page 123.

A function $f$ is "commutative" when, for all $n \in \Nat$, for all permutation
$\sigma \in \mathcal{S}_n$, for all $w \in \Sigma^n$, $f(w) = f(\sigma(w))$.
A function has "unary output" when the output alphabet is $\set{1}$.

## Deciding Commutativity {.exercise .warmup}

Let $f$ be a function from $\Sigma^*$ to $\Gamma^*$ computed by a 2DFT. Is it
decidable whether $f$ is commutative?

## Unary Output {.exercise .warmup}

Let $f$ be a function from $\Sigma^*$ to $\set{1}^*$. Prove that the following are equivalent:

1. $f$ is computed by a 2DFT.
2. $f$ is computed by a rational function.

This is Theorem 5.15 in the case $k = 1$ in @Gaetan2023.


## Rational Series {.exercise}

A "rational series" is a function from $\Sigma^*$ to $K$ where $K$ is
a semi-ring that is computed by a 'weighted automaton'. We recall that
a "weighted automaton" $W$ is a finite (non-deterministic) automaton with
weights in $\Real$, whose semantics is defined as $W(w)$ is the sum over all
accepting runs of $W$ of the product of the weights along this path.
Equivalently, a 'weighted automaton' is defined in terms of monoids by
a morphism $\mu \colon \Sigma^* \to \Mat{n,n}(\Real)$ and a linear map $\lambda
\colon \Mat{n,n}(\Real) \to \Real$, such that $W(w) \defined \lambda(\mu(w))$.


We define "counting formulas" as a generalisation of the correspondence between
$\MSO$ and regular languages to the case of 'rational series'. A counting
formula is a formula $\varphi \in \MSO$ with first-order and second-order free
variables, whose semantics is given by $\countval{\varphi}(w) \defined
\card{\setof{\nu \text{ valuation }}{w, \nu \models \varphi(w)}}$.

Prove that the following are equivalent:

1. $f$ is computed by a 'weighted automaton' with $\Nat$-output,
2. $f$ is computed by a 'counting formula'.

What happens if you restrict formulas to be in $\FO$?

## Recursive Invisible Pebbles {.exercise .challenging}

We define a "recursive invisible pebble" transducer as follows: it is
a collection of 2DFTs over the same input alphabet $\Sigma$ and the same output
alphabet $\Gamma$, where the transitions are defined as usual, except that some
transitions can perform a *recursive call* to another 2DFT in the family. This
recursive call is launched *over the whole input word*, with a distinguished
position where the head was placed before the call. Once this computation
terminates, the control goes back to the calling transducer, and its run
continues. 

Prove that the class of functions computed by 'recursive invisible pebble'
transducers with unary output alphabets is the same as the class of functions
computed by 'rational series'.



## Linear Growth {.exercise .challenging}

Prove that the following are equivalent in the case of $\Nat$-weighted automata:

1. Weighted automata with linear growth.
2. 2DFTs with unary output.

What about the case of $\Rel$?


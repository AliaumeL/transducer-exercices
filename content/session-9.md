---
author: Aliaume LOPEZ
title: Transducers
subtitle: Linear Regular Functions
email: ad.lopez@uw.edu.pl
lang: en-GB
session: 9
date: 2024-04-29
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

# Lambda-calculus

## Basic Training {.exercise}

Write lambda-terms for the following functions:

- [ ] `lowercase`
- [ ] `expandtabs`
- [ ] `sort`
- [ ] `swap`

## How to duplicate {.exercise}

Prove that square (without underscores) is definable in the lambda calculus.

## Subject Reduction {.exercise}

Prove that (context) beta reduction and eta expansion preserve typing using the
classical *subject reduction technique*.

## What is the expressive power of the lambda-calculus? {.exercise}

Prove that the lambda-calculus using linear regular functions without squaring
is strictly less expressive than the same lambda-calculus with squaring.
What are the kind of functions computed?

# Pebble transducers

## Squaring for atoms {.exercise}

Let $f$ be the function that maps $w$ to the string $\prod_{i,j \text{ lex}}
w[i]w[j]$.

1. Prove that it is definable by an atomic pebble transducer.
2. Prove that it is not definable by an atomic $2$-pebble transducer.

### Number of outputs {.hint}

Remark that the nested transducer has a bound on the size of its ouptut.
Indeed, for any fixed $i$, if the output is too large, one letter repeats
(because of the shape of the output) a lot, which means that the head goes a
lot of time to some position, and if it is higher than the number of states,
the automata loops. As a consequence, the output is at most linear.

## Composition of pebbles ? {.exercise}

Prove that $k$-pebble transducers are not closed under composition.

### Size issues {.hint}

Just compose square twice.

## I was blind all along {.exercise}

We define *blind* models as models where the pebble cannot be read except for
the last one. In the pebble model, the machine starts in the last position of
the head of the caller and returns to this position when it pops.

1. Prove that the list of suffixes can be produced by a *blind* pebble transducer.
2. Prove that the composition of blind pebble transducers can express squaring.
3. Prove that blind pebble transducer are strictly less expressive than
   pebble transducers, because they cannot express squaring (this is quite difficult).
4. Conclude that blind pebble transducers are not closed under composition.


### Squaring by composition {.hint}

Let $f$ be the function that lists suffixes. We can post-compose $f$ to
underline the first letter of every suffix. Then, we can post-compose this
function to prepend to any underlined letter, all the underlined letters that
come before it in the reverse order. Finally, we can use a map reverse
operation to put everything in the correct ordering.


# Composition of functions

## Replacing map reverse? {.exercise}

What happens if one replaces the combinator `map-reverse`
by `square-map-reverse` in the definition of polyregular functions?

## Weaker squaring {.exercise}

What happens if we replace `square` by `square-without-underlines`
in the definition of poylregular functions?

# For Transducers 

## Bounded output {.exercise}

Prove that it is decidable whether a for-transducer has bounded
output.

## Decidability of unnested {.exercise}

Give an algorithm that decides if a for-transducer $f$
can be realised by an *unnested* for-transducer.

## For transducers with string variables {.exercise}

Prove the equivalence between for-transducers and for-transducer with string
variables having a "single-use" property, that cannot be iterated over.

# Self-reduction? {.exercise}

## Evalutation of polyregular functions {.exercise}

Let $P_{k,d}$ be the collection of for-programs with nesting at most $k$, and
using at most $d$ distinct boolean variables. Prove that the evaluation
function $e \colon P_{k,d} \times \Sigma^* \to \Gamma^*$ is polyregular. What
is the increase in the number of loops? Of pebbles?

# Reductions modulo polyregular functions

A *polyregular reduction* of a problem $A$ into a problem $B$ is a polyregular
function $f$ that maps instances of $A$ into instances of $B$, and such that $x
\in A$  if and only if $f(x) \in B$. 

## A canonical P-complete language {.exercise}

Let $A$ be the language of strings $(M,w,n)$ such that $M$ is the code of a
non-deterministic turing machine, and $M(w)$ accepts in time at most $n$, where
$n$ is written in unary.

1. Prove that the language $A$ is $NP$-complete with respect to polyregular
   reductions.
2. Prove that the SAT problem is $NP$-complete with respect to polyregular
   reductions.
3. Prove that the 3SAT problem is $NP$-complete with respect to polyregular
   reductions.



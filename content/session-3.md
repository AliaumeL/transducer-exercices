---
author: Aliaume LOPEZ
title: Transducers
subtitle: Mealy Machines
email: ad.lopez@uw.edu.pl
lang: en-GB
session: 3
date: 2024-03-04
refs: |
   ::: {#refs}
   :::
---

<!-- These are the latex command used in this document --->
\newcommand{\Nat}{\mathbb{N}}
\newcommand{\Real}{\mathbb{R}}
\newcommand{\MSO}{\mathbb{MSO}}
\newcommand{\FO}{\mathbb{FO}}

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
\newcommand{\prefleq}{\mathrel{\sqsubseteq_{\mathsf{prefix}}}}

\newcommand{\Res}{\mathsf{Res}}
\newcommand{\resi}[2]{{#2}^{-1}{#1}}

\newcommand{\lowercaseExample}{\mathsf{lowercase}}
\newcommand{\expandtabs}{\mathsf{expandtabs}}
\newcommand{\sort}{\mathsf{sort}}
\newcommand{\swap}{\mathsf{swap}}
<!-- end of the custom commands -->

# Previously, in Transducers

## Aperiodicity and Counters {.exercise}

Let $L$ be a regular language. Prove the equivalence between the following
properties.

1. The minimal DFA of $L$ is *counter-free*.
2. The syntactic monoid of $L$ is *aperiodic*.

Assume that $L$ is recognised by a *counter-free* automaton (that may not be
minimal), is $L$ *aperiodic*? What about a *non-deterministic* counter-free
automaton?

## Canonical Bimachines {.exercise}

Let us recall that the production function of a rational function $f$ can be
written $\pi_f \colon \Sigma^* \times \Sigma \times \Sigma^* \to \Gamma^*$.
Given a rational function $f \colon \Sigma^* \to \Gamma^*$, we can define two
congruences $\simeq_l$ and $\simeq_r$ over $\Sigma^*$ as follows:

$$
u \simeq_ l v
\iff
\forall x,y \in \Sigma^*,
\forall a \in \Sigma,
\forall w \in \Sigma^*,
\pi_f(xuy, a, w) = \pi_f(xvy, a, w)
$$

And similarly for $\simeq_r$.

1. Prove that $\simeq_l$ and $\simeq_r$ have finite index.
2. Construct a *canonical* bimachine computing $f$.
3. What is the complexity of the construction?

## The Great Simplification {.exercise .warmup}

Given a rational function $f$, is it decidable whether there exists a 
Mealy Machine that computes $f$?

### Use Canonical Bimachines {.hint}

Can it be that the canonical bimachine is non-trivial?

## Fixed points {.exercise .challenging}

A fixed point of a function $f$ is a value $x$ such that $f(x) = x$.
For the following models of computation, can we decide if $f$ has a fixed point?

- Mealy Machines?
- Rational Transductions?
- Two-way Deterministic Transducers with outputs?

### Partial Solution {.solution}

- Mealy Machines: Yes, because the collection of fixed points is a regular language.
- Rational Transductions: Yes, by using similar techniques as for the equivalence of rational functions.

# Logic 


## Kleene Star Stability {.exercise}

Are languages definable in first-order logic closed under kleene star?

## Examples of aperiodic languages

Write a star-free expression that defines the language $(ab)^*$.

## A single existential quantifier is enough

Show that regular languages are definable by
$\MSO$ formulas using a single existential monadic second order
quantifier.

## Word representations

Consider two ways of representing a finite word as a model: we either have the
order relation $x < y$, or we have the successor relation $x = y + 1$. Show
that for both ways, $\MSO$ gives the same expressive power. Is it true for
$\FO$?

## Monadic Colouring

Consider finite words, represented using order x < y. Show that every MSO
formula is equivalent to a formula of the form ∃Xφ(X) where φ(X) is a
first-order formula.

# Two Way Deterministic

## Examples and non-examples {.exercise .warmup}

For the following functions, provide the simplest model of computation
that can express them.

- The `reverse` function [@bojanczykToolbox, Problem 130]
- The `sort` function 
- The `cycle` function, that performs a circular permutation such, for instance
  mapping $abcd$ to $dabc$
- The `swap` function, that swaps the first two letters of a word

## 2DFTs for Languages {.exercise .warmup}

Prove that the class of languages recognised by deterministic two-way
transducers coincides with the class of languages recognised by deterministic
finite automata.

## Forward Images? {.exercise .warmup}

Let $f$ be computed by a two-way deterministic transducer with outputs, and $L$
be a regular language. Is it true that $f(L)$ is a regular language?

### The answer is no {.hint}

What about $f(L) = \setof{ a^n b^n }{ n \in \Nat}$?

## Expressiveness {.exercise .warmup}

Prove that 2DFT are more expressive than rational functions. What about
*sweeping* DFTs that can only change direction at the endpoints of the input?

## Languages and Functions {.exercise .warmup}

Show that if $f$ is recognised by a deterministic two-way transducer and $g$ is
rational (with suitable input and output alphabets), then $g \circ f$ is
recognised by a deterministic two-way transducer.
[@bojanczykToolbox, Problem 135]


## Class inclusions {.exercise .challenging}

Prove that given a function $f$ computed by a two-way deterministic transducer
with outputs, it is decidable whether $f$ is rational.


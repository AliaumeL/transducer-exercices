---
author: Aliaume LOPEZ
title: Transducers
subtitle: Two Way Transducers
email: ad.lopez@uw.edu.pl
lang: en-GB
session: 4
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
\newcommand{\prefleq}{\mathrel{\sqsubseteq_{\mathsf{prefix}}}}

\newcommand{\Res}{\mathsf{Res}}
\newcommand{\resi}[2]{{#2}^{-1}{#1}}

\newcommand{\lowercaseExample}{\mathsf{lowercase}}
\newcommand{\expandtabs}{\mathsf{expandtabs}}
\newcommand{\sort}{\mathsf{sort}}
\newcommand{\swap}{\mathsf{swap}}
<!-- end of the custom commands -->


# Previous Models 

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
4. Can you refine the construction by first minimising the left congruence, and
   then the right congruence?

This construction was used in @FIGALH2016 to prove the decidability of the
following problem: given a rational function $f$, is it decidable whether $f$
can be computed by a *star-free* bimachine?

## The Great Simplification {.exercise .warmup}

Given a rational function $f$, is it decidable whether there exists a 
Mealy Machine that computes $f$?

### Use Canonical Bimachines {.hint}

Can it be that the canonical bimachine is non-trivial?


# Logic

## Word representations {.exercise}

Consider two ways of representing a finite word as a model: we either have the
order relation $x < y$, or we have the successor relation $x = y + 1$. Show
that for both ways, $\MSO$ gives the same expressive power. Is it true for
$\FO$?

## Short Formulas {.exercise}

Prove that there exists a family of languages $L_n$ that are defined by
a formula of size $O(n)$ but such that the minimal deterministic automaton for
$L_n$ has size $\Omega(2^n)$.

### Good languages {.hint}

Consider the language $L_n$ of words of length exactly $2^n$.

### The usual trick {.hint}

Let $\varphi(x,y)$ be a first order formula.
Prove the equivalence between the two following formulas:

1. $\psi(x,y) \defined \varphi(x,z) \wedge \varphi(z,y)$.
2. $\theta(x,y) \defined \forall s,t. (s = x \wedge t = z) \vee (s = z \wedge t = y) \Rightarrow \varphi(s,t)$.

### Minimal Automaton {.hint}

How would you prove that the minimal automaton has at least $2^n$ states? Using
the Myhill-Nerode theorem for instance?

## Logic and Monoids {.exercise}

Let $q \in \Nat$ be a fixed *quantifier rank*.

1. Prove that the $\MSO^q$ theory of a word $uw$ is uniquely determined by the
   $\MSO$ theory of $u$ and $w$.
2. What about the $\FO^q$ theory?
3. Define the map $\iota \colon \Sigma^* \to \PSet{\MSO^q}$ by


# Two Way Deterministic

## Examples and non-examples {.exercise .warmup}

For the following functions, provide the simplest model of computation
that can express them.

- The `reverse` function
- The `sort` function 
- The `cycle` function, that performs a circular permutation such, for instance
  mapping $abcd$ to $dabc$
- The `swap` function, that swaps the first two letters of a word

## 2DFTs for Languages {.exercise .warmup}

Prove that the class of languages recognised by deterministic two-way
transducers coincides with the class of languages recognised by deterministic
finite automata **using monoids**.

## Forward Images? {.exercise .warmup}

Let $f$ be computed by a two-way deterministic transducer with outputs, and $L$
be a regular language. Is it true that $f(L)$ is a regular language?

### The answer is no {.hint}

What about $f(L) = \setof{ a^n b^n }{ n \in \Nat}$?

## Expressiveness {.exercise .warmup}

Prove that 2DFT are more expressive than rational functions. What about
*sweeping* DFTs that can only change direction at the endpoints of the input?

## Languages and Functions {.exercise .challenging}

Provide a direct proof of the following inclusion of classes:

$$
\mathsf{2DFA} \cdot \mathsf{Rat} 
\subseteq
\mathsf{Rat} \cdot \mathsf{2DFA}
$$

### Use a general decomposition theorem {.hint}

Every deterministic two-way transducer can be decomposed into a first rational
function that computes the *state information* about the run, followed by
a *unfold* function, that utilizes this information together with the input
word to produce the input.

## Class inclusions {.exercise .challenging}

Prove that given a function $f$ computed by a two-way deterministic transducer
with outputs, it is decidable whether $f$ is rational.
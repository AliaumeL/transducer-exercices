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

### Use the transition monoid {.hint}

Prove that the transition monoid of the minimal DFA of $L$ is
the syntactic monoid of $L$.

### Non-deterministic counter-free automaton {.hint}

Use the transition monoid to define what a *counter* should be.

### From aperiodicity to counter-freeness {.solution}

Let us assume that $A = (Q, q_0, \delta, F)$ is the minimal DFA of $L$ and that
the syntactic monoid of $L$ is aperiodic. Using the hint, we know that
$\delta_w^n$ is eventually constant for all $w \in \Sigma^*$. As a consequence,
if $q \in Q$ is such that $\delta(q, w^n) = q$, then $(\delta_w)^{kn}(q) = q$
for all $k \in \Nat$. If $k$ is large enough, then $\delta_w^{kn}
= \delta_w^{kn+1}$, and therefore $\delta_w(q) = \delta_w (\delta_w^{kn})(q)
= \delta_w^{kn} (q) = q$. We have proven that $A$ has no counters.

### From counter-freeness to aperiodicity {.solution}

Assume that the minimal DFA $A = (Q, q_0, \delta, F)$ recognising $L$ is
counter-free. Let $w \in \Sigma^*$. We will prove that the sequence
$\delta_w^n$ is eventually constant. Let $q \in Q$, there exists $i < j$ such
that $\delta_w^i(q) = \delta_w^j(q)$. Let $q' \defined \delta_w^i(q)$, then
$\delta_w^{j-i}(q') = q'$. Since $A$ is counter-free, we conclude that
$\delta_w(q') = q'$. In particular, the sequence $\delta_w^n(q)$ is eventually
constant. Now, because $Q$ is finite, the sequence $\delta_w^n$ is itself
eventually constant. And because there are finitely many functions $\delta_w$
there exists a uniform bound $N_0$ such that $\delta_w^n = \delta_w^m$ for all
$n,m \geq N_0$ and all $w \in \Sigma^*$. 

### Non-minimal counter-free automaton {.solution}

If $A$ is a counter-free automaton that recognises $L$, then the minimal DFA
recognising $L$ is also counter-free.



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

### What do you want to prove {.hint}

- Mealy Machines: Yes, because the collection of fixed points is a regular language.
- Rational Transductions: **no**.

### Solution {.solution}

For Mealy Machines, the output is letter-to-letter, so if a fixed point exists,
it must start with a transition that produces exactly the letter that is read. This means
that it has a fixed point if and only if it has a fixed point of length $1$.

For rational transductions, the problem is undecidable because it is equivalent
to the halting problem for Turing Machines. Let $M$ be a Turing Machine,
such that a configuration of $M$ terminates.

Consider the function $s_M \colon \Sigma^* \to \Sigma^*$ that maps an encoding
of a configuration of $M$ to the encoding of the successor configuration. Let
$f_M \colon \Sigma^* \to \Sigma^*$ be the rational function that maps
a sequence of configurations to the sequence of **successor** configurations, prepending
to the result the initial configuration of $M$.

A terminating run of $M$ is a fixed point of $M$. Conversely, if $f_M$ has
a fixed point, then it must be a valid run of $M$ (successor configurations are
correctly computed), and this run cannot be continued (otherwise it would not
be a fixed point). Therefore, the problem of deciding whether $f_M$ has a fixed
point is equivalent to the halting problem for $M$.


# Logic 


## Kleene Star Stability {.exercise}

Are languages definable in first-order logic closed under kleene star?

## Examples of aperiodic languages

Write a star-free expression that defines the language $(ab)^*$.

## A single existential quantifier is enough

Show that regular languages are definable by
$\MSO$ formulas using a single existential monadic second order
quantifier.

### Encode the states with padding {.hint}

If the automaton has $n$ states, then represent the state of the automaton for
positions that are multiple of $n$ using a unary encoding of the state plus
a separator. How can you then recover the intermediate transitions?

## Word representations

Consider two ways of representing a finite word as a model: we either have the
order relation $x < y$, or we have the successor relation $x = y + 1$. Show
that for both ways, $\MSO$ gives the same expressive power. Is it true for
$\FO$?

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


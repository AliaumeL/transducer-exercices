---
author: Aliaume LOPEZ
title: Transducers
subtitle: Logic of Transductions
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

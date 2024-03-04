---
title: First Homework
author: Aliaume LOPEZ
subtitle: Mealy Machines, Sequential Functions, and Variations thereof
email: ad.lopez@uw.edu.pl
lang: en-GB
session: 1
date: 2024-02-26
---

\newcommand{\Nat}{\mathbb{N}}
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


# Mealy Machines and Variations

## Flip-Flop {.exercise}

Show that a 'flip-flop' machine can be obtained by composition of 'binary flip
flop' machines. What is the minimal number of intermediate machines needed?

## Decidable {.exercise}

Show that it is decidable whether a 'sequential function' is injective.

```{=html}
::: {#refs}

:::
```

## Semantically Functional {.exercise}

Prove that the two models are equivalent, and provide effective
conversions.

1. rational functions.
2. functional relations computed by non deterministic Mealy Machines.

## Semantically Size Preserving {.exercise}

Let $f \colon \Sigma^* \to \Gamma^*$ be a 'rational function'. Show that $f$ the following
are equivalent:

1. $f$ is semantically size preserving.
2. $f$ is computable by a 'letter-to-letter rational transducer'.


### Intermediate Computational Model {.hint}

Consider the following intermediate model of computation where it is
furthermore assumed that there exists $K \in \Nat$ such that at anytime of the
run of $f$, the difference of lengths between the input read so far and the
output is at most $K$.

Show that the intermediate model is equivalent to the syntactical model.

### Finding the constant $K$ {.hint}

Show that the following function is well-defined: $\delta(p,q)$ that associates
to each pair of states $p$ and $q$ of the transducer the difference of length
induced by **any** run from $p$ to $q$.

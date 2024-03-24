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


# Logic

## MSO Workout {.exercise}

Provide MSO transductions realizing the following functions:

1. `reverse`
2. `sort`
3. `swap-first-last`
4. `duplicate`


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

## Pumping Sweeping Transducers {.exercise}

Let $f$ be computed by a sweeping transducer. Provide an appropriate pumping
lemma for $f$. Use this pumping argument to prove that `map-reverse` is not
computable using a sweeping transducer.

## Pumping 2DFTs {.exercise .challenging}

Provide a pumping lemma for 2DFTs.

## Sweeping Minimization {.exercise .challenging}

We define the *sweeping number* of a sweeping transducer the maximal number of
sweeps it performs on any input words. 

1. Prove that the *sweeping number* of a sweeping transducer is finite
2. Does there exist an algorithm that, given a transducer $T$, computes its
   sweeping number?
3. Describe an algorithm that, given a sweeping transducer $T$ and a number $k$
   with the promise that $T$ can be realized by a sweeping transducer of
   sweeping number $k$, constructs a such a transducer.
4. Given a sweeping transducer $T$ and a number $k$, is it decidable whether
   $T$ is realized by a sweeping transducer with sweeping number at most $k$?

### Use effective continuity {.hint}

Recall that if a function $f$ is computed by a 2DFT, then it is *continuous*,
and even more: effectively continuous.

# Well quasi orderings

## Well-Quasi-Ordered Image {.exercise}

Let $f$ be a function from $\Sigma^*$ to $\Gamma^*$. We say that $f$ generates
a well-quasi-order whenever $f(\Sigma^*)$ is *well-quasi-ordered* for the
factor relation. We say that $f$ generates a $k$-well-quasi-order whenever
$f(\Sigma^*)$ endowed (freely) with $k$ distinguishing colours (unary
predicates) is a well-quasi-order. Finally, we say that $f$ generates an
$\infty$-well-quasi-order whenever it generates a $k$-well-quasi-order for all
$k \in \Nat$.

1. Prove that it is not decidable whether $f$ generates a well-quasi-order when
   $f$ is computed by a 2DFT.
2. What about a bimachine? What about a Mealy Machine?
3. Prove that it is decidable whether $f$ generates an
   $\infty$-well-quasi-ordering, even in the case of a 2DFT.

# Commutative Functions

From the thesis of Gaëtan page 124. Recall what a weigthed automata is.

## Commutative Output Bimachines {.exercise}

We will restrict our attention to functions $f$ from $\Sigma^*$ to $\Nat
= \set{1}^*$. Prove that in this setting bimachines are as expressive as 2DFTs.
Theorem 5.15 cas $k = 1$ + lin functions.

## Linear Growth {.exercise}

Prove that the following are equivalent in the case of $\Nat$:

1. Weighted automata with linear growth.
2. 2DFTs with unary output.

What about the case of $\Rel$?

## Deciding Commutativity {.exercise}

Let $f$ be a function from $\Sigma^*$ to $\Gamma^*$ computed by a 2DFT.
Is it decidable whether $f$ is commutative?




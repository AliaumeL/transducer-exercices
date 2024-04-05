---
author: Aliaume LOPEZ
title: Transducers
subtitle: Linear Regular Functions
email: ad.lopez@uw.edu.pl
lang: en-GB
session: 5
date: 2024-03-18
knowledges:
    - synonyms:
        - deatomisable
        - deatomisables
    - synonyms:
        - atomic bimachine
        - atomic bimachines
    - synonyms:
        - equivariance property
    - synonyms:
        - atomic code
        - atomic codes
        - coding of atoms
        - atom coding function
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

\newcommand{\Res}{\mathsf{Res}}
\newcommand{\resi}[2]{{#2}^{-1}{#1}}

\newcommand{\lowercaseExample}{\mathsf{lowercase}}
\newcommand{\expandtabs}{\mathsf{expandtabs}}
\newcommand{\sort}{\mathsf{sort}}
\newcommand{\swap}{\mathsf{swap}}

\newcommand{\toinj}{\hookrightarrow}

\newcommand{\Atoms}{\mathbb{A}}

<!-- end of the custom commands -->


# Logic

## MSO Workout {.exercise .warmup}

Provide MSO transductions realizing the following functions:

1. `reverse`
2. `sort`
3. `swap-first-last`
4. `duplicate`


# Atomisation and Deatomisation

## Deatomisation of Bimachines {.exercise .challenging}

Let $\Atoms$ be an infinite set, and $\mathcal{S}$ be the set of permutations
of $\Atoms$. We define "atomic bimachines" with input alphabet $(\Sigma \cup
\Atoms)$ and output alphabet $(\Gamma \cup \Atoms)$ via the existence of
a finite monoid $M$ and a morphism $\mu \colon (\Sigma \cup \Atoms)^* \to M$
such that $\mu(a) = 1_M$ for all $a \in \Atoms$, together with a production
function $\pi \colon M \times (\Sigma \cup \Atoms) \times M \to (\Gamma \cup
\Atoms)^*$, satisfying the following "equivariance property" (where $\sigma \in
\mathcal{S}$ is lifted from permutations over $\Atoms$ to an action over
$(\Gamma \cup \Atoms)^*$ and $(\Sigma \cup \Atoms)^*$ in the natural way):

$$
\forall a \in \Atoms, \forall \sigma \in \mathcal{S},
\pi (m, \sigma(a), n) = \sigma(\pi(m,a,n)) \quad .
$$

An "atom coding function" is a function $c \colon \Atoms \toinj \langle 1^*
\rangle$, i.e., that maps every atom to a unique word of the form $\langle 1^k
\rangle$ for some $k \in \Nat$. We say that a function $f \colon (\Atoms \cup
\Sigma)^* \to (\Atoms \cup \Gamma)^*$ is "deatomisable" if there exists
a rational function $f^\dagger \colon (\Sigma \cup \set{ \langle, \rangle,
1})^* to (\Gamma \cup \set{ \langle, \rangle, 1})^*$ such that for all 'atomic
codes' $c \colon \Atoms \toinj \langle 1^* \rangle$, the following commutes

$$
c \circ f = f^\dagger \circ c \quad .
$$

Prove that the following are equivalent:

1. A function $f$ is 'deatomisable',
2. It is realisable by an 'atomic bimachine'.


## Atomic Bimachines {.exercise}

Prove that the following are not computable by 'atomic bimachines'.

1. The reverse function.
2. The duplicate function.
3. The "unzip" function.

Conclude that those cannot be computed by rational functions.

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

This exercise is based on the notion of *sweeping transducers*
and their study done by @BGMP15 and @BGMP16.

Let $f$ be computed by a sweeping transducer. Provide an appropriate pumping
lemma for $f$. Use this pumping argument to prove that `map-reverse` is not
computable using a sweeping transducer.

## Pumping for sweeping 2DFTs {.exercise .challenging}

Provide a pumping lemma for sweeping 2DFTs. Conclude that `map-reverse` is not
computable using a sweeping transducer.

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

1. Is it decidable whether the image of $f$ is a well-quasi-ordering when $f$
   is computedb y a 2DFT?
2. What about a bimachine? What about a Mealy Machine?
3. Prove that it is decidable whether $f$ generates an
   $\infty$-well-quasi-ordering.

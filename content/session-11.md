---
author: Aliaume LOPEZ
title: Transducers
subtitle: Monoids (finally)
email: ad.lopez@uw.edu.pl
lang: en-GB
session: 11
date: 2024-05-03
knowledges:
  - synonyms:
      - regular function
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

\newcommand{\Mat}[1]{\mathcal{M}\_{#1}}

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
\newcommand{\prefleq}{\mathrel{\sqsubseteq\_{\mathsf{prefix}}}}

\newcommand{\card}[1]{\left| #1 \right|}
\newcommand{\countval}[1]{\# #1}

\newcommand{\Res}{\mathsf{Res}}
\newcommand{\resi}[2]{{#2}^{-1}{#1}}

\newcommand{\lowercaseExample}{\mathsf{lowercase}}
\newcommand{\expandtabs}{\mathsf{expandtabs}}
\newcommand{\sort}{\mathsf{sort}}
\newcommand{\swap}{\mathsf{swap}}

\newcommand{\cbs}[2]{\mathsf{cbs}(#1,#2)}

\newcommand{\prefixes}{\mathsf{prefixes}}

\newcommand{\map}{\mathsf{map}}

\newcommand{\toinj}{\hookrightarrow}

# Monoids and MSO

## Monoids and Regularity {.exercise}

We say that a language is recognized by a finite monoid $M$ if there exists
a morphism $\mu \colon A^* \to M$ and a subset $P \subseteq M$ such that $L
= \mu^{-1}(P)$.

1. Prove that a language is regular if and only if it is recognized by a finite
   monoid.
2. Use the above result to conclude that regular languages are closed under
   the following operations:
   - union,
   - intersection,
   - complement,
   - reversal,
   - concatenation
3. Prove that the class of regular languages is closed under
   radicals $\sqrt{L} \defined \setof{ w \in A^* }{ ww \in L }$.
4. Prove that the class of regular language is closed under
   Kleene star.

## From MSO to Monoids {.exercise}

Let $\varphi$ be an $\MSO$ sentence over finite words. Prove that there exists
a monoid $M$ and a function $f : A^* \to M$ and a subset $P \subseteq M$ such
that $w \models \varphi$ if and only if $f(w) \in P$.

Can you adapt the construction in the case of $\MSO$ formulas?

### Use automata theory {.hint}

At least for the first part, you can use the fact that $\varphi$ defines
a regular language.

## From Monoids to MSO {.exercise}

Let $M$ be a finite monoid and $m \in M$. Construct an $\MSO$ formula
$\varphi_m(x,y)$ over $M^*$ that accepts all pairs $x < y$ such that the factor
$w[x:y]$ evaluates to $m$.

If the monoid is aperiodic, can you write this formula in $\FO$?

# Factorisation Forests

## Baby Factorisation Forest {.exercise}

Let $M$ be a finite monoid. Prove that there exists a constant $N$ such that
for every $w \in M^*$ with $|w| \geq N$, there exist $v_0, v_1 \in M^*$, and $u
\in M^+$ such that $w = v_0 u v_1$ and $u$ is an idempotent element of $M$.

## First-order Factorisation Forests {.exercise}

Let $M$ be a finite _aperiodic_ monoid. Prove that there exists a constant $N$
such that for every $w \in M^*$, one can build a factorisation of $w$ of depth
at most $N$, where idempotent products are replaced by _constant_ products.

## Pumping lemma for regular functions {.exercise}

Let $f$ be a [regular function]{.kref}. Prove that there exists $N \geq 0$ such
that for all $w \in A^*$ with $|w| \geq N$, there exist $v_0, v_1 \in A^*$, $u
\in A^+$, $n \geq 0$, $\alpha_0, \dots, \alpha_n \in B^*$, $\beta_1, \dots,
\beta_n \in B^+$ such that $w = v_0 u v_1$ and

$$
f(v_0 u^{X + 1} v_1) = \alpha_0 \beta_1^X
\alpha_1 \dots \beta_n^X \alpha_n  \quad ,\quad  \text{for all } X \geq 0
\quad .
$$

### Solution {.solution}

Without loss of generality, we assume that $Q = Q^\leftarrow \cup
Q^\rightarrow$, where states in $Q^\leftarrow$ are always doing left
transitions, while states in $Q^\rightarrow$ are always doing right
transitions. We define the transition monoid of $f$ as follows: $M \defined
Q \to Q$. The intended semantics is that given a state $q \in Q$, and a word
$u$, the transition performed by $u$ is given by the first state reached by $f$
outside of the word $u$.

## Efficient Query Evaluation {.exercise}

Let $q \in \Nat$. Provide a linear-time computation of a data-structure over
a word $w$ allowing for constant-time answer to $\MSO$ queries of quantifier
depth at most $q$.

### Use factorisation forests {.hint}

Construct a factorisation forest of the monoid of $\MSO^q$ types.

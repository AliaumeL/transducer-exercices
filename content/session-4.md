---
author: Aliaume LOPEZ
title: Transducers
subtitle: Two Way Transducers
email: ad.lopez@uw.edu.pl
lang: en-GB
bibliography: 
- static/bibtex/papers.bib
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

### Use Monoids Bimachines {.hint}

Prove that a rational function $f$ that satisfies $f(\varepsilon) =
\varepsilon$ can be transformed into a "monoid-bimachine" defined by a finite
monoid $M$, a surjective morphism $\mu \colon \Sigma^* \tosurj M$, and a
production map $\pi \colon M \times \Sigma \times M \to \Gamma^*$, whose
semantics is defined as follows for all words $w \in \Sigma^*$:

$$
f(w) \defined \prod_{u a v = w} \pi(\mu(u), a, \mu(v)) \quad .
$$

The production function can be generalised
to subwords as follows:

$$
\pi(m_l, w, m_r) \defined \prod_{uav = w} \pi(m_l \mu(u), a, \mu(v) m_r) \quad .
$$

Using this notation $f(w) = \pi(1_M, w, 1_M)$.

### Decompose the problem {.hint}

Can you decide if a letter-to-letter unambiguous NFA with outputs is computed
by a Mealy Machine? Can you decide if a rational function is computed by a
letter-to-letter unambiguous NFA with output?

### What about idempotents {.hint}

Let $w \in \Sigma^*$ be such that $\mu(w)^2 = \mu(w)$ ($\mu(w)$ is idempotent),
and $(m_l, m_r) \in M^2$. What can you say about $\pi(m_l \mu(w), w,
\mu(w)m_r)$?

### Construct Idempotents {.hint}

Prove using Ramsey’s theorem that for every finite monoid $M$ there exists (a
computable) $N \in \Nat$ such that for all $w \in M^*$, one can compute $w =
u_1 u_2 u_3$ such that $\mu(u_2)$ is *idempotent* -- $\mu(u_2)^2 = \mu(u_2)$
--, $|u_1| \leq N$ and $|u_3| \leq N$.

### Use Quantitative Pumping Arguments {.hint}

Assume that $f$ is computed by a letter-to-letter unambigous NFA with outputs,
then $|f(w)| = |w|$ for all $w \in \Sigma^*$. Prove that this necessary
condition is also sufficient.

To that end, notice that the map $X \mapsto \pi(m_l, w^X, m_r)$ is a function
from $\Nat$ to $\Gamma^*$ that must be size preserving, and therefore that
$|\pi(m_l\mu(w), w,\mu(w) m_r)| = |w|$. Indeed, because $\mu$ is surjective,
there exist words $(x,y) \in \Sigma^*$ such that $\mu(x) = m_l$ and $\mu(y) =
m_r$. Therefore, for $X \geq 3$,

$$
f(x w^X y) = \underbrace{\pi(1_M, xw, \mu(wy))}_{\alpha}
             \pi(\mu(xw), w, \mu(wy))^{X-2}
             \underbrace{\pi(\mu(xw), y, 1_M)}_{\beta} \quad .
$$

Use the above equation to conclude.


# Logic

## Word representations {.exercise}

Consider two ways of representing a finite word as a model: we either have the
order relation $x < y$, or we have the successor relation $x = y + 1$. Show
that for both ways, $\MSO$ gives the same expressive power. Is it true for
$\FO$?

## Short Formulas {.exercise}

Prove that there exists a family of languages $L_n$ that are defined by
a formula of size $O(n)$ but such that the minimal deterministic automaton for
$L_n$ has size $\Omega(2^n)$. What about the size of an NFA$?

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

### Colored Logic {.hint}

Define a translation of usual formulas in a *coloured logic*, where variables
are either guaranteed to be taken in $u$ or guaranteed to be taken in $w$. This
can be seen as an extra type system, or a sorted logic.

Prove that formulas in this typed logic are equivalent to boolean combinations
of formulas that have a single type (i.e., monochromatic formulas), taking care
of counting the quantifier rank of the resulting sentences.

What have you proven?

### Aperiodicity {.hint}

To prove that the monoid is *aperiodic* in the case of $\FO^q$, it suffices to
prove that given a first order sentence $\varphi$, and a word $w$, there exists
$n \in \Nat$ such that $w^n \satisfies \varphi \iff w^{n+1} \satisfies
\varphi$. We will prove the stronger statement by induction: for sentences of
quantifier rank $q$, $w^{2^q}$ and $w^{2^q + 1}$ have the same $q$-first order
types.

# Two Way Deterministic

## Examples and non-examples {.exercise .warmup}

For the following functions, provide the simplest model of computation
that can express them.

- The `reverse` function
- The `sort` function 
- The `cycle` function, that performs a circular permutation such, for instance
  mapping $abcd$ to $dabc$
- The `swap` function, that swaps the first two letters of a word

### Proof for the reverse using Monoids {.hint}

Consider a bimachine defined in terms of monoids, i.e., defined by a morphism
$\mu \colon \Sigma^* \to M$, and a production function $\pi \colon M \times
\Sigma \times M \to \Gamma^*$. Let $e_a$ be the unique idempotent in the image
$\setof{\mu(a^k)}{k \geq 1}$ and $e_b$ be the unique idempotent in the image
$\setof{\mu(b^l)}{l \geq 1}$.

Consider the (generalised) outputs $\alpha \defined \pi(e_a, a^k, e_a e_b)$ and
$\beta \defined \pi(e_a e_b, b^l, e_b)$. It is clear that
$\mathsf{reverse}(a^{Xk} b^{Yl}) = b^{Yl} a^{Xk}$, but it is also equal to $u_0
\alpha^X u_1 \beta^Y u_2$, where $u_0, u_1, u_2 \in \Gamma^*$. By considering
$Y$ large enough, we conclude that $\alpha$ is $b^k$. Similarly, we conclude
that $\beta = a^l$. However, this is absurd, since the number of $a$’s and
$b$’s are not preserved when $X \neq Y$.

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

### Reverse {.hint}

The reverse function is not rational, but can be performed using a sweeping
2DFT.

### Reverse Map {.hint}

The reverse map function is not doable by a sweeping 2DFT, but can be done by a
2DFT.

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

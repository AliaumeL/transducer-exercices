---
author: Aliaume LOPEZ
title: Transducers
subtitle: Growth Rate
email: ad.lopez@uw.edu.pl
lang: en-GB
session: 12
date: 2024-05-03
knowledges:
  - synonyms:
      - regular function
      - regular functions
  - synonyms:
      - polyblind function
      - polyblind functions
      - polyblind

  - synonyms:
      - polyblind depth
  - synonyms:
      - straight-line program
      - straight-line programs
      - straight line program
      - straight line programs
  - synonyms:
      - N-polyregular
      - N-polyregular function
  - synonyms:
      - Z-polyregular
      - Z-polyregular function
  - synonyms:
      - N-star-free
      - N-star-free function
  - synonyms:
      - Z-star-free
      - Z-star-free function
  - synonyms:
      - rational series
  - synonyms:
      - N-rational series
  - synonyms:
      - Z-rational series
  - synonyms:
      - Q-rational series
  - synonyms:
      - dimension
  - synonyms:
      - growth rate
  - synonyms:
      - ultimately N-polynomial
  - synonyms:
      - $d$-pumpable
      - $(d+1)$-pumpable

refs: |
  ::: {#refs}
  :::
---

<!-- These are the latex command used in this document --->

\newcommand{\Nat}{\mathbb{N}}
\newcommand{\Real}{\mathbb{R}}
\newcommand{\Rat}{\mathbb{Q}}
\newcommand{\Rel}{\mathbb{Z}}
\newcommand{\Complex}{\mathbb{C}}

\newcommand{\MSO}{\mathbb{MSO}}
\newcommand{\FO}{\mathbb{FO}}

\newcommand{\Span}[1][]{\mathsf{Span}_{#1}}
\newcommand{\Spec}{\mathsf{Spec}}

\newcommand{\NPoly}[1][]{\mathsf{N}\text{-}\mathsf{Poly}_{#1}}
\newcommand{\ZPoly}[1][]{\mathsf{Z}\text{-}\mathsf{Poly}_{#1}}
\newcommand{\NSF}[1][]{\mathsf{N}\text{-}\mathsf{SF}_{#1}}
\newcommand{\ZSF}[1][]{\mathsf{Z}\text{-}\mathsf{SF}_{#1}}

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

\newcommand{\ind}[1]{\mathbf{1}_{#1}}

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



# Deciding Growth of Unary Output

The goal of this longer exercise is to prove the following statement relating
the [growth rate]{.kref} of a function to its [dimension]{.kref} in a specific
case.

> Let $f$ be an 'N-polyregular function'. The following are equivalent
>
> 1. $f$ is computed by an $\MSO$-interpretation of dimension $d$.
> 2. The growth rate of $f$ is $O(n^d)$.

## Playing with unary output {.exercise}

Prove the following equivalence:

1. $f$ is 'N-polyregular' (resp. 'Z-polyregular') of 'dimension' $d$
2. $f$ is a $\Rel$-linear combination (resp. $\Nat$-linear combination) of
   of functions of the form $\countval{\varphi}$ where $\varphi$ is an
   $\MSO$-formula with at most $d$ variables.

## A non-result {.exercise}

Is the following function 'N-polyregular'? 'Z-polyregular'?

$$
f(w) \defined (\vcount[a]{w} - \vcount[b]{w})^2 \quad .
$$

## Simple operations {.exercise}

Let $f$ and $g$ be two 'N-polyregular' functions. Prove that $f \times g$ is
'N-polyregular', where $f \times g$ is defined by $(f \times g)(w) \defined
f(w) \times g(w)$. Similarly, prove that $f \otimes g$ is 'N-polyregular',
where $f \otimes g$ is defined by $(f \otimes g)(w) \defined \sum_{uv = w} f(u)
\times g(v)$.

## Alternative definition {.exercise}

Prove that for all $n \in \Nat$,
we have $\ZPoly[n+1] = \Span(\setof{ \ind{L} \otimes f }{ f \in \ZPoly[n] })$.

## Polyregular Functions and Matrices {.exercise}

Let $f$ be a 'Z-rational series' defined by a minimal representation $(I, \mu, F)$.
Let $w \in \Sigma^*$ and $\lambda \in \Spec(\mu(w))$. There exist
coefficients $\alpha_{i,j} \in \Complex$ and
words $u_1, v_1, \dots, u_n, v_n \in \Sigma^*$ such that

$$
\lambda^X
=
\sum_{i,j = 1}^n \alpha_{i,j} f(v_i w^X u_j) \quad \forall X \geq 0 \quad .
$$

To prove the statement, you can use the fact that in a minimal representation,
and therefore that  $\Span[\Rat](\setof{ \mu(w)F }{ u \in \Sigma^*})$ equals
$\Rat^n$. Similarly, for a minimal representation, $\Span[\Rat](\setof{ I\mu(w)
}{ u \in \Sigma^* })$ equals $\Rat^n$.

## Ultimately polynomial functions {.exercise}

Let $f$ be a function from $\Sigma^*$ to $\Rel$.
Prove that the following are equivalent:

1. $f$ is a 'Z-rational series' that has polynomial growth,
2. $f$ is a 'Z-rational series' that is 'ultimately N-polynomial',
3. $f$ is a 'Z-rational series' with eigenvalues in $\mathbb{U} \cup \set{0}$,
4. $f$ is a 'Z-rational series' with eigenvalues in $B(0,1)$.

Where "ultimately N-polynomial" means that for all pumping patterns, there
exists a polynomial $P$ such that 

$$
f( \alpha_0 w_1^{NX_1} \alpha_1 w_2^{NX_2}
\dots \alpha_{n-1} w_n^{NX_n} \alpha_n) = P(X_1, \dots, X_n) 
\quad \text{when the $X_i$'s 
are large enough} \quad .
$$

You may also use the following corollary of [@BERE10, Corollary  2.6 page 159] stating

> Let $f$ be a 'Z-rational series' of growth rate $O(n^d)$. Then $f$
> belongs to span of the products of at most $q + 1$ characteristic series of
> rational languages.

## Growth of Unary Output {.exercise}

Let $f$ be an 'N-polyregular function'.
Prove the following equivalences:

1. $f$ is computed by an $\MSO$-interpretation of dimension $d$,
2. $f$ is not '$(d+1)$-pumpable',
3. $f$ has 'growth rate' $O(n^d)$.

Where a function is "$d$-pumpable" if there exists a family of words such that

$$
f(\alpha_0 w_1^{X_1} \alpha_1 w_2^{X_2} \dots \alpha_{n-1} w_n^{X_n}
\alpha_n) = \Omega(|X_1 + \dots + X_n|^d) \quad . $$


To that end, you may use the forest factorisation theorem of Simon, which
states that for all 'N-polyregular' functions $f$, there exists a *regular*
function $g$ from $\Sigma^*$ to trees of bounded depth such that $f(w)
= h \circ g(w)$ where $h$ counts the number of patterns of certain shapes in
the tree.

## Growth when negative values are allowed {.exercise}

Let $f$ be a 'Z-polyregular function'.
Prove the following equivalences:

1. $f$ is computed by an $\MSO$-interpretation of dimension $d$,
2. $f$ is not '$(d+1)$-pumpable',
3. $f$ has 'growth rate' $O(n^d)$.

Use the following decomposition of $f$ into $f_\text{dep} + f_{\text{indep}}$
where $f_{\text{dep}}$ counts *independent* tuples of variables, and
$f_{\text{indep}}$ counts *dependent* tuples of variables. Then, conclude by
induction.

# Compression

## Straight line program evaluation {.exercise}

Let $e$ be the evaluation function from [straight line programs]{.kref} to
strings. Is $e$ a polyregular function?

### Solution {.solution}

The function $e$ is not polyregular, because $e$ can have exponential size
output, for instance by compressing $a^n$ into $O(\log(n))$ operations.

## Efficient compression {.exercise}

What is the minimal size (number of instructions) needed to express
$\prefixes(a^n)$ as a [straight line program]{.kref}?

### What about variables containing two hashes? {.hint}

Let $x_i$ be a variable in a [straight line program]{.kref} that evaluates to
$\prefixes(a^n)$ and that contains a string with two hashes. Can it be used
twice?

### Solution {.solution}

We prove that a [straight line program]{.kref} that evaluates to a factor of
$\prefixes(a^n)$ having $k$ hashes must contain at least $k$ variables
evaluating to words containing at least two hashes.

Let us first remark that every variable in the straight line program containing
more than one hash can only be used once, as otherwise the output word contains
two hash-separated words of the same size, which contradicts the definition of
$\prefixes(a^n)$.

For the base case, if the factor contains at least one hash, then the [straight
line program]{.kref} must contain at least one instruction.

For the induction, let $x_\ell$ be the last variable of the straight line
program. It cannot be a constant assignment because the factor contains at
least two hashes. Therefore, $x_\ell = x_i x_j$ for some $i,j < \ell$. By the
induction hypothesis, $x_i$ and $x_j$. If $x_i$ contains at least two hashes,
then it can only be used once, and $x_i \neq x_j$, otherwise, $x_j$ contains a
factor of $\prefixes(a^n)$ with at least $k$ hashes, but of smaller size and we
proceed by induction. Now, because $x_i$ and $x_j$ are distinct variables, and
because every variable containing at least two hashes can only be used once, we
can partition the variables of the straight line program into three sets: the
ones containing at most one hash, the ones containing at least two hashes used
to build $x_i$, and the ones containing at least two hashes used to build
$x_j$. Using the induction hypothesis we conclude as desired.

## Straight-line homomorphic programs {.exercise}

A function $f$ is _straight-line homomorphic_ if there exists a _polynomial
time algorithm_ $P$ such that for all straight line program $X$, $f(e(X)) =
e(P(X))$, where $e$ is the expansion function.

1. Prove that $\prefixes$ is not straight-line homomorphic.
2. Prove that [regular functions]{.kref} are straight-line homomorphic.

### Proof of the first implication {.solution}


It is clear that $\prefixes$ is not straight-line homomorphic because
$\prefixes(a^n)$ cannot be compressed in less than $n$ instructions, while
$a^n$ can be compressed in $O(\log(n))$ instructions. If $\prefixes$ were
straight-line homomorphic, then the compression of $\prefixes(a^n)$ would be
doable in $O(P(\log(n)))$ instructions.

### Sketch of the second implication using Monoids {.solution}

For the second part. Let $f$ be computed by a copyless SST with states $Q$,
registers $\set{1, \dots, n}$, and output function $F$. The sketch of the proof
is as follows: we construct the transition monoid of the SST, and prove that we
can encode it inside a straight line program.

To a word $w$ we associate the function from $Q \times (\Gamma^*)^n \to
Q \times (\Gamma^*)^n$ that maps a state $q$ and a tuple of registers $r$ to
the state $q'$ and the tuple of registers $r'$ that the SST would be in after
reading $w$ starting in state $q$ and with registers $r$. Note that this monoid
is finitely generated, but is not finite, because of the unbounded
values in the registers.

However, the program is *copyless*, meaning that the value in a register is
a function of the form $r_i' \leftarrow \alpha_0 r_{j_0} \alpha_1 r_{j_1}
\dots$ where the $\alpha$'s are constants in $\Gamma^*$, and the indices $j_k$
are distinct. In particular, since we can only use each register once, we have
at most $n+1$ words $\alpha_0, \dots, \alpha_n$ in the update function.

Now, we will encode the transition of a word $w$ in a straight line program by
using variables $y_{i,q,r}$ that encode the $i$th word $\alpha$ in the update
function of the register $r$ after reading $w$ if starting in state $q$.
These can be composed to simulate the transition of the SST on the input word.

This new straight-line program is constructed in polynomial time.

### Proof of the second implication using Krohn–Rhodes decompositions {.solution}

Remark that functions that can be efficiently evaluated over compressed strings
are closed under composition. Therefore, it is enough to prove that the
basic functions in a Krohn–Rhodes decomposition can be evaluated efficiently.

It is clear that any homomorphism can be efficiently evaluated. For mealy
machines, it is very simple, as one can encode the transition monoid inside the
decomposition. For map-duplicate and map-reverse, a simple straight-line
program can be constructed.


# Cheat-Sheet

## Rational Series {.def}

Recall that a "rational series" is a triple $(I, \mu, F)$ where $I$ is a
vector of initial values, $\mu$ is a matrix of transitions, and $F$ is a vector
of final values. The function $f$ associated to the rational series is defined
by

$$
f(w) \defined I \mu(w) F \quad .
$$

If the coefficients are restricted to belong to $\Nat$, $\Rel$ or $\Rat$, we
call them respectively "N-rational series", "Z-rational series", and
"Q-rational series".

## Grwoth rate {.def}

Let $f \colon \Sigma^* \to \Gamma^*$, its "growth rate" is a function that maps
$n \in \Nat$ to the maximal value of $\card{f(w)}$ for $w \in \Sigma^n$.

## Dimension {.def}

In this exercise sheet, an interpretation of "dimension" $d$ is an
$\MSO$-interpretation where the maximal arity of the polynomial functor
describing the domain is $d$.

## Z-Polyregular Functions {.def}

A function $f$ is "Z-polyregular" if there exists a polyregular function $g
\colon \Sigma^* \to \set{-1,+1}^*$ such that $f(w) = \sum(g(w))$ for all $w \in
\Sigma^*$. If the function $g$ has outputs in $\set{1}^*$, then it is called
"N-polyregular". Furthermore, if the function $g$ is _star-free_ (i.e.,
_first-order_) then we say that $f$ is "Z-star-free" (resp. "N-star-free").

This provides us with the following table of functions

|               | $\set{-1,+1}^*$          | $\set{1}^*$              |
| ------------- | ------------------------ | ------------------------ |
| _Polyregular_ | Z-polyregular ($\ZPoly$) | N-polyregular ($\NPoly$) |
| _Star-free_   | Z-star-free ($\ZSF$)     | N-star-free ($\NSF$)     |

## Straight line program {.def}

A "straight line program" over an alphabet $\Sigma$ is a finite sequence of
instructions of the form $x_i := u$ where $u$ is a single letter, or $x_i :=
x_j x_k$ with $i > j,k$. The value of a straight line program is the value of
the last variable.

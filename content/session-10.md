---
author: Aliaume LOPEZ
title: Transducers
subtitle: One proof done well (hopefully)
email: ad.lopez@uw.edu.pl
lang: en-GB
session: 10
date: 2024-04-29
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

# Blind again

## Pumping lemma for regular functions {.exercise}

Let $f$ be a [regular function]{.kref}. Prove that there exists $N \geq 0$ such
that for all $w \in A^*$ with $|w| \geq N$, there exist $v_0, v_1 \in A^*$, $u
\in A^+$, $n \geq 0$, $\alpha_0, \dots, \alpha_n \in B^*$, $\beta_1, \dots,
\beta_n \in B^+$ such that $w = v_0 u v_1$ and 

$$
f(v_0 u^{X + 1} v_1) = \alpha_0 \beta_1 X
\alpha_1 \dots \beta_n X \alpha_n \quad  \text{for all} X \geq 0
\quad .
$$

### Idempotent transition monoid {.hint}

Look at idempotent words in the transition monoid of the function $f$.

### Self-contained proof {.solution}

One version of the full proof is given by [@Gaetan2023, Proposition 2.16]. 

## Prefixes is not blind {.exercise}

Our goal is to prove that the function `prefixes` is not computable by a 
[polyblind function]{.kref}.

1. Let $f_1, \cdots, f_n$ be regular functions. Is it possible that $f_1(w)
   f_2(w) \cdots f_n(w)$ computes a factor of $\prefixes(w)$ with a number of
   hashes that tends to $+\infty$ as $|w|$ grows?
2. Let $f$ be a regular function. Is it possible that $f(w)^{|w|}$ computes a
   factor of $\prefixes(w)$ with a number of hashes that tends to $+\infty$ as
   $|w|$ grows?
3. Using an induction on the [polyblind depth]{.kref} and leveraging the
   pumping lemma of [regular functions]{.kref} prove that the function
   $\prefixes$ is not polyblind.

### For the first {.hint}

Note that $f_1(w) \dots f_n(w)$  is of linear output size.

### For the second {.hint}

Notice that if $f(w)$ outputs a word with at least two hashes, then $f(w)^2$
cannot be a factor of $\prefixes(w)$. If it has only one hash, then $f(w)^X =
(f(w)^2)^{X/2}$ and we conclude similarly for even $X$s.

### For the third {.hint}

The statement is clear for regular functions. Let us now consider a function
obtained by a [composition by substitution]{.kref}. Leveraging the pumping
lemma for regular functions, conclude that some factor of $\prefixes(w)$ should
be computed by a function lower [polyblind depth]{.kref}.

### Self-contained proof {.solution}

A complete proof of the result can be found in [@Gaetan2023, Proposition 3.14].

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

A function $f$ is *straight-line homomorphic* if there exists a *polynomial
time algorithm* $P$ such that for all straight line program $X$, $f(e(X)) =
e(P(X))$, where $e$ is the expansion function.

1. Prove that $\prefixes$ is not straight-line homomorphic.
2. Prove that [regular functions]{.kref} are straight-line homomorphic.

### Solution {.solution}

It is clear that $\prefixes$ is not straight-line homomorphic because
$\prefixes(a^n)$ cannot be compressed in less than $n$ instructions, while
$a^n$ can be compressed in $O(\log(n))$ instructions. If $\prefixes$ were
straight-line homomorphic, then the compression of $\prefixes(a^n)$ would be
doable in $O(P(\log(n)))$ instructions.

--- 

For the second part. Let $f$ be computed by a copyless SST with states $Q$,
registers $\set{1, \dots, n}$, and output function $F$.
We construct our program $P$ as follows.

For every states $q_1, q_2 \in Q$, for every variable $x_i$ in the straight
line program for the input word, for every register $r \in \set{1, \dots, n}$,
we create two variables $y_{i,q_1,r,\text{in}}$ and $y_{i,q_2,r,\text{out}}$.
These are meant to encode the transitions of the SST on the word $x_i$ if it
were to start in state $q_1$, and end up in state $q_2$, with initial values of
the registers being $y_{i,q_1,r,\text{in}}$, and with the final values of the
registers (after reading $x_i$) stored in $y_{i,q_2,r,\text{out}}$.

Now, it is easy to write the straight line program that uses these variables to
simulate the SST on the input word. For a single letter $x_i \defined a$, this
is just a transition of the SST. For a concatenation $x_i \defined x_j x_k$, we
use the intermediate variables $y_{j,q_1,r,\text{out}}$ to simulate the
transition of the SST on $x_j$, and then use the intermediate variables
$y_{k,q_2,r,\text{in}}$ to simulate the transition of the SST on $x_k$.

This new straight-line program is constructed in polynomial time.

# Cheat-Sheet 

## The prefixes function {.def}

The prefixes function is defined inductively as follows $\prefixes(w)$ is the
list of non-empty prefixes of $w$ separated by hashes. For instance,
$\prefixes(abc) = a \# ab \# abc$.

## Composition by substitution {.def}

Let $f$ be a function from $\Sigma^*$ to $\set{1,\dots,k}^*$,
and $g_1, \dots, g_k$ be functions from $\Sigma^* \to \Gamma^*$.
The "composition by substitution" of $f$ by $g_1, \dots, g_k$ is the function

$$
\cbs{f}{g_1, \dots, g_k}(w) = \map(\lambda x. g_x (w)) (f(w)) \quad .
$$


## Polyblind functions {.def}

The class of "polyblind" functions is defined as the smallest class of
functions containing the regular functions and closed under composition by
substitution. The "polyblind depth" of a function is the smallest $k$ such that
the function can be obtained by composition by substitution of nesting depth at
most $k$.

## Straight line program {.def}

A "straight line program" over an alphabet $\Sigma$ is a finite sequence of
instructions of the form $x_i := u$ where $u$ is a single letter, or $x_i :=
x_j x_k$ with $i > j,k$. The value of a straight line program is the value of
the last variable.

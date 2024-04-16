---
author: Aliaume LOPEZ
title: Transducers
subtitle: Linear Regular Functions
email: ad.lopez@uw.edu.pl
lang: en-GB
session: 7
date: 2024-04-08
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

\newcommand{\toinj}{\hookrightarrow}

# Combinators

## Playing with combinators {.exercise .warmup}

Write the following functions using the combinators
and prime functions for regular functions.

1. The identity map.
1. $f_1 \colon w \mapsto ww$.
2. $f_2 \colon (ab)^n \mapsto a^n b^n$ and does
   *anything* on inputs that do not belong to $(ab)^*$.

## Size restrictions {.exercise .warmup}

Let $f \colon X \to Y$ be a function that can be expressed using the
combinators. We define inductively the size of an element in $X$ as you would
expect. Prove that the size of $f(x)$ is bounded by an affine function on the
size of $x$.

## Higher order constructors {.exercise .warmup}

Representing booleans as $\mathbb{B} \defined 1 + 1$, 
write the following functions:

1. The map $\land \colon \mathbb{B}^2 \to \mathbb{B}$,
2. The map $\lor \colon \mathbb{B}^2 \to \mathbb{B}$,
3. The map $\mathsf{if} \colon \mathbb{B} \times X \times X \to X$,
4. The map $\mathsf{any} \colon \mathbb{B}^* \to \mathbb{B}$,
5. The map $\mathsf{all} \colon \mathbb{B}^* \to \mathbb{B}$.

## Internal regular languages {.exercise .warmup}

Write a function $f \colon \Sigma^* \to \mathbb{B}$
that recognizes the language $(ab)^*$.


## Binding of variables {.exercise .warmup}

Write a function $f \colon xwy \mapsto (xy)^{|w|}$, where $x$ and $y$ are
letters. Is it possible to define the function $g \colon (u,w) \mapsto
u^{|w|}$?


# Previously

## Recursive Invisible Pebbles {.exercise .challenging}

We define a "recursive invisible pebble" transducer as follows: it is
a collection of 2DFTs over the same input alphabet $\Sigma$ and the same output
alphabet $\Gamma$, where the transitions are defined as usual, except that some
transitions can perform a *recursive call* to another 2DFT in the family. This
recursive call is launched *over the whole input word*, with a distinguished
position where the head was placed before the call. Once this computation
terminates, the control goes back to the calling transducer, and its run
continues. 

Prove that the class of functions computed by 'recursive invisible pebble'
transducers with unary output alphabets is the same as the class of functions
computed by 'rational series'.



## Linear Growth {.exercise .challenging}

Prove that the following are equivalent in the case of $\Nat$-weighted automata:

1. Weighted automata with linear growth.
2. 2DFTs with unary output.

What about the case of $\Rel$?

## Minimising growth {.exercise .challenging}

Recall that in $\MSO$-transductions, we introduced a duplication function
$d_{\alpha, \beta}$ that maps $w$ to $\diamond^\beta \prod_{i = 1}^{|w|} w_i
(\#)^{\alpha - 1}$. Any regular function is written as the composition of an
$\MSO$-intepretation (without copies) with a duplication. As a consequence,
$|f(w)| \leq \alpha |w| + \beta$ for some $\alpha, \beta \in \Nat$.

Question: assume that there exists $\alpha', \beta' \in \Nat$ such that $|f(w)|
\leq \alpha' |w| + \beta'$ for all $w$. Is it possible to represent $f$ using
$d_{\alpha',\beta'}$ followed by an $\MSO$-intepretation.


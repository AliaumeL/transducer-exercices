---
author: Aliaume LOPEZ
title: Transducers
subtitle: One proof done well (hopefully)
email: ad.lopez@uw.edu.pl
lang: en-GB
session: 10
date: 2024-04-29
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

# Blind again

## Prefixes is not blind {.exercise}

Following the proof of Gaëtan. TODO. write it up.

Our goal is to prove that the function `prefixes` is not computable by a blind
transducer.

1. Prove that blind transducers are equivalently described by a *composition by
   substitution* operation.
1. Let $f$ be a *regular* function. Prove that there exists $u,v,w \in
   \Sigma^*$ with $w$ non-empty such that $f(u w^X v)$ is a finite product of
   (pumping argument)
1. Conclude.

# Compression

A *straight line program* is a sequence of instructions of the form $x_i := u$
where $u$ is a finite string, or $x_i := x_j x_k$ with $i > j,k$. The value of
a straight line program is the value of the last variable.

## Straight line program evaluation {.exercise}

Let $e$ be the evaluation function, from straight line programs to strings.
Is $e$ a polyregular function?

## Straight-line homomorphic programs {.exercise}

A function $f$ is *straight-line homomorphic* if there exists a *polynomial
time algorithm* $P$ such that for all straight line program $X$, $f(e(X)) =
e(P(X))$, where $e$ is the expansion function.

1. Prove that rational functions are straight-line homomorphic.
2. Prove that regular functions are straight-line homomorphic.
3. Prove that the *squaring* function is not straight-line homomorphic.

---
title: Second Homework
author: Aliaume LOPEZ
subtitle: Polyregular Functions
email: ad.lopez@uw.edu.pl
lang: en-GB
session: 2
date: 2024-04-30
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

\newcommand{\zip}{\mathsf{zip}}

\newcommand{\Res}{\mathsf{Res}}
\newcommand{\resi}[2]{{#2}^{-1}{#1}}

\newcommand{\lowercaseExample}{\mathsf{lowercase}}
\newcommand{\expandtabs}{\mathsf{expandtabs}}
\newcommand{\sort}{\mathsf{sort}}

\newcommand{\growth}{\mathsf{growth}}
\newcommand{\swap}{\mathsf{swap}}

::: ics-todo
# Add to your calendar 

- **Due:** 2024-06-03 18:15 CET
- **Organizer:** <mailto:ad.lopez@uw.edu.pl>
- **Summary:** MIMUW Transducer Course Homework 2
- **Url:** <https://www.irif.fr/~alopez/ressources/teaching/mimuw-2024/homework-2.pdf>

--- 

This homework is due for the 3nd of June, 18:15 GMT+1. It should be sent to
<ad.lopez@uw.edu.pl>. Exercises are independent, and can be skipped without
penalty. Failure to deliver the homework in due time is heavily penalized. 

Please submit your homework in PDF format, and make sure to include your name
and student identifier in the document. Every exercise should be present in
your copy, if you fail to solve an exercise, please write "I couldn't solve
this exercise" and move on to the next one. 

The answers should be written in English. Please keep the answers concise and
precise. Please separate statements from proofs in your answers, and provide a
proof (even a short one) for every statement made. Handwaving proofs are not
accepted. Proofs by intimidation are not accepted. Proofs by obfuscation are
not accepted.

:::

# Mandatory Exercises

## Invertible functions {.exercise}

Let $f \colon \Sigma^* \to \Gamma^*$ be an *injective function*. Is it true
that if $f$ is *linear regular*, then so is the partial inverse $f^{-1}$? What
about *polyregular*?

## Context-free languages {.exercise}

Let $L$ be a context-free language, and $f$ be a polyregular function.
Is it decidable whether $f^{-1}(L) \neq \emptyset$?

## Image Intersection {.exercise}

Let $f_1$ and $f_2$ be two polyregular functions from $\Sigma^*$ to $\Gamma^*$.
Is it decidable whether $\im{f_1}{\Sigma^*} \cap \im{f_2}{\Sigma^*}
= \emptyset$?

## Image of linear regular {.exercise}

Let $f$ be a *linear regular* function from $\Sigma^*$ to $\Gamma^*$. We define
$\mathsf{growth}_f(n)$ to be the maximum among all words $w \in \Sigma^{\leq
n}$ of the length of $f(w)$.
Prove that one of the following holds:

1. The function $\growth_f$ is *bounded*.
2. There exists a $\alpha > 0$, for large enough $n \in \Nat$,  $\growth_f (n)$ is at least $\alpha n$.

## Polyregular Reductions {.exercise}

Consider two decision problems (which is the same thing as a language) $A
\subseteq \Sigma^*$ and $B \subseteq \Gamma^*$. A polyregular
reduction from a problem $A$ to a problem $B$ is a polyregular function $f
\colon \Sigma^* \to \Gamma^*$ such that for all $w \in \Sigma^*$, $w \in A$ if
and only if $f(w) \in B$. 

We write boolean formulas as strings over the alphabet $\Sigma \defined \set{a,
\neg, \land, \lor, (, )}$. Variables are encoded as $a^n$ for some $n$. For
instance, $(a \land \neg( aa \vee aaaa))$ is a valid formula which uses three
variables $a$, $aa$ and $aaaa$. The language of valid formulas is given by the
following grammar: $F \mapsto ( F \land F ) \mid ( F \lor F ) \mid \neg F \mid
V$ and $V \mapsto aV \mid a$. In particular, valid formulas are
*well-bracketed* expressions.


We call $\mathsf{SAT}$ the list of satisfiable boolean formulas written over
this alphabet. We call $\mathsf{CNFSAT}$ the list of satisfiable boolean formulas
where the formula is in *conjunctive normal form* (CNF), that is, it is a
conjunction of disjunctions of variables or their negations.

Construct a polyregular reduction from $\mathsf{SAT}$ to $\mathsf{CNFSAT}$.


# Optional Exercises 🏆

The optional exercises are listed in the webpage
<https://aliaumel.github.io/transducer-exercices/hall-of-fame.html>. There are
plenty of exercises to choose from, and you can select any of them to solve. We
divide the number of points given by the number of contestants that provided
a solution, so choose wisely.

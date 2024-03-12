---
title: First Homework
author: Aliaume LOPEZ
subtitle: Mealy Machines, Sequential Functions, and Variations thereof
email: ad.lopez@uw.edu.pl
lang: en-GB
session: 1
date: 2024-03-11
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
\newcommand{\swap}{\mathsf{swap}}

::: ics-todo
# Add to your calendar 

- **Due:** 2024-04-02 18:15 CET
- **Organizer:** <mailto:ad.lopez@uw.edu.pl>
- **Summary:** MIMUW Transducer Course Homework 1
- **Url:** <https://www.irif.fr/~alopez/ressources/teaching/mimuw-2024/homework-1.pdf>

--- 

This homework is due for the 2nd of March, 18:15 GMT+1. It should be sent to
<ad.lopez@uw.edu.pl>.
Exercises are independent, and can be skipped without penalty. Failure to
deliver the homework in due time is heavily penalized. 

Exercises without a $\star$ symbol are *mandatory* and should be attempted by
everyone. Exercises with a $\star$ symbol are *optional* and will be rewarded
by extra points.

:::

# Mealy Machines and Variations

## Continuous {.exercise .warmup}

Is the `zip` function continuous? Where `zip(w1 # w2)` is defined inductively as follows

$$
\begin{aligned}
\zip (au \# bv) &= a b \zip (u \# v) \\
\zip (\varepsilon \# v) &= v \\
\zip (u \# \varepsilon) &= u \\
\zip (\varepsilon \# \varepsilon) &= \varepsilon \\
\end{aligned}
$$

## Flip-Flop {.exercise .warmup}

Show that a flip-flop machine can be obtained by composition of binary flip
flop machines. What is the minimal number of intermediate machines needed?

## Decidable {.exercise .warmup}

Show that it is decidable whether a rational function is injective.
Can you provide an upper bound on the complexity of the decision problem?

### How was decidability of equivalence proven? {.hint}

Recall that the decidability of equivalence between two rational functions was
obtained in the lecture by constructing a language of *counterexamples to
equivalence* and proving that this language was context-free.

## $\star$ Windowed Transducers {.exercise .challenging}

A Mealy machine is called *windowed* if there exists a constant $K \in \Nat$
such that the output of the machine on a given input letter only depends on the
letters at distance at most $K$ from the input letter.

1. Provide an example of a Mealy Machine that is not windowed.
2. Is it decidable whether a Mealy Machine is windowed?

The definition of *windowed* generalizes naturally to unambiguous NFAs with
output where every transition is labelled by a single output letter, called
unambiguous NFAs  with letter-to-letter output.

3. Is it decidable whether an unambiguous NFA with letter-to-letter output is
   windowed?




# Semantic properties

## Semantically Functional {.exercise .warmup}

Prove that the two models are equivalent, and provide effective
conversions.

1. unambiguous NFA with output (i.e. rational functions)
2. NFA with output which are functional (i.e., for every input, there is exactly one output, which might arise from different runs)



## $\star$ Semantically Size Preserving {.exercise .challenging}

Prove that the following two subclasses of rational functions are equivalent
and provide effective conversions:

1. unambiguous NFA with output where every transition is labelled by exactly
   one output letter.
2. unambiguous NFA with output where for every input word, the output has the
   same length as the input. 


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

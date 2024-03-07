---
author: Aliaume LOPEZ
title: Transducers
subtitle: Mealy Machines
email: ad.lopez@uw.edu.pl
lang: en-GB
session: 2
date: 2024-03-04
knowledges:
    - synonyms:
        - graph
    - synonyms:
        - regular language
    - synonyms:
        - code
    - synonyms:
        - prefix code
    - synonyms:
        - code with bounded delay
    - synonyms: 
        - Mealy Machine
        - closed subsets
    - synonyms:
        - regular topologies
        - regular topology
    - synonyms:
        - continuous
    - synonyms:
        - sequential transducer
        - sequential
        - sequential function
    - synonyms:
        - impure sequential function
    - synonyms:
        - rational function
    - synonyms:
        - code with bounded delay
    - synonyms:
        - topology
    - synonyms:
        - Lipschitz
    - synonyms:
        - prefix distance
    - synonyms:
        - prefix preserving functions
        - preserves prefixes
        - prefix preserving
refs: |
   ::: {#refs}
   :::
---

<!-- These are the latex command used in this document --->
\newcommand{\Nat}{\mathbb{N}}
\newcommand{\Real}{\mathbb{R}}
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

\newcommand{\Res}{\mathsf{Res}}
\newcommand{\resi}[2]{{#2}^{-1}{#1}}

\newcommand{\lowercaseExample}{\mathsf{lowercase}}
\newcommand{\expandtabs}{\mathsf{expandtabs}}
\newcommand{\sort}{\mathsf{sort}}
\newcommand{\swap}{\mathsf{swap}}
<!-- end of the custom commands -->

# Continuity. Again.

## It is cake? {.exercise .warmup}

Let $\Sigma$ and $\Gamma$ be two alphabets. Prove or disprove that the
following functions are 'continuous' for the 'regular topologies'
on $\Sigma^*$ and $\Gamma^*$:

- [ ] The map $w \mapsto w w$
- [ ] The map $w \mapsto w^{|w|}$
- [ ] The map $w \mapsto \odot_{i = 1}^{|w|} \left( w_{< i} \bar{w_i} w_{> i} \# \right)$
- [ ] A function $f \colon \Sigma^* \to \set{1}^*$ that is
  increasing and such that $\im{f}{\Sigma^*} \subseteq 
  \setof{n!}{n \in \Nat}$.
- [ ] The map $w \mapsto \odot_{i = 1}^{|w|} w_{< i}$.
 

## A Graph Property {.exercise}

Let $f \colon \Sigma^* \to \Gamma^*$ be a function preserving lengths. Prove
that the following are equivalent:

1. The 'graph' of $f$ is a 'regular language',
2. $f$ can be computed by a 'Mealy Machine' with regular lookahead.

### Simple conversions {.hint}

Transform transitions of the form $p \to^{a/b} q$ into transitions of the form
$p \to^{(a,b)} q$. I.e., use the fact that $Q \times (\Sigma \times \Gamma) \to
Q \subseteq (Q \times \Sigma) \times (Q \times \Gamma)$.

### Semantic and Syntaxic Unabmiguity {.hint}

To convert a 'graph' into a 'Mealy Machine' with regular lookahead, start from
a *deterministic* finite automaton that recognizes the graph.


### Solution for the easy implication {.solution}

Consider a 'Mealy Machine' with regular lookahead. It is defined as $T \defined
(Q, q_0, \delta, \lambda)$. Let us write $A \defined (Q, q_0, \delta', Q)$
where $\delta'(q, (a,b)) = \delta(q,a)$ if $\lambda(q,a) = b$, and is undefined
otherwise. An easy induction on the size of the input shows that $A$ recognizes
exactly the graph of $f$.

### Solution for the hard implication {.solution}

For simplicity, let us start with a *deterministic* and *co-deterministic*
finite automaton $A \defined (Q, q_0, \delta, F)$ that recognizes the 'graph'
of $f$. Define the following 'Mealy Machine' $T \defined (Q, q_0, \delta',
\lambda')$, where $(q,a,q') \in \delta'$ if and only if there exists $b \in
\Gamma$ such that $\delta(q,(a,b)) = q'$ in $A$, and $\lambda(q,a,q') = b$
where $b$ is the unique letter in $\Gamma$ such that $\delta(q,(a,b)) = q'$
(because the automaton is co-deterministic).

It is an easy induction on the size of the input to prove that $T$ computes
$f$, i.e., that accepting runs produce $f(w)$. Let us now prove that $T$ is
unambiguous. Assume that two runs $\rho, \theta \in Q^*$ of $T$ are accepting
on a given word $w$. To each of these runs, one can associate a word $u$ and
$v$, both in $\Gamma^*$, and such that $\delta(\rho_i, w_{i+1}, u_{i+1})
= \rho_{i+1})$ for $0 \leq i < |w|$ (and similarly for $\theta$). Because both
runs are accepting, and since $T$ produces $f(w)$, we conclude that $u
= v = f(w)$. In particular, we can now use the fact that $A$ is deterministic
to conclude that $\rho = \theta$.

# Sequential Functions {.exercise}

## Sequential Functions and Forward Images {.exercise}

Prove that the image of a rational language through a 'sequential function' is
a rational language. Is it true for rational functions?

Is the function $f$ that maps to a binary encoded number $n$ its square $n^2$
a 'sequential function'?

## Sequential Functions and Topology {.exercise .warmup}

Prove that the function $(\times 3)$ that maps a binary encoded number $n$ to
its triple $3n$ is not a 'sequential function'.

### Use the topological characterization {.hint}

Recall that a 'sequential function' is 'continuous', and 'Lipschitz' for the
'prefix distance'.


## Injectivity, fixedpoints {.exercise .challenging}

For the following models, is injectivity decidable?
Is the property of having a fixed point decidable?

1. Mealy Machines
2. Rational transductions
3. Sequential Functions


## Is it a code? {.exercise .warmup}

Are the following functions sequential?

1. The *relation* $\beta_1^{-1}$ where $\beta_1 \colon \set{x,y}^* \to
   \Sigma^*$ is defined by $\beta_1(x) = a$, $\beta_1(y) = aba$?
2. The *relation* $\beta_2^{-1}$ where $\beta_2 \colon \set{x,y,z}^* \to
   \Sigma^*$ is defined by $\beta_2(x) = ab$, $\beta_2(y) = abb$, and
   $\beta_2(z) = baab$?

## Coding and Decoding {.exercise}

Let $\beta \colon \Gamma^* \to \Sigma^*$  be a morphism.
Prove that the following are equivalent:

1. The set $X \defined \im{\beta}{\Gamma^*}$ is a 'code with bounded delay'
2. The function $\beta^{-1}$ is an 'impure sequential function'.

### Start with sequential functions {.hint}

Show that if $X$ is a prefix code (no two words of $X$ are related by the
prefix relation), then $\beta^{-1}$ is a 'pure sequential function'.

## Continuous functions ... {.exercise}

Let $\Sigma \defined \set{0,\dots,9}$ and $f \colon \Sigma^* \to \Sigma^*$ be
a 'rational function'. To a word $u \in \Sigma^*$, we associate the number
$\bar{u} \defined \sum_{i = 1}^{|u|} u_i 10^{-i}$. This allows us to lift the
usual distance on $\Real$ to $\Sigma^*$ by defining $d(u,v) \defined |\bar{u}
- \bar{v}|$.

Can you provide sufficient conditions for $f$ to be 'continuous' in this new
topology?
 
# Homework


## String Manipulation {.exercise}

Let $\Sigma$ be a fixed finite alphabet, and $E$ be a finite set of rules of
the form $u \to v$ where $u,v \in \Sigma^*$. Can you think about a method to
obtain a transducer that realizes the "search and replace" operations defined
by $E$? What about the case where patterns overlap? What happens if we allow
for rules defined by regular expressions?

\clearpage

# Cheat Sheet {.cheat-sheet}

## Codes 

### Codes with Bounded Delay {.def}

Let us write $\Gamma \defined \set{x_1, \dots, x_n}
= X$. By definition, $X$ is a "code" if the map $\beta \colon \Gamma^* \to
\Sigma^*$ defined by $\beta(x_i) = x_i$ is injective.

A set $X \subseteq \Sigma^*$ is a "prefix code" if no word of $X$ is a prefix
of another word of $X$. 

A "code with bounded delay" $d$ is a code $X$ such that for all $u \in
\Gamma^{d+1}$, for all $v \in \Gamma^*$ if $\beta(u) \prefleq \beta(v)$ then
$u_1 = v_1$.

## Machines

### Regular Language {.def}

A "regular language" is a language that is recognized by a deterministic finite
automaton.

### Mealy Machine {.def}

Let $\Sigma$ and $\Gamma$ be two alphabets.
A "Mealy Machine" $\mealy{M}$ is a tuple $(q_0, Q, \delta, \lambda)$ 
such that

1. $Q$ is a finite set of *states*.
2. $q_0 \in Q$ is the *initial state*.
3. $\delta \colon Q \times \Sigma \to Q$ is a
   *transition function*.
4. $\lambda \colon Q \times \Sigma \to \Gamma$ is an *output function*.

The semantics of a Mealy Machine is given by the following inductive
equations:
$$
    \mealy{M}(w) \defined \mealy{M}(q_0, w) 
    \quad 
    \mealy{M}(q,\emptyword) \defined \emptyword
    \quad 
    \mealy{M}(q,au) \defined \lambda(q,a) \concat \mealy{M}(\delta(q,a), u)
$$

### Mealy Machine With Lookahead {.def}

Let $\Sigma$ and $\Gamma$ be two alphabets.
A "Mealy Machine with Lookahead" $\mealy{M}$ is a tuple $(q_0, Q, \delta, \lambda)$ 
such that

1. $Q$ is a finite set of *states*.
2. $q_0 \in Q$ is the *initial state*.
3. $\delta \subseteq Q \times \Sigma \times Q$ is a
   *transition relation*.
4. $\lambda \colon Q \times \Sigma \times Q \to \Gamma$ is an *output function*.

In addition to this syntactic definition, we furthermore assume that for each
$w \in \Sigma^*$, there exists at most one path in the automaton $(q_0, Q,
\delta)$ starting from $q_0$ and reading $w$.

The semantics of the Mealy Machine is given by considering potential *runs* of
the machine. Because of the absence of ambiguity, it defines a partial map
$\mealy{M} \colon \Sigma^* \topartial \Gamma^*$.

### Sequential Functions {.def}

Let $\Sigma$ and $\Gamma$ be two alphabets.
A "sequential transducer" $A$ is a tuple $(q_0, Q, \delta, \lambda)$ 
such that

1. $Q$ is a finite set of *states*.
2. $q_0 \in Q$ is the *initial state*.
3. $\delta \colon Q \times \Sigma \topartial Q$ is a **partial**
   *transition function*.
4. $\lambda \colon Q \times \Sigma \to \Gamma^*$ is an *output function*.

The semantics is defined as for Mealy Machines.

**Warning:** this is sometimes called *pure sequential functions*. In this
document, we call "impure sequential functions" those that also have an output
function $\rho \colon Q \to \Gamma^*$ that is called at the end of the
computation.

### Eilenberg Bimachines {.def}

An "Eilenberg Bimachine" is a tuple $(A, B, \pi, u)$ where $A$ and $B$ are two
deterministic finite automata, and $u \in \Gamma^*$, together with a production
function $\pi \colon Q_A \times Q_B \times \Sigma \to \Gamma^*$.with
a production function 

The semantics of an Eilenberg Bimachine over non-empty words is given as follows:

1. We run $A$ on the input from left to right
2. We run $B$ on the input from right to left
3. We replace every letter $a_i$ of the input by the word $\pi(q^A_i, q^B_i,
   a_i)$ where $q^A_i$ and $q^B_i$ are respectively the states of $A$ after the
   letter $a_i$ and $B$ before the letter $a_i$.

For empty words, the bimachine outputs $u$.
   

## Maths

### Graph of a Function {.def}

Let $f \colon X \to Y$ be a function. The "graph" of $f$ is the set $\graph(f)
\defined \setof{(x, f(x))}{x \in X}$.

### Topology and Continuous functions {.def}

Let $X$ be a set. A "topology" over $X$ is a subset $\tau$ of $\Parts(X)$
closed under finite intersections and arbitrary unions. In a topological space
$(X, \tau)$, the subsets in $\tau$ are called "open subsets", and their
complement are called "closed subsets".

A function $f \colon (X, \tau) \to (Y,\theta)$ is "continuous" whenever for all
open subset $U \in \theta$, its pre-image $\preim{f}{U}$ is an open subset of
$\tau$. Equivalently, it is continuous if the pre-image of 'closed subsets' are
closed subsets.

### Lipschitz functions {.def}

A function $f \colon (X,d_X) \to (Y, d_Y)$ is "Lipschitz" if there exists a
constant $K \geq 0$ such that for all $x_1,x_2 \in X^2$, $d_Y(f(x_1), f(x_2))
\leq K d_X(x_1, x_2)$.

### Prefix Distance {.def}

Let $\Sigma^*$ be a finite alphabet. The "prefix distance" between two words
$u,v$ is $\vcount{u} + \vcount{v} - 2 \vcount{w}$ where $w$ is the longest common
prefix of $u$ and $v$.


### Regular Topology {.def}

Let $\Sigma$ be a finite alphabet. We equip $\Sigma^*$ with a metric distance
as follows: to a pair of words $u,w$, we associate the minimal size $s(u,w)$ of
a deterministic automaton that *separates* $u$ from $w$. The *distance* between
two words $u$ and $w$, is defined as $d(u,w) \defined 2^{-s(u,w)}$. The
"regular topology" is the topology defined by this metric on $\Sigma^*$.

Equivalently, the *regular topology* is the coarsest 'topology' containing the
regular languages as 'closed subsets'.

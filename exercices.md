---
author: Aliaume LOPEZ
title: Transducer Exercice Session
subtitle: Mealy Machines
lang: en-US
session: 1
date: 2024-02-26
header-includes: |
    <script>
        const connect = () => {
            const ws = new WebSocket("ws://localhost:8080");
            ws.onopen = () => setTimeout(() => ws.send("keepalive"), 30000);
            ws.onclose = () => setTimeout(connect, 1000);
            ws.onmessage = () => location.reload();
        };
        connect();
    </script>
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


\newcommand{\Res}{\mathsf{Res}}
\newcommand{\resi}[2]{{#2}^{-1}{#1}}

\newcommand{\lowercaseExample}{\mathsf{lowercase}}
\newcommand{\expandtabs}{\mathsf{expandtabs}}
\newcommand{\sort}{\mathsf{sort}}
\newcommand{\swap}{\mathsf{swap}}

```{=tex}
\knowledge{notion}
 | wqo
 | well-quasi-order
 | well-quasi-ordering 
 
\knowledge{notion}
 | Mealy Machine
\knowledge{notion}
 | flip-flop machine
\knowledge{notion}
 | binary flip-flop machines
 | binary flip-flop machine
\knowledge{notion}
 | Mealy Machine with Lookahead
\knowledge{notion}
 | preserves prefixes
\knowledge{notion}
 | sequential transducer
 | sequential
\knowledge{notion}
 | topology
\knowledge{notion}
 | open subsets
 | open
\knowledge{notion}
 | closed subsets
\knowledge{notion}
 | continuous
\knowledge{notion}
 | Lipschitz
\knowledge{notion}
 | prefix distance
\knowledge{notion}
 | regular topology
\knowledge{notion}
 | Presburger Arithmetic
```

# Mealy Machines

## True or False? {.exercise}

For each of the following functions, decide whether they can be realized by a
'Mealy Machine'. In positive cases, provide the Mealy Machine, in negative cases,
provide a proof that it cannot be realized.

- [ ] The function $\lowercaseExample \colon \Sigma^* \to \Sigma^*$,
      where $\Sigma$ is the latin alphabet,
      that maps a word $w$ to its lowercase variant. 
      For instance, $\lowercaseExample(aAbcDA) = aabcda$.

- [ ] The function $\expandtabs \colon \Sigma^* \to \Sigma^*$
      that works on the alphabet $\Sigma$ of ASCII characters, 
      and replaces the `tab` codepoint `\t` by four spaces codepoints.

- [ ] The function $w \mapsto c^{\vcount[a]{w}}$.

- [ ] The function $\sort \colon \Sigma^* \to \Sigma^*$ that
      sorts its input, where $\Sigma$ is a finite alphabet
      equipped with a total ordering $\leq$.

- [ ] The function $\Delta \colon \Sigma^* \to \Sigma^*$ that
      maps $u$ to $uu$.

- [ ] The function $\swap \colon \Sigma^* \to \Sigma^*$ that maps $au$ to $ua$
  and $\emptyword$ to $\emptyword$.

- [ ] The function $\swap_2 \colon \Sigma^* \to \Sigma^*$ that
 maps $ua$ to $au$ and $\emptyword$ to $\emptyword$.

What are the extensions of Mealy Machines for which the above functions are computable?

## Arithmetic Circuits {.exercise}

The goal of this exercise is to prove that operations on binary numbers are
possible. To that end we have to provide an encoding of tuples numbers, which
we do as follows: a tuple $(n_1, \dots, n_k) \in \Nat^k$ is represented on the
alphabet $\set{0, 1}^k$ by writing the numbers in *binary*, and *padding them
with zeros* so that the length matches. There are four variants of this
encoding, obtained by deciding whether to pad on the left or the right, and
whether to write numbers with the most significant bit on the left or the
right.

1. For each of the four possible encodings, decide whether the map $(+) \colon
   \Nat^2 \to \Nat$ can be represented using a Mealy Machine.
2. For each of the four possible encodings, decide whether the map $(/3) \colon
   \Nat \to \Nat$ can be represented using a Mealy Machine.
3. Write a Mealy Machine that computes $(n,4n)$ in binary.
4. Deduce a Mealy Machine that computes $5n$ in binary by using the wreath
   product construction and the construction of the addition.

## Bonus: Presburger Arithmetic {.exercise}

Prove that 'Presburger Arithmetic' is decidable.

### Encoding of numbers and formulas {.hint}

Encode a formula $\varphi(\vec{x})$ as a **regular** language of $\Nat^X$,
where numbers are encoded in binary with the most significant bit is on the
left, and the padding is on the right.

### Presburger Operators {.hint}

Start by proving that each of these operations are computed by Mealy Machines.

1. The equality operator $(=) \colon \Nat^3 \to \set{0,1}$.
2. The addition operator $(+) \colon \Nat^2 \to \Nat$.
3. The existential quantifier $(\exists x) \colon \Nat^{x \vec{y}} \to \Nat^{\vec{y}}$.


## Flip Flop Machines {.exercise}

Prove that every 'flip-flop machine' can be obtained by composing 'binary
flip-flop machines'. What is the number of intermediate machines that are
needed?

### Encode states {.hint}

Given a state $q \in Q$, compute using a 'binary flip-flop machine' the sequence
of approximated states $\set{q, \neg q}$.

### For the upper bound {.hint}

Use a binary encoding to obtain a logarithmic number of intermediate machines.

### For the lower bound {.hint}

Obtain an upper bound on the number of machines obtained by composing $k$
binary flip-flop machines.

## Regularity of Mealy Machines {.exercise} 

The goal of this exercise is to understand the relationship between Mealy
Machines and regular languages. Let $f \colon \Sigma^* \to \Gamma^*$ 
be a function computed by a Mealy Machine.

1. Prove that the image of $\Sigma^*$ through $f$ is a regular language.
2. Prove that the pre-image of $\Gamma^*$ through $f$ is a regular language.
3. Let $L$ be a regular language, prove that $\im{f}{L}$ and $\preim{f}{L}$ are
   regular languages, i.e., that $f$ is 'open' and 'continuous' for the
   'regular topology'.
4. Is every 'open' and 'continuous' map computable by a Mealy Machine?
5. A function $f \colon \Sigma^* \to \Gamma^*$ is 'Lipschitz'
   for the 'prefix distance'. What is the value of the Lipschitz constant?
6. The graph of a function $f \colon X \to Y$ is the subset $\graph(f)
   \subseteq X \times Y$ defined by $\setof{ (x,y) \in X \times Y }{ f(x) = y
   }$. Can you provide a necessary and sufficient condition on the graph of $f$
   for it to be representable using a Mealy Machine?

## Decidability Properties of Mealy Machines {.exercise}

In this exercise, the goal is to understand what is decidable about Mealy
Machines. For each of the following questions, prove (or disprove) that it is
decidable, and in case of decidability, provide a precise complexity class.

1. Can we decide if two Mealy Machines compute the same function?
2. Can we decide if a Mealy Machine is surjective?
4. Can we decide if $f(w) \sqsubseteq g(w)$ for all $w \in \Sigma^*$?
3. Can we decide if a Mealy Machine is injective?
5. Can we decide if there exists $w \in \Sigma^*$ such that $f(w) = g(w)$?
6. Can we decide if a Turing machine computes a function that can be computed
   by a Mealy Machine?

### Deciding Injectivity {.hint}

Consider the set $\setof{ (u,v) \in \Sigma^* \times \Sigma^* }{ f(u) = f(v) }$,
and show that it is a regular language.


## Variations on Mealy Machines {.exercise}

Describe the relationship between the expressiveness of the following variations
of Mealy Machines:

1. Mealy Machines
2. Mealy Machines with lookaheads.
3. Sequential functions.
4. Mealy Machines with lookaheads with an ambiguous transition relation, but
   such that every run produces the same output.
5. Mealy Machines with lookaheads with an ambiguous transition relation, where
   the semantic is undefined if there are multiple runs producing different
   outputs.
6. Mealy Machines with transitions labelled by regular expressions.

## Efficient String Matching  {.exercise}

The goal of this homework is to study the problem of string matching. That is,
given a pattern $m \in \Sigma^*$ and a text $t \in \Sigma^*$, one wants to
produce a text $m(t) \in (\Sigma \uplus \bar{\Sigma})^*$ where occurrences of
$m$ are overlined. To avoid ambiguity, we will overline *non-overlapping*
occurrences of the pattern, starting from the left of the text $t$.

1. Is the function that underlines the *starts* of the matches computable by a
   'Mealy Machine'? By a 'sequential function'? By a 'Mealy Machine with
   lookaheads'?
2. Same question with underlining the *ends* of the matches.
3. Same question for the function $m$.
4. Conclude by providing an efficient algorithm to perform string matching.
   What is the (time/space) complexity in $\vcount{m}$? What is the
   (time/space) complexity in $\vcount{t}$?

# Homework

## Continuous Functions {.exercise}

Prove that there exists uncountably many 'continuous' functions from $\Sigma^*$
to $\Gamma^*$ for the 'regular topology'. It is true for 'continuous' and
'prefix preserving functions'?

### The alphabet does not matter {.hint}

Consider the set of all functions from $\Nat$ to $\Nat$.


### Sufficient conditions for continuity {.hint}

Show that the following conditions are sufficient for a function $f \colon \Nat \to \Nat$ to be
continuous:

1. $\forall n \in \Nat, f(n)$ is a factorial,
2. $\liminf_{n \to \infty} f(n) = \infty$.


## Stability properties of Sequential Functions {.exercise}

We say that a function "preserves prefixes" if for all $u,v \in \Sigma^*$, $u
\prefleq v$ implies $f(u) \prefleq f(v)$. Prove that the following propositions
are equivalent for a function $f \colon \Sigma^* \to \Gamma^*$:

1. $f$ is 'sequential'.
2. $f$ is 'continuous' for the 'regular topology', 'Lipschitz' for the 'prefix
   distance', and 'preserves prefixes'.



\clearpage

# Cheat Sheet {.cheat-sheet}

## Machines

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

### Flip-Flop Machine {.def}

A "flip-flop machine" is a Mealy Machine such that for all letters $a \in
\Sigma$, either $\delta(\cdot,a)$ is the identity function, or it is a constant
function. It is *binary* when $Q = \set{0,1}$.

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

**Warning:** this is sometimes called *pure sequential functions*.

## Maths

### Presburger Arithmetic {.def}

Formulas of the "Presburger Arithmetic" are built from the following grammar:

$$
\begin{aligned}
    \varphi &\defined \top \mid \bot \mid \varphi \land \varphi \mid \varphi \lor \varphi \mid \lnot \varphi \mid \exists x. \varphi \mid x = y + z
\end{aligned}
$$

Given a valuation $\nu \colon \vec{x} \to \Nat$, we define the semantics of
$\varphi$ inductively as follows:

$$
\begin{aligned}
    \nu \models \top &\iff \text{true} \\
    \nu \models \bot &\iff \text{false} \\
    \nu \models \varphi \land \psi &\iff \nu \models \varphi \text{ and }  \nu \models \psi \\
    \nu \models \varphi \lor \psi &\iff \nu \models \varphi \text{ or } \nu \models \psi \\
    \nu \models \lnot \varphi &\iff \text{ not } (\nu \models \varphi) \\
    \nu \models \exists x. \varphi &\iff \text{ there exists } n \in \Nat \text{ s.t. } \nu[x \mapsto n] \models \varphi \\
    \nu \models x = y + z &\iff \nu(x) = \nu(y) + \nu(z)
\end{aligned}
$$

### Topology and Continuous functions {.def}

Let $X$ be a set. A "topology" over $X$ is a subset $\tau$ of $\Parts(X)$
closed under finite intersections and arbitrary unions. In a topological space
$(X, \tau)$, the subsets in $\tau$ are called "open subsets", and their
complement are called "closed subsets".

A function $f \colon (X, \tau) \to (Y,\theta)$ is "continuous" whenever for all
open subset $U \in \theta$, its pre-image $\preim{f}{U}$ is an open subset of
$\tau$. Equivalently, it is continuous if the pre-image of closed subsets are
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

Equivalently, the *regular topology* is the coarsest topology containing the
regular languages as *closed subsets*.


### Well-quasi-ordering {.def}

A quasi-ordered set $(X, \leq)$ is a "well-quasi-ordering" if for every
sequence $\seqof{x_i}{i \in \Nat}$ of elements in $X$, there exists an
increasing pair of indices $i < j$ such that $x_i \leq x_j$.

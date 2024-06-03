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

# First Order Logic

## Some Examples {.exercise}

Provide first-order transductions
that represent the following functions:

1. The function that maps a word $w$ to its reverse.
2. The function that maps a word
   $ab^na$ to $(ab)^n (ba)^n$, 
   $ba^nb$ to $(ba)^n (ab)^n$,
   and $w$ to $w$ otherwise.
3. The function that sorts the letter in a word.

## Some Non-Examples {.exercise}

Prove that the following functions are not representable by first-order
transductions:

1. The function that maps $w$ to $a$ if $w$ is of odd length
   and $b$ otherwise.
2. The function that maps $w$ to $w^2$ if $w$ is of even length
   and $w^3$ otherwise.
3. Given a non-trivial group $(G, \cdot)$, the function that maps
   a word $w$ to its image in $G$.

# Lambda Terms

## Extra Functions {.exercise}

Prove that the lambda-calculus becomes strictly more
expressive when adding the following functions:

1. The trace operator $\mathsf{trace} \colon (A \times B \to A \times B) \to (B
   \to 1 + B)$ that computes the trace of a function.
2. The fold operator $\mathsf{fold} \colon (Q \times \Sigma \to Q) \to Q \times
   \Sigma^* \to Q$.

# Blind again

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

# Cheat-Sheet 

## Regular functions {.def}

A function $f: A^* \to B^*$ is called a "regular function" if there exists
a two-way deterministic finite automaton with outputs (2DFT) that computes $f$.
Such an automaton has a finite set of states $Q$ with a distinguished initial
state $q_0$, a transition function function over an extended input alphabet
$\Sigma = A \cup \set{ \vdash , \dashv }$ to delimit the endpoints of the input
word. The transition function has the following type $\delta \colon \Sigma
\times Q \to Q \times \set{ \leftarrow, \downarrow, \rightarrow,  \uparrow }$.
That is, it can read a letter, change state, move left $\leftarrow$, right
$\rightarrow$, stay in place $\downarrow$, or exit the computation $\uparrow$.

The output of the automaton is guided by a production function $\lambda \colon
Q \times \Sigma \to B^*$. That is, for every state and current letter, the
automaton can produce some word in $B^*$.

A "run of a 2DFT" is a sequence of configurations $(q_i, p_i)$ where $q_i$ is
the ith state of the computation, and $p_i$ is the ith position of the head
over an extended input word $\vdash w \dashv$. The run starts in the initial
state $q_0$, and the initial position $p_0 = 0$ (so on the letter $\vdash$).
The unique run is defined inductively as one expects using the transition
function $\delta$. Note that a 'regular function' should guarantee that the run
does not go *out of bounds* nor *loops forever*.

The production of a run $\rho$ of a 2DFT is the word obtained by concatenating
the outputs produced by each transition.



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


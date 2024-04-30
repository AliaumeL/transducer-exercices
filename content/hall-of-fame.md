---
title: Bounty Board
author: Aliaume LOPEZ
subtitle: Zbieraj łupy, dzielni rycerze
email: ad.lopez@uw.edu.pl
lang: en-GB
date: 2024-04-30
knowledges:
    - synonyms:
        - deatomisable
        - deatomisables
    - synonyms:
        - atomic bimachine
        - atomic bimachines
    - synonyms:
        - equivariance property
    - synonyms:
        - atomic code
        - atomic codes
        - coding of atoms
        - atom coding function
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

\newcommand{\toinj}{\hookrightarrow}

\newcommand{\MSO}{\mathsf{MSO}}
\newcommand{\Atoms}{\mathbb{A}}

\newcommand{\topartial}{\rightharpoonup}

\newcommand{\prefleq}{\mathrel{\sqsubseteq_{\mathsf{prefix}}}}

\newcommand{\zip}{\mathsf{zip}}

\newcommand{\Res}{\mathsf{Res}}
\newcommand{\resi}[2]{{#2}^{-1}{#1}}

\newcommand{\lowercaseExample}{\mathsf{lowercase}}
\newcommand{\expandtabs}{\mathsf{expandtabs}}
\newcommand{\sort}{\mathsf{sort}}
\newcommand{\swap}{\mathsf{swap}}


# The Bounty Board Rules ⚔️

The Bounty Board is a place where you can find tasks to complete. Each task is
associated with a reward. The rewards are given in terms of points at the end
of the year, with the following formula: $$ \text{points} = 1 / \text{number of
bounty hunters} $$. Some bounties have a limited date of completion, and some
are open until the end of the year.

To collect a bounty, you need to send to `ad.lopez@uw.edu.pl` a complete
solution in `pdf` format. Upon reception, and if the solution is correct, you
will be added to the list of bounty hunters for this task.

# The Bounty Board 🏆

The board contains columns **Task**, **Difficulty**, and **Bounty Hunters**.
The difficulty is rated from 🌟 to 🌟🌟🌟🌟🌟, if no-one has collected the
bounty yet, it is indicated with an *empty nest* 🪹.


| Task  |   Difficulty  |   Bounty Hunters  |
|:--------------|--------------:|------------------:|
| [Be There Or Be Very Weak Square](#be-there-or-be-very-weak-square) | 🌟🌟🌟🌟 | 🪹 |
| [Minimising growth](#minimising-growth) | 🌟🌟🌟🌟 | 🪹 |
| [Deatomisation of Bimachines](#deatomisation-of-bimachines) | 🌟🌟🌟 | 🪹 |
| [Nesting Birds](#nesting-birds) | 🌟🌟🌟 | 🪹 |
| [Bounded Output](#bounded-output) | 🌟🌟 | 🪹 |
| [Forward Loops Cannot Go Backwards](#forward-loops-cannot-go-backwards) | 🌟 | 🪹 |
| [Windowed Transducers](#windowed-transducers) | 🌟 | 🪹 |
| [One Size Fits All](#one-size-fits-all) | 🌟 | 🪹 |


# Bounties

## Bounded Output {.exercise}

Let $f : \Sigma^* \to \Gamma^*$ be a polyregular function. We say that $f$ has
bounded output if there exists a constant $N$ such that for all words $w \in
\Sigma^*$, $|f(w)| \leq N$. Give an algorithm that decides if a polyregular
function has bounded output.

## Forward Loops Cannot Go Backwards {.exercise}

Let us call $\mathsf{ForwardPoly}$ the class of functions computed by
for-programs that only have forward loops. Prove that the `reverse` function is
not in $\mathsf{ForwardPoly}$.

## Nesting Birds {.exercise}

Give an algorithm that inputs a polyregular function $f$, and decides whether
$f$ can be realised by a for-program that does not nest for loops.

## One Size Fits All {.exercise}

Prove that the following two subclasses of rational functions are equivalent
and provide effective conversions:

1. unambiguous NFA with output where every transition is labelled by exactly
   one output letter.
2. unambiguous NFA with output where for every input word, the output has the
   same length as the input. 


## Be There Or Be Very Weak Square {.exercise}

A *semi-blind* $k$-pebble transducer is obtained by modifying the original
model so that when placing a new pebble, the machines does not start from the
leftmost position of the input (and stays where it is currently), but such that
the pebbles cannot be seen by submachines. Prove that semi-blind $k$-pebble
transducers cannot compute the `squaring` function.

## Windowed Transducers {.exercise}

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


## Minimising growth {.exercise}

Recall that in $\MSO$-transductions, we introduced a duplication function
$d_{\alpha, \beta}$ that maps $w$ to $\diamond^\beta \prod_{i = 1}^{|w|} w_i
(\#)^{\alpha - 1}$. Any regular function is written as the composition of an
$\MSO$-interpretation (without copies) with a duplication. As a consequence,
$|f(w)| \leq \alpha |w| + \beta$ for some $\alpha, \beta \in \Nat$.

Question: assume that there exists $\alpha', \beta' \in \Nat$ such that $|f(w)|
\leq \alpha' |w| + \beta'$ for all $w$. Is it possible to represent $f$ using
$d_{\alpha',\beta'}$ followed by an $\MSO$-interpretation.


## Deatomisation of Bimachines {.exercise}

Let $\Atoms$ be an infinite set, and $\mathcal{S}$ be the set of permutations
of $\Atoms$. We define "atomic bimachines" with input alphabet $(\Sigma \cup
\Atoms)$ and output alphabet $(\Gamma \cup \Atoms)$ via the existence of
a finite monoid $M$ and a morphism $\mu \colon (\Sigma \cup \Atoms)^* \to M$
such that $\mu(a) = 1_M$ for all $a \in \Atoms$, together with a production
function $\pi \colon M \times (\Sigma \cup \Atoms) \times M \to (\Gamma \cup
\Atoms)^*$, satisfying the following "equivariance property" (where $\sigma \in
\mathcal{S}$ is lifted from permutations over $\Atoms$ to an action over
$(\Gamma \cup \Atoms)^*$ and $(\Sigma \cup \Atoms)^*$ in the natural way):

$$
\forall a \in \Atoms, \forall \sigma \in \mathcal{S},
\pi (m, \sigma(a), n) = \sigma(\pi(m,a,n)) \quad .
$$

An "atom coding function" is a function $c \colon \Atoms \toinj \langle 1^*
\rangle$, i.e., that maps every atom to a unique word of the form $\langle 1^k
\rangle$ for some $k \in \Nat$. We say that a function $f \colon (\Atoms \cup
\Sigma)^* \to (\Atoms \cup \Gamma)^*$ is "deatomisable" if there exists
a rational function $f^\dagger \colon (\Sigma \cup \set{ \langle, \rangle,
1})^* to (\Gamma \cup \set{ \langle, \rangle, 1})^*$ such that for all 'atomic
codes' $c \colon \Atoms \toinj \langle 1^* \rangle$, the following commutes

$$
c \circ f = f^\dagger \circ c \quad .
$$

Prove that the following are equivalent:

1. A function $f$ is 'deatomisable',
2. It is realisable by an 'atomic bimachine'.

---
title: First Homework
author: Aliaume LOPEZ
subtitle: Mealy Machines
email: ad.lopez@uw.edu.pl
website: https://www.irif.fr/~alopez/enseignement.html
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
% here put knowledges
```

# Mealy Machines and Variations

## Flip-Flop {.exercise}

Show that a 'flip-flop' machine can be obtained by composition of 'binary flip
flop' machines. What is the minimal number of intermediate machines needed?

## Decidable {.exercise}

Show that it is decidable whether a 'sequential function' is injective.

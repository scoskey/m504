# Math 404/504 homework

## Homework 3, due Thursday 3 February

1. Show that if $(x\_0,y\_0)$ is a solution to $ax+by=d$, then so is $(x\_0+kb/d,y\_0-ka/d)$.
2. Let $a,b,c$ be three numbers with $\gcd(a,b,c)=1$. Explain how to use the extended Euclidean algorithm to solve the equation $ax+by+cz=1$. Apply your method to solve $155x+341y+385z=1$, and to solve $1234x+3456y+6789z=1$. (You may use calculators/computers, but please show me your process.)
3. Solve each of the congruences using the extended Euclidean algorithm. $4x\equiv17\pmod{21}$, $63x-350\equiv500\pmod{730}$, $1234x\equiv5000\pmod{12345}$. (You may use calculators/computers, but please show me your process.)
4. Silverman, exercise 8.4

### Supplemental problems

* SP8 Prove that if $s,t$ are odd numbers with no common factors, then the Pythagorean triple $(\frac{s^2-t^2}{2},st,\frac{s^2+t^2}{2})$ is primitive.
* SP9 Silverman, exercise 7.5.
* SP10 Modify the function "gcd2" to always returns a pair $x,y$ with $x>0$. Then use it to write a new function "reciprocal" which takes as input two numbers $a,n$ with $\gcd(a,n)=1$ and returns the value of $a^{-1}$ in $\mathbb Z\_n$.
* SP11 Silverman, exercise 8.10

## Homework 2, due Thursday 27 January

1. Show that if $u,v$ have no common factors, aren't both even, and aren't both odd, then the triple $(u^2-v^2,2uv,u^2+v^2)$ will have no common factors.
2. Silverman, exercise 3.2
3. Show that if $r\_i,r\_{i+1},r\_{i+2}$ are successive remainders in a run of the Euclidean algorithm, then $r\_{i+2}\lt\frac12r\_i$. (See Silverman, exercise 5.3.)
4. Let $F\_n$ denote the Fibonacci sequence. Show that in a run of the Euclidean algorithm on $F\_{n+1},F\_n$, the quotient $q$ will be $1$ every time. Show that the algorithm terminates in $n-1$ steps.

### Supplemental problems

* SP5 Silverman, exercise 3.5(a)-(d)
* SP6 Find the $\gcd$ of any pair of Fibonacci numbers $F\_n$ and $F\_m$ in terms of $n$ and $m$, and prove you are correct.
* SP7 Silverman, exercise 5.4

## Homework 1, due Thursday 20 January

1. Show how to generate a square triangle number from a pair $p,q$ such that $p^2$ and $2q^2$ are one unit apart. Verify your resulting quantity $n$ is a square triangle.
2. Show how, given $p,q$ as above, to generate a new pair $p',q'$ with the same property. Verify your $p',q'$ satisfy that $(p')^2$ and $2(q')^2$ are one unit apart.
3. Show that if $(a,b,c)$ is a primitive Pythagorean triple, then exactly one of $a,b$ is odd.
4. Show how to generate a primitive Pythagorean triple from two odd numbers $s,t$. Verify that it is a Pythagorean triple.
5. Silverman, exercise 1.6.

### Supplemental problems

* SP1 Silverman, exercise 1.3
* SP2 Silverman, exercise 2.1
* SP3 Silverman, exercise 2.6
* SP4 Silverman, exercise 2.7
* ... suggest your own!


<script>
window.MathJax = {
  tex: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    processEscapes: true,
    macros: {
      set: ["{\\left\\{ #1 \\right\\}}", 1],
      abs: ["{\\left| #1 \\right|}", 1],
      lt: ["<"]
    }
  }
};
</script>

<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>

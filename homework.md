# Math 404/504 homework

## Homework 14, due Friday 29 April

1. Silverman, exercise 48.4(a). Let $x$ be the continued fraction $[a,\overline{b,c}]$. Find a formula for $x$.
2. Consider the Pell equation $x^2-41y^2=1$. (a) Find the periodic continued fraction for $\sqrt{41}$. (b) State the period $k$ of the continued fraction for $\sqrt{41}$. (c) Find the first $k$ convergents for the continued fraction for $\sqrt{41}$. (d) Plug the $k-1$st convergent into $x^2-41y^2$ to get $\pm1$ on the right-hand side. (e) If you got $-1$ on the right-hand side, use the method of squaring to find a solution to $x^2-41y^2=1$.

### Supplemental problems

* SP42 Silverman, exercise 48.1
* SP43 Silverman, exercise 48.2

## Homework 13, due Friday 22 April

1. Silverman, exercise 31.4. Explore the first five pentagonal numbers. Find a formula for the pentagonal numbers and use it to find the 10th and 100th pentagonal numbers.
2. (Similar to Silverman, exercise 32.4.) We have studied square triangles, so now study square pentagons. Set $n^2=$ your formula for the $m$th pentagonal number. Use substitution to reduce the problem to solving a Pell equation (it helped me to multiply both sides by 24). Then use computational methods to find three solutions to the Pell equation, and finally, three square pentagonal numbers.
3. Silverman, exercise 32.1. Show that if $D$ is a perfect square, then $x^2-Dy^2=1$ has no nontrivial solutions.
4. Consider the Pell equation $x^2-21y^2=1$. Suppose you know that $(110,24)$ and $(12098,2640)$ are solutions to $x^2-21y^2=4$. Use the quotient method from 4(c) of the Pell equation activity to find a solution to $x^2-21y^2=1$.

### Supplemental problems

* SP39 Study triangular pentagonal numbers and find some examples. What Pell-like equation may be solved in order to find them?
* SP40 Complete the proof that the quotient method works from 4(c) of the Pell equation activity.
* SP41 Silverman, exercise 34.1(a)(b).

## Homework 12, due Friday 15 April

1. (Similar to Silverman, exercise 28.7.) (a) Suppose $p$ is an odd prime and $a$ is a square modulo $p$. Show that $a$ cannot be a primitive root modulo $p$. (b) More generally suppose $n\mid p-1$ and $a$ is an $n$th power modulo $p$. Show that $a$ cannot be a primitive root modulo $p$.
2. Find all primitive $(p-1)$th roots for the primes: $p=23,29,31$.
3. Silverman, exercise 29.3(a)(b). If $ab\equiv1\pmod{p}$, then how are $\mathrm{Ind}(a)$ and $\mathrm{Ind}(b)$ related? If $a+b\equiv0\pmod{p}$, how are $\mathrm{Ind}(a)$ and $\mathrm{Ind}(b)$ related? For each question, collect some data, make a conjecture, and then prove that your conjecture is true.
4. Silverman, exercise 29.7(c). (Or in other words, complete page 3 of the ElGamal activity.)

### Supplemental problems

* SP35 Silverman, exercise 28.1
* SP36 Silverman, exercise 28.8(a)(c)
* SP37 Silverman, exercise 29.1
* SP38 Silverman, exercise 29.6

## Homework 11, due Friday 8 April

1. Silverman, exercise 24.2. Show that if $p$ is a prime and $p\neq5$ and $p=a^2+5b^2$ then $p\equiv1$ or $p\equiv9\pmod{20}$. [Hint: Consider the possibilities for $p$ modulo $4$ and modulo $5$.]
2. Use the descent procedure from class to write $p=1553$ as a sum of two squares.
3. Suppose $p\equiv5\pmod{8}$ and $p-1=4s$. Show that $x=a^{(s+1)/2}$ is a solution to $x^2\equiv\pm a\pmod{p}$. Show that $z=2^s$ is a solution to $z^2\equiv-1\pmod{p}$.
4. Use the method from class to solve $x^2\equiv 7\pmod{197}$. [Note: $p\equiv5\pmod{8}$.]

### Supplemental problems

* SP31 Silverman, exercise 24.6
* SP32 Use the descent procedure from class to write $p=54133$ as a sum of two squares.
* SP33 (Similar to Silverman, exercise 25.4.) Show that if $p,q\equiv3\pmod{4}$ then $pq$ is not a sum of two squares. [Hints: If $pq=a^2+b^2$, reduce modulo $p$ to get $a^2+b^2\equiv0\pmod{p}$. Show this implies that either $a,b\equiv0\pmod{p}$ or else $-1$ is a square modulo $p$. Then get a contradiction.]
* SP34 Use the method from class to solve $x^2\equiv11\pmod{353}$. [Note: $p\equiv1\pmod{8}$ so you have to use the full procedure.]

## Homework 9, due Friday 18 March

1. (Similar to Silverman, exercise 20.3.) Make a list of the cubes modulo $p=17$. Show that if $p\equiv2\pmod{3}$, then every number is a cubic residue modulo $p$. [Hint: Show that in this case it is possible to find an exponent that performs cube roots.]
2. Prove that $(\frac{-1}{p})=1$ if $p\equiv1\pmod{4}$ and that $(\frac{-1}{p})=-1$ if $p\equiv3\pmod{4}$. [You may use Euler's Criterion which states that $(\frac{a}{p})\equiv a^{(p-1)/2}\pmod{p}$.]
3. Silverman, exercise 21.1.
4. Calculate the Legendre symbols using factoring and quadratic reciprocity: $(\frac{85}{101})$, $(\frac{29}{541})$, $(\frac{101}{1987})$

### Supplemental problems

* SP27 Silverman, exercise 22.2
* SP28 Silverman, exercise 22.3
* SP29 Silverman, exercise 22.4
* SP30 Calculate the Legendre symbols using Jacobi reciprocity (no factoring except $2$ and $-1$): $(\frac{85}{101})$, $(\frac{29}{541})$, $(\frac{101}{1987})$

## Homework 8, due Friday 11 March

1. Silverman, exercise 18.4 (see [math.brown.edu/johsilve/frint.html#exercise18.4](https://www.math.brown.edu/johsilve/frint.html#exercise18.4))
2. How long does it take to find $\phi(n)$? Use `from sympy import totient` and time the `totient()` function on at least 30 different integers with 5-50+ digits. Make a table of number of digits and the run time. What does your data suggest about how many digits you should use to be secure?
3. Silverman, exercise 19.3
4. Silverman, exercise 19.7

### Supplemental problems

* SP23 Silverman, exercise 18.5
* SP24 Silverman, exercise 19.2
* SP25 SIlverman, exercise 19.4
* SP26 SIlverman, exercise 19.5

## Homework 7, due Friday 4 March

1. Use `powermod` and `binaryexpand` (or similar calculator methods) to calculate the powers: $28^{749}\pmod{1147}$, and $208^{1\,010\,101}\pmod{101}$. Show your work with enough calculator output to understand your process.
2. Use `euler`, `inverse`, and `pow` (or similar calculator methods) to solve the roots: $x^{113}\equiv347\pmod{463}$, and $x^{275}\equiv139\pmod{588}$. Show your work with enough calculator output to understand your process.
3. Let $n=13$. Find an exponent $k$ such that $x^k\pmod{13}$ has exactly one solution. Find an example of an exponent $k$ such that $x^k\pmod{13}$ has more than one solution. How many solutions are there? Find a second example of an exponent $k$ such that $x^k\pmod{11}$ has more than one solution. How many are there?
4. Let $n=pq$ be a product of distinct primes, and let $\lambda(n)=\mathrm{lcm}(p-1,q-1)$. Show that if $\gcd(a,n)=1$, then $a^{\lambda(n)}\equiv 1\pmod{n}$.

### Supplemental problems

* SP20 Silverman, exercise 17.3(a)
* SP21 Silverman, exercise 17.3(c) - give many examples supporting your conjecture.
* SP22 Show that if $\gcd(a,10)=1$, then $a^{2001}$ and $a$ have the same last three digits.

## Homework 6, due Thursday 24 February

1. Silverman, exercise 12.2
3. Prove that if $t=2^p-1$ and $t$ is prime, then $t(t+1)/2$ is a perfect number.
3. Silverman, exercise 15.1. Prove that the divisor sum function $\sigma(n)$ satisfies $\sigma(mn)=\sigma(m)\sigma(n)$ when $\gcd(m,n)=1$.
4. Silverman, exercise 15.5

### Supplemental problems

* SP16 Silverman, exercise 12.3
* SP17 Silverman, exercise 13.6
* SP18 Silverman, exercise 14.1
* SP19 Silverman, exercise 15.3

## Homework 4, due Thursday 10 February

1. (Similar to Silverman, exercise 9.1.) Use Fermat's little theorm to help find a solution to each equation.
  * $x^{74}\equiv5\pmod{37}$
  * $x^{83}\equiv16\pmod{41}$
  * $x^{55}\equiv27\pmod{53}$
2. (Similar to Silverman, exercise 9.2.)
  * Find the value of $(p-2)!\pmod{p}$ for the first five odd primes $p$.
  * Show that if $p$ is prime, then the numbers $2\leq a\leq p-2$ can be sorted into pairs that are inverses of one another (in other words, $a^{-1}\neq a$).
  * Conclude that $(p-2)!\equiv1\pmod{p}$.
3. Silverman, exercise 10.3(a)
4. Silverman, exercises 11.5 and 11.6

### Supplemental problems

* SP12 Show that for any $n$, you can find $n$ consecutive composite numbers.
* SP13 Silverman, exercise 10.1
* SP14 Silverman, exercise 11.10
* SP15 Silverman, exercise 11.11

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

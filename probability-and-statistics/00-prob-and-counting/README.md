# Probability and Statistics: Week 0 - Probability and Counting

## Theoretical Review

**1. Sample space** $S$ of an experiment is the set of all possible outcomes of the experiment.

**2. An event** $A$ is the subset of sample space $S$ => $A$ occurred if the actual outcome is in A.

Example: When rolling a dice:
- Sample space $S = \set{1,2,3,4,5,6}$.
- Event $A$: 1 is rolled. $A = \set{1}$.
- Event $B$: An odd number is rolled. $B = \set{1, 3, 5}$.

**3. De Morgan's Laws**:
- $\bar{A \cap B} = \bar{A} \cup \bar{B}$
- $\bar{A \cup B} = \bar{A} \cap \bar{B}$

**4. Naive definition of probability**: $P_{naive}(A) = \frac{|A|}{|S|} = \frac{\text{Number of outcomes favorable to }A}{\text{Total number of outcomes in }S}$

**5. Multiplication rule**: Experiment $A$ has $a$ possible outcomes, experiment $B$ has $b$ possible outcomes => The compound experiment has $ab$ possible outcomes.

**6. Sampling with replacement**: choosing a certain object does NOT preclude it from being chosen again.
- If there is $n$ objects, $k$ choices, with replacement given $n^k$ possible outcomes.

**7. Sampling without replacement**: choosing a certain object precludes it from being chosen again.
- If there is $n$ objects, $k$ choices, with replacement given $\frac{n!}{(n-k)!} = n(n-1)...(n-k+1)$ possible outcomes.

**8. Definition of probability**:
- $P(\emptyset) = 0$
- $P(S) = 1$
- $P(\bar{A}) = 1 - P(A)$
- If $A \subseteq B$, then $P(A) \leq P(B)$
- $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- If $A_1, ..., A_n$ are disjoint ( $A \cap B = \emptyset$ ), then $$P(\bigcup_{j=1}^{n}) = \sum_{j=1}^{n} P(A_j)$$
- (Inclusion-Exclusion) For any $A_1, ..., A_n$ $$P(\bigcup_{i=1}^n A_i) = \sum_i P(A_i) - \sum_{i \lt j} P(A_i \cap A_j) + \sum_{i \lt j \lt k} P(A_i \cap A_j \cap A_k) - ... + (-1)^{n+1} P(A_1 \cap ... \cap A_n)$$

**9. Bose-Einstein**: $\binom{n+k-1}{k}$

**Problem Definition:** How many ways are there to choose $k$ times from a set of $n$ objects with replacement, if order doesn't matter (we only care about how many times each object was chosen, not the order in which they were chosen)?

**Solution:** Suppose that when we chose object of type $i$, we will put it in the box $i$ as well, it will not change the problem since we do not care about the order. For example, choosing $k=7$ times of a set of $n=4$ objects can have this scenario.

- Box 1: o
- Box 2: o o
- Box 3: o o o
- Box 4: o o o o

*o represents an object*

This, or any configuration, can be encoded as a sequence of |'s and o's. For example:

| o | o o | o o o | o |

This sequence must:
- Start and end with a |.
- Have $k$ o's and $n-1$ |'s in between.
or we can say there are 2 fixed slots and $n+k-1$ available slots to be alternatively chosen.

In consequence, we choose $k$ out of $n+k-1$ to be o's with $\binom{n+k-1}{k}$ possible outcomes. This is also the answer to the problem definition.

## Interesting Examples

**1. A casino uses 10 standard decks of cards mixed together into one big deck, which is a *superdeck*. Thus, the superdeck has 52 x 10 = 520 cards, with 10 copies of each card. How many different 10-card hands can be dealt from the superdeck? The order of the cards does not matter, nor does it matter which of the original 10 decks the cards came from.**

**Solution:** It is similar to: *How many ways are there to choose* $k=10$ *cards out of* $n=52$ *distinct cards within the superdeck?*. Hence, there are $\binom{52+10-1}{10} = \binom{52+10-1}{10}$ possible outcomes.

**2. To fulfill the requirements for a certain degree, a student can choose to take any 7 out of a list of 20 courses, with the constraint that at least 1 of the 7 courses must be a statistics course. Suppose that 5 of the 20 courses are statistics course. How many choices are there for which 7 courses to take?**

**Solution:**
- Student takes exactly 1 statistics course: $\binom{5}{1} \times \binom{15}{6}$ possible outcomes.
- Student takes exactly 2 statistics courses: $\binom{5}{2} \times \binom{15}{5}$ possible outcomes.
- Student takes exactly 3 statistics courses: $\binom{5}{3} \times \binom{15}{4}$ possible outcomes.
- Student takes exactly 4 statistics courses: $\binom{5}{4} \times \binom{15}{3}$ possible outcomes.
- Student takes exactly 5 statistics courses: $\binom{5}{5} \times \binom{15}{2}$ possible outcomes.
The total number of choices is the sum of all aforementioned cases.

**Alternative Solution:**
- Sample space size: $\binom{20}{7}$
- Student takes no statistics course: $\binom{15}{7}$ possible outcomes.
The total number of choice is: $\binom{20}{7} - \binom{15}{7}$

*Warning:* The answer is not $\binom{5}{1} \times \binom{19}{6}$ due to overcounting.

Suppose that $S_1, S_2, S_3, S_4$ and $S_5$ are the statistics course.
- Case 1
    - Choose 1 out of 5 statistics course: $S_1$ are being chosen.
    - Choose 6 out of 19 remaining course: $S_2, S_4, S_5$ are being chosen.
- Case 2
    - Choose 1 out of 5 statistics course: $S_4$ are being chosen.
    - Choose 6 out of 19 remaining course: $S_1, S_2, S_5$ are being chosen, with the same normal course as in case 1.
From the above, the 2 cases are similar.

**3. A fair dice is rolled $n$ times. What is the probability that at least 1 of the 6 values never appears?**

**Solution:** 

Let $A_i$ be the event that value $i$ never appears $(1 \le i \le 6)$.

Using the inclusion-exclusion, we will get:
$$P(\bigcup_{i=1}^6 A_i) = \sum_i P(A_i) - \sum_{i \lt j} P(A_i \cap A_j) + \sum_{i \lt j \lt k} P(A_i \cap A_j \cap A_k) - ... + P(\bigcap_{i=1}^6 A_i)$$

Calculate to get: $$P(\bigcup_{i=1}^6 A_i) = \binom{6}{1}\frac{5^n}{6^n} - \binom{6}{2}\frac{4^n}{6^n} + \binom{6}{3}\frac{3^n}{6^n} - \binom{6}{4}\frac{2^n}{6^n} + \binom{6}{5}\frac{1^n}{6^n}$$

**4. There are 100 passengers lined up to board an airplane with 100 seats (with each seat assigned to one of the passengers). The first passenger in line crazily decides to sit in a randomly chosen seat (with all seats equally likely). Each subsequent passenger takes his or her assigned seat if available, and otherwise sits in a random available seat. What is the probability that the last passenger in line gets to sit in his or her assigned seat?**

**Solution:**

Suppose that passenger $i (1 \le i \le 100)$ must seat in seat $i$. Then:
- When seat $i$ is occupied by an unassigned passenger, then passenger $i$ can only choose seat 1 or seat with number greater than $i$.
- If a passenger $k (1 \le i \lt 100)$ sits on seat 1, then other passenger will sits correctly as well as passenger 100.
- If a passenger $k$ sits on seat 100, then other passenger will sits correctly, passenger 100 will sit incorrectly.
- The process of having incorrect seats always be end when there is a passenger decided to sit on seat 1 or 100. For example:
    - The crazy passenger 1 sits on seat 23.
    - Passenger 2 to 22 sits correctly.
    - Passenger 23 sits on seat 87.
    - Passenger 24 to 86 sits correctly.
    - Passenger 87 sits on seat 1 (end of the incorrect process across passenger 1-99).
    - Passenger 88 to 99 sits correctly.
    - Passenger 100 sits correctly since the last incorrect 1-99 passenger sits on seat 1.
- We only consider the passenger that ends the incorrect process across 1-100. He/she will have equal chance to pick seat 1 or 100. Therefore, $P = \frac{1}{2}$

## Programming problems

**1. Matching problem:** $n$ cards is label from $1$ to $n$, you draw a card randomly $n$ times and count from 1 for every card that you have drawn. Find the probability that the number that you have count is exactly like the number in the card. (Solution: $1 - \frac{1}{e}$, code is in `a-matching-problem.py`).

**2. Birthday problem:** Find the probability that at least one pair in a group of $k$ people has the same birthday (among 365 dates, excluding February 29 and any given information such as there are twins).

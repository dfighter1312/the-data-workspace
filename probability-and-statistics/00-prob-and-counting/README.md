# Probability and Statistics: Week 0 - Probability and Counting

## Theoretical Review

1. Sample Spaces $S$ of an experiment is the set of all possible outcomes of the experiment.
2. An event $A$ is the subset of sample space $S$ => $A$ occurred if the actual outcome is in A.

Example: When rolling a dice:
- Sample space $S = \set{1,2,3,4,5,6}$.
- Event $A$: 1 is rolled. $A = \set{1}$.
- Event $B$: An odd number is rolled. $B = \set{1, 3, 5}$.

3. De Morgan's Laws:
- $\bar{A \cap B} = \bar{A} \cup \bar{B}$
- $\bar{A \cup B} = \bar{A} \cap \bar{B}$

4. Naive definition of probability: $P_{naive}(A) = \frac{|A|}{|S|} = \frac{\text{Number of outcomes favorable to }A}{\text{Total number of outcomes in }S}$

5. Multiplication rule: Experiment $A$ has $a$ possible outcomes, experiment $B$ has $b$ possible outcomes => The compound experiment has $ab$ possible outcomes.

6. Sampling with replacement: choosing a certain object does NOT preclude it from being chosen again.
- If there is $n$ objects, $k$ choices, with replacement given $n^k$ possible outcomes.

7. Sampling without replacement: choosing a certain object precludes it from being chosen again.
- If there is $n$ objects, $k$ choices, with replacement given $\frac{n!}{(n-k)!} = n(n-1)...(n-k+1)$ possible outcomes.

8. Definition of probability:
- $P(\emptyset) = 0$
- $P(S) = 1$
- $P(\bar{A}) = 1 - P(A)$
- If $A \subseteq B$, then $P(A) \leq P(B)$
- $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- If $A_1, ..., A_n$ are disjoint ( $A \cap B = \emptyset$ ), then $$P(\bigcup_{j=1}^{n}) = \sum_{j=1}^{n} P(A_j)$$
- For any $A_1, ..., A_n$ $$P(\bigcap_{i=1}^n = \sum_i P(A_i) - \sum_{i \lt j} P(A_i \cap A_j) + \sum_{i \lt j \lt k} P(A_i \cap A_j \cap A_k) - (-1)^{n+1} P(A_1 \cap ... \cap A_n))$$

9. Bose-Einstein: Updated later.

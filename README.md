# tilde-calculate
This is a manim to show to tilde-calculate: a~b = |a-b|

For the different permutations of the numbers 1, 2, 3, ..., n (n > 4), apply the "~" operation (left-associative) sequentially, i.e., for the permutation a1, a2, ..., an, the result is calculated as ((...((a1 ~ a2) ~ a3) ~ ... ~ an). We need to find the minimum (min) and maximum (max) of this operation result across all possible permutations.

### Thought Process
1. **Operation Property Analysis**: The operation a~b = |a-b| is a binary operation and left-associative. The final result depends on the order of the permutation.
2. **Parity Key**: Through analysis, it is found that the parity of the final result is consistent with the parity of the sum S = n(n+1)/2 of the numbers 1 to n. That is, L(S) ≡ S mod 2.
- If S is even, then L(S) is even; if S is odd, then L(S) is odd.
3. **Minimum Determination**:
   - When S is even, it can be arranged so that the final result is 0, hence min = 0.
   - When S is odd, the final result is at least 1 and can reach 1, hence min = 1.
4. **Determination of the Maximum Value**:
   - Through case analysis (n=3,4,5,6), it is found that the maximum value depends on the remainder of n divided by 4:
     - If n ≡ 0 or 1 mod 4, then max = n.
     - If n ≡ 2 or 3 mod 4, then max = n-1.
5. **Verification**: For n=5 (S=15 odd, min=1; n≡1 mod 4, max=5) and n=6 (S=21 odd, min=1; n≡2 mod 4, max=5), the results hold.

### Answer
For n > 4:
- **Minimum value min**:
- If n(n+1)/2 is even, then min = 0.
  - If n(n+1)/2 is odd, then min = 1.
- **Maximum value max**:
  - If n ≡ 0 or 1 mod 4, then max = n.
- If n ≡ 2 or 3 mod 4, then max = n-1.

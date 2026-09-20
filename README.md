# Coding practice — organised by pattern

Small interview-style problems, grouped by the technique they practise.
Each file is self-contained: a function (or `Solution` class) followed by
`print(...)` calls with `# expected:` comments. Run any one with
`python3 <folder>/<file>.py`.

Nothing has been deleted; near-duplicates are listed at the bottom.

## Folders

| Folder | What it practises | Files |
|---|---|---|
| `sliding-window/` | A `left`/`right` pair where `right` always advances and `left` catches up only when the window breaks a rule | 7 |
| `hashmaps-and-sets/` | Trading memory for O(1) lookups: seen-sets, frequency maps, last-seen-index maps, group-by | 9 |
| `two-pointers/` | Two indices moving through an array with different roles (slow/fast, left/right) — no window invariant | 1 |
| `prefix-sum-and-counting/` | Running total/balance + first index each value was seen; equal balance twice ⇒ the span between is "balanced" | 1 |
| `sorting-and-intervals/` | Sort first, then sweep — overlaps, rooms, scheduling | 1 |
| `arrays-and-strings/` | Single linear pass comparing neighbours; current/max run counters | 2 |
| `parsing-and-string-processing/` | Walking a string char by char with a small state machine; run-length; slicing | 3 |
| `maths-and-modulo/` | Remainder reasoning, digit manipulation | 3 |
| `api-and-json/` | `requests` + JSON responses + pagination loops | 1 |
| `linked-lists/` | Pointer manipulation on nodes | 1 |

## Patterns to recognise in an interview

**Sliding window** — trigger words: *longest / shortest / minimum-length subarray or
substring* with a constraint (unique chars, at most k distinct, sum ≥ target, at most
one zero). Two shapes:

- *Variable window* — `for right in range(n)`: add `nums[right]`, then
  `while <window invalid>: remove nums[left]; left += 1`, then record
  `right - left + 1`. Files: `longest_substring_without_repeating.py`,
  `longest_k_distinct.py`, `longest_streak_after_removal.py`, `min_subarray_sum.py`.
- *Fixed window of size k* — loop `i in range(n - k + 1)`. Files:
  `cheapest_delivery_window.py`, `first_unique_window.py`. Both currently re-slice
  and re-scan every window (O(n·k)); the upgrade is a rolling sum / rolling
  count so each step is O(1).

**Hashmap / set** — trigger words: *first repeated, most frequent, count pairs that
sum to, within k of each other, missing number, consecutive sequence*.

- Seen-set: `first_repeated_transaction.py`, `first_missing_positive_id.py`.
- Value → last index (for "within k"): `first_duplicate_within_k.py`.
- Value → count (frequency / two-sum-count): `most_frequent_error.py`,
  `transaction_pair_count.py` — note the *check before insert* ordering so an
  element can't pair with itself.
- Group-by aggregation: `transaction_summary.py`.
- Set as O(1) membership for sequence-building: `longest_consecutive_sequence.py`
  — the key line is `if num - 1 not in num_set` (only start from sequence heads,
  which keeps it O(n)).

**Two pointers (not a window)** — sorted input, in-place rewrite, or scanning from
both ends. `remove_duplicates_sorted_array.py`: `left` marks the write position,
`right` reads; write only when `nums[right]` is new.

**Prefix balance** — "longest subarray with equal 0s and 1s" cannot be done with a
window because removing from the left doesn't restore validity. Instead keep a
running `balance` (+1 / −1) and a map `balance → first index seen`, seeded with
`{0: -1}`. Same balance at indices `i` and `j` ⇒ subarray `(i, j]` is balanced.
`longest_balanced_binary.py` keeps the failed counter-based attempt commented out,
which is a useful reminder of *why* the window approach breaks.

**Sort + sweep** — `minimum_meeting_rooms.py`: sort starts and ends separately,
walk both with two pointers, `rooms += 1` on a start, `rooms -= 1` when an end
comes first. Max of `rooms` is the answer. Same skeleton handles "max concurrent
X" for any interval problem.

**Linear scan / run counting** — `first_peak_value.py`, `longest_increasing_run.py`,
`longest_character_run.py`: compare `i` with `i-1`, keep `current` and `best`.
Watch the tie-breaking rule (`>` vs `>=`) and the "reset to 1, not 0" on a break.

**String state machine** — `documentation_transform.py`: an `in_backticks` flag
and an accumulating buffer; act on the closing delimiter. Standard shape for any
"transform text between markers" question.

**Modulo** — `greatest_sum_divisible_by_three.py`: bucket numbers by `n % 3`; if the
total has remainder 1, drop either the smallest rem-1 number or the two smallest
rem-2 numbers (whichever costs less). Symmetric for remainder 2.

## Good revision problems

Start with these — each is the cleanest example of its pattern:

1. `sliding-window/longest_substring_without_repeating.py` — canonical variable window (LeetCode 3)
2. `sliding-window/longest_k_distinct.py` — variable window with a count map
3. `sliding-window/min_subarray_sum.py` — shrink-while-valid, *minimum* length (LeetCode 209)
4. `hashmaps-and-sets/first_duplicate_within_k.py` — value → last index (LeetCode 219)
5. `hashmaps-and-sets/transaction_pair_count.py` — two-sum counting
6. `hashmaps-and-sets/longest_consecutive_sequence.py` — set + sequence-start check (LeetCode 128)
7. `two-pointers/remove_duplicates_sorted_array.py` — slow/fast in-place (LeetCode 26)
8. `prefix-sum-and-counting/longest_balanced_binary.py` — prefix balance (LeetCode 525)
9. `sorting-and-intervals/minimum_meeting_rooms.py` — sort + sweep (LeetCode 253)
10. `parsing-and-string-processing/documentation_transform.py` — delimiter state machine
11. `maths-and-modulo/greatest_sum_divisible_by_three.py` — remainder buckets (LeetCode 1262)

## Unfinished / non-runnable files (kept as-is)

- `sliding-window/longest_unique_substring.py` — same problem as
  `longest_substring_without_repeating.py`; no `return` and the window never
  shrinks, so every test prints `None`. Worth finishing without looking at the
  other file.
- `hashmaps-and-sets/cheapest_supplier_cost.py` — stub with an empty `else:`
  (won't parse). Intended pattern: `productId → min price` map, return `-1` if
  any product id in `range(numProducts)` is missing.
- `api-and-json/API_practice.py` — snippet: no `import requests`, `url` undefined,
  and `all_records` is filled outside the page loop so it only ever holds the last
  page.
- `linked-lists/linklist.py` — iterative reversal body only; no `Node` class or
  `head`.

## Near-duplicates

- `longest_substring_without_repeating.py` ↔ `longest_unique_substring.py` — same problem.
- `first_duplicate_within_k.py` ↔ `earliest_repeat_window.py` — identical solution.
- `first_repeated_transaction.py` is the same idea with no distance limit.

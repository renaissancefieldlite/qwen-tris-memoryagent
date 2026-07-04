# MBPP Reflexion-Adjacent Slice - qwen_tris_mbpp_reflexion_slice_20260704T032927Z

## Boundary

Small local public MBPP slice. This is not an official leaderboard run.
It compares one-shot baseline generation against a Qwen Tris architecture-on
feedback/repair pass on the same tasks and same local model.

## Setup

- Dataset: `google-research-datasets/mbpp: sanitized`
- Split: `test`
- Model: `qwen2.5:3b`
- Offset: `0`
- Limit: `5`

## Result

- Baseline one-shot: `5/5`
- Qwen Tris architecture-on with one repair pass: `5/5`
- Delta: `+0` tasks

## Rows

| Task | Baseline | Tris architecture-on | Repair used |
|---|---:|---:|---:|
| `11` | pass | pass | no |
| `12` | pass | pass | no |
| `14` | pass | pass | no |
| `16` | pass | pass | no |
| `17` | pass | pass | no |

## Task Details

### Task `11`

Write a python function to remove first and last occurrence of a given character from the string.

Tests:

```python
assert remove_Occ("hello","l") == "heo"
assert remove_Occ("abcda","a") == "bcd"
assert remove_Occ("PHP","P") == "H"
```

Baseline: `passed`

Tris final: `passed`

### Task `12`

Write a function to sort a given matrix in ascending order according to the sum of its rows.

Tests:

```python
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
assert sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]])==[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
assert sort_matrix([[5,8,9],[6,4,3],[2,1,4]])==[[2, 1, 4], [6, 4, 3], [5, 8, 9]]
```

Baseline: `passed`

Tris final: `passed`

### Task `14`

Write a python function to find the volume of a triangular prism.

Tests:

```python
assert find_Volume(10,8,6) == 240
assert find_Volume(3,2,2) == 6
assert find_Volume(1,2,1) == 1
```

Baseline: `passed`

Tris final: `passed`

### Task `16`

Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.

Tests:

```python
assert text_lowercase_underscore("aab_cbbbc")==(True)
assert text_lowercase_underscore("aab_Abbbc")==(False)
assert text_lowercase_underscore("Aaab_abbbc")==(False)
```

Baseline: `passed`

Tris final: `passed`

### Task `17`

Write a function that returns the perimeter of a square given its side length as input.

Tests:

```python
assert square_perimeter(10)==40
assert square_perimeter(5)==20
assert square_perimeter(4)==16
```

Baseline: `passed`

Tris final: `passed`

# MBPP Reflexion-Adjacent Slice - qwen_tris_mbpp_reflexion_slice_20260704T033343Z

## Boundary

Small local public MBPP slice. This is not an official leaderboard run.
It compares one-shot baseline generation against the same generated code
after a Qwen Tris architecture-on feedback/repair pass on failing rows.
Passing baseline rows are not rewritten, so the reflection lane cannot
hide regressions by changing already-passing answers.

## Setup

- Dataset: `google-research-datasets/mbpp: sanitized`
- Split: `test`
- Model: `qwen2.5:3b`
- Offset: `0`
- Limit: `20`

## Result

- Baseline one-shot: `15/20`
- Qwen Tris architecture-on repair route: `16/20`
- Delta: `+1` tasks

## Rows

| Task | Baseline | Tris architecture-on | Repair used |
|---|---:|---:|---:|
| `11` | pass | pass | no |
| `12` | pass | pass | no |
| `14` | pass | pass | no |
| `16` | pass | pass | no |
| `17` | pass | pass | no |
| `18` | pass | pass | no |
| `19` | pass | pass | no |
| `20` | fail | fail | yes |
| `56` | fail | fail | yes |
| `57` | pass | pass | no |
| `58` | pass | pass | no |
| `59` | fail | pass | yes |
| `61` | fail | fail | yes |
| `62` | pass | pass | no |
| `63` | fail | fail | yes |
| `64` | pass | pass | no |
| `65` | pass | pass | no |
| `66` | pass | pass | no |
| `67` | pass | pass | no |
| `68` | pass | pass | no |

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

### Task `18`

Write a function to remove characters from the first string which are present in the second string.

Tests:

```python
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'
```

Baseline: `passed`

Tris final: `passed`

### Task `19`

Write a function to find whether a given array of integers contains any duplicate element.

Tests:

```python
assert test_duplicate(([1,2,3,4,5]))==False
assert test_duplicate(([1,2,3,4, 4]))==True
assert test_duplicate([1,1,2,2,3,3,4,4,5])==True
```

Baseline: `passed`

Tris final: `passed`

### Task `20`

Write a function to check if the given number is woodball or not.

Tests:

```python
assert is_woodall(383) == True
assert is_woodall(254) == False
assert is_woodall(200) == False
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `56`

Write a python function to check if a given number is one less than twice its reverse.

Tests:

```python
assert check(70) == False
assert check(23) == False
assert check(73) == True
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `57`

Write a python function to find the largest number that can be formed with the given list of digits.

Tests:

```python
assert find_Max_Num([1,2,3]) == 321
assert find_Max_Num([4,5,6,1]) == 6541
assert find_Max_Num([1,2,3,9]) == 9321
```

Baseline: `passed`

Tris final: `passed`

### Task `58`

Write a python function to check whether the given two integers have opposite sign or not.

Tests:

```python
assert opposite_Signs(1,-2) == True
assert opposite_Signs(3,2) == False
assert opposite_Signs(-10,-10) == False
```

Baseline: `passed`

Tris final: `passed`

### Task `59`

Write a function to find the nth octagonal number.

Tests:

```python
assert is_octagonal(5) == 65
assert is_octagonal(10) == 280
assert is_octagonal(15) == 645
```

Baseline: `test_failure`

Tris final: `passed`

### Task `61`

Write a python function to count the number of substrings with the sum of digits equal to their length.

Tests:

```python
assert count_Substrings('112112') == 6
assert count_Substrings('111') == 6
assert count_Substrings('1101112') == 12
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `62`

Write a python function to find smallest number in a list.

Tests:

```python
assert smallest_num([10, 20, 1, 45, 99]) == 1
assert smallest_num([1, 2, 3]) == 1
assert smallest_num([45, 46, 50, 60]) == 45
```

Baseline: `passed`

Tris final: `passed`

### Task `63`

Write a function to find the maximum difference between available pairs in the given tuple list.

Tests:

```python
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
assert max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
assert max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `64`

Write a function to sort a list of tuples using the second value of each tuple.

Tests:

```python
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
assert subject_marks([('Telugu',49),('Hindhi',54),('Social',33)])==([('Social',33),('Telugu',49),('Hindhi',54)])
assert subject_marks([('Physics',96),('Chemistry',97),('Biology',45)])==([('Biology',45),('Physics',96),('Chemistry',97)])
```

Baseline: `passed`

Tris final: `passed`

### Task `65`

Write a function to flatten a list and sum all of its elements.

Tests:

```python
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
assert recursive_list_sum(([7, 10, [15,14],[19,41]]))==106
assert recursive_list_sum(([10, 20, [30,40],[50,60]]))==210
```

Baseline: `passed`

Tris final: `passed`

### Task `66`

Write a python function to count the number of positive numbers in a list.

Tests:

```python
assert pos_count([1,-2,3,-4]) == 2
assert pos_count([3,4,5,-1]) == 3
assert pos_count([1,2,3,4]) == 4
```

Baseline: `passed`

Tris final: `passed`

### Task `67`

Write a function to find the number of ways to partition a set of Bell numbers.

Tests:

```python
assert bell_number(2)==2
assert bell_number(10)==115975
assert bell_number(56)==6775685320645824322581483068371419745979053216268760300
```

Baseline: `passed`

Tris final: `passed`

### Task `68`

Write a python function to check whether the given array is monotonic or not.

Tests:

```python
assert is_Monotonic([6, 5, 4, 4]) == True
assert is_Monotonic([1, 2, 2, 3]) == True
assert is_Monotonic([1, 3, 2]) == False
```

Baseline: `passed`

Tris final: `passed`

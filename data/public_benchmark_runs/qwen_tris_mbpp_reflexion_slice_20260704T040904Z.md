# MBPP Reflexion-Adjacent Slice - qwen_tris_mbpp_reflexion_slice_20260704T040904Z

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
- Limit: `50`

## Result

- Baseline one-shot: `35/50`
- Qwen Tris architecture-on repair route: `38/50`
- Delta: `+3` tasks

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
| `69` | fail | fail | yes |
| `70` | pass | pass | no |
| `71` | fail | pass | yes |
| `72` | fail | fail | yes |
| `74` | fail | fail | yes |
| `75` | pass | pass | no |
| `77` | pass | pass | no |
| `79` | pass | pass | no |
| `80` | pass | pass | no |
| `82` | pass | pass | no |
| `83` | fail | fail | yes |
| `84` | pass | pass | no |
| `85` | pass | pass | no |
| `86` | fail | fail | yes |
| `87` | fail | fail | yes |
| `88` | pass | pass | no |
| `89` | pass | pass | no |
| `90` | pass | pass | no |
| `91` | fail | fail | yes |
| `92` | fail | fail | yes |
| `93` | pass | pass | no |
| `94` | pass | pass | no |
| `95` | pass | pass | no |
| `96` | pass | pass | no |
| `97` | pass | pass | no |
| `98` | fail | pass | yes |
| `99` | pass | pass | no |
| `100` | pass | pass | no |
| `101` | pass | pass | no |
| `102` | pass | pass | no |

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

### Task `69`

Write a function to check whether a list contains the given sublist or not.

Tests:

```python
assert is_sublist([2,4,3,5,7],[3,7])==False
assert is_sublist([2,4,3,5,7],[4,3])==True
assert is_sublist([2,4,3,5,7],[1,6])==False
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `70`

Write a function to find whether all the given tuples have equal length or not.

Tests:

```python
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
assert get_equal([(1, 2, 3), (4, 5, 6, 7)]) == False
assert get_equal([(1, 2), (3, 4)]) == True
```

Baseline: `passed`

Tris final: `passed`

### Task `71`

Write a function to sort a list of elements.

Tests:

```python
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
assert comb_sort([41, 32, 15, 19, 22]) == [15, 19, 22, 32, 41]
assert comb_sort([99, 15, 13, 47]) == [13, 15, 47, 99]
```

Baseline: `test_failure`

Tris final: `passed`

### Task `72`

Write a python function to check whether the given number can be represented as the difference of two squares or not.

Tests:

```python
assert dif_Square(5) == True
assert dif_Square(10) == False
assert dif_Square(15) == True
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `74`

Write a function to check whether it follows the sequence given in the patterns array.

Tests:

```python
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
assert is_samepatterns(["red","green","greenn"], ["a","b"])==False
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `75`

Write a function to find tuples which have all elements divisible by k from the given list of tuples.

Tests:

```python
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
assert find_tuples([(5, 25, 30), (4, 2, 3), (7, 8, 9)], 5) == [(5, 25, 30)]
assert find_tuples([(7, 9, 16), (8, 16, 4), (19, 17, 18)], 4) == [(8, 16, 4)]
```

Baseline: `passed`

Tris final: `passed`

### Task `77`

Write a python function to find whether a number is divisible by 11.

Tests:

```python
assert is_Diff (12345) == False
assert is_Diff(1212112) == True
assert is_Diff(1212) == False
```

Baseline: `passed`

Tris final: `passed`

### Task `79`

Write a python function to check whether the length of the word is odd or not.

Tests:

```python
assert word_len("Hadoop") == False
assert word_len("great") == True
assert word_len("structure") == True
```

Baseline: `passed`

Tris final: `passed`

### Task `80`

Write a function to find the nth tetrahedral number.

Tests:

```python
assert tetrahedral_number(5) == 35
assert tetrahedral_number(6) == 56
assert tetrahedral_number(7) == 84
```

Baseline: `passed`

Tris final: `passed`

### Task `82`

Write a function to find the volume of a sphere.

Tests:

```python
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
assert math.isclose(volume_sphere(25), 65449.84694978735, rel_tol=0.001)
assert math.isclose(volume_sphere(20), 33510.32163829113, rel_tol=0.001)
```

Baseline: `passed`

Tris final: `passed`

### Task `83`

Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.

Tests:

```python
assert get_Char("abc") == "f"
assert get_Char("gfg") == "t"
assert get_Char("ab") == "c"
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `84`

Write a function to find the nth number in the newman conway sequence.

Tests:

```python
assert sequence(10) == 6
assert sequence(2) == 1
assert sequence(3) == 2
```

Baseline: `passed`

Tris final: `passed`

### Task `85`

Write a function to find the surface area of a sphere.

Tests:

```python
assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)
assert math.isclose(surfacearea_sphere(15), 2827.4333882308138, rel_tol=0.001)
assert math.isclose(surfacearea_sphere(20), 5026.548245743669, rel_tol=0.001)
```

Baseline: `passed`

Tris final: `passed`

### Task `86`

Write a function to find nth centered hexagonal number.

Tests:

```python
assert centered_hexagonal_number(10) == 271
assert centered_hexagonal_number(2) == 7
assert centered_hexagonal_number(9) == 217
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `87`

Write a function to merge three dictionaries into a single dictionary.

Tests:

```python
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{"L":"lavender","B":"Blue"})=={'W': 'White', 'P': 'Pink', 'B': 'Black', 'R': 'Red', 'G': 'Green', 'L': 'lavender'}
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" },{"L":"lavender","B":"Blue"},{ "G": "Green", "W": "White" })=={'B': 'Black', 'P': 'Pink', 'R': 'Red', 'G': 'Green', 'L': 'lavender', 'W': 'White'}
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `88`

Write a function to get the frequency of all the elements in a list, returned as a dictionary.

Tests:

```python
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
assert freq_count([1,2,3,4,3,2,4,1,3,1,4])==({1:3, 2:2,3:3,4:3})
assert freq_count([5,6,7,4,9,10,4,5,6,7,9,5])==({10:1,5:3,6:2,7:2,4:2,9:2})
```

Baseline: `passed`

Tris final: `passed`

### Task `89`

Write a function to find the closest smaller number than n.

Tests:

```python
assert closest_num(11) == 10
assert closest_num(7) == 6
assert closest_num(12) == 11
```

Baseline: `passed`

Tris final: `passed`

### Task `90`

Write a python function to find the length of the longest word.

Tests:

```python
assert len_log(["python","PHP","bigdata"]) == 7
assert len_log(["a","ab","abc"]) == 3
assert len_log(["small","big","tall"]) == 5
```

Baseline: `passed`

Tris final: `passed`

### Task `91`

Write a function to check if a string is present as a substring in a given list of string values.

Tests:

```python
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
assert find_substring(["red", "black", "white", "green", "orange"],"abc")==False
assert find_substring(["red", "black", "white", "green", "orange"],"ange")==True
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `92`

Write a function to check whether the given number is undulating or not.

Tests:

```python
assert is_undulating(1212121) == True
assert is_undulating(1991) == False
assert is_undulating(121) == True
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `93`

Write a function to calculate the value of 'a' to the power 'b'.

Tests:

```python
assert power(3,4) == 81
assert power(2,3) == 8
assert power(5,5) == 3125
```

Baseline: `passed`

Tris final: `passed`

### Task `94`

Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.

Tests:

```python
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
assert index_minimum([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'
assert index_minimum([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'
```

Baseline: `passed`

Tris final: `passed`

### Task `95`

Write a python function to find the length of the smallest list in a list of lists.

Tests:

```python
assert Find_Min_Length([[1],[1,2]]) == 1
assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3
```

Baseline: `passed`

Tris final: `passed`

### Task `96`

Write a python function to find the number of divisors of a given integer.

Tests:

```python
assert divisor(15) == 4
assert divisor(12) == 6
assert divisor(9) == 3
```

Baseline: `passed`

Tris final: `passed`

### Task `97`

Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.

Tests:

```python
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
assert frequency_lists([[1,2,3,4],[5,6,7,8],[9,10,11,12]])=={1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1,10:1,11:1,12:1}
assert frequency_lists([[20,30,40,17],[18,16,14,13],[10,20,30,40]])=={20:2,30:2,40:2,17: 1,18:1, 16: 1,14: 1,13: 1, 10: 1}
```

Baseline: `passed`

Tris final: `passed`

### Task `98`

Write a function to multiply all the numbers in a list and divide with the length of the list.

Tests:

```python
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
assert math.isclose(multiply_num((-10,-20,-30)), -2000.0, rel_tol=0.001)
assert math.isclose(multiply_num((19,15,18)), 1710.0, rel_tol=0.001)
```

Baseline: `test_failure`

Tris final: `passed`

### Task `99`

Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.

Tests:

```python
assert decimal_to_binary(8) == '1000'
assert decimal_to_binary(18) == '10010'
assert decimal_to_binary(7) == '111'
```

Baseline: `passed`

Tris final: `passed`

### Task `100`

Write a function to find the next smallest palindrome of a specified integer, returned as an integer.

Tests:

```python
assert next_smallest_palindrome(99)==101
assert next_smallest_palindrome(1221)==1331
assert next_smallest_palindrome(120)==121
```

Baseline: `passed`

Tris final: `passed`

### Task `101`

Write a function to find the kth element in the given array using 1-based indexing.

Tests:

```python
assert kth_element([12,3,5,7,19], 2) == 3
assert kth_element([17,24,8,23], 3) == 8
assert kth_element([16,21,25,36,4], 4) == 36
```

Baseline: `passed`

Tris final: `passed`

### Task `102`

Write a function to convert a snake case string to camel case string.

Tests:

```python
assert snake_to_camel('python_program')=='PythonProgram'
assert snake_to_camel('python_language')==('PythonLanguage')
assert snake_to_camel('programming_language')==('ProgrammingLanguage')
```

Baseline: `passed`

Tris final: `passed`

# MBPP Reflexion-Adjacent Slice - qwen_tris_mbpp_reflexion_slice_20260704T062754Z

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
- Limit: `100`

## Result

- Baseline one-shot: `67/100`
- Qwen Tris architecture-on repair route: `71/100`
- Delta: `+4` tasks

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
| `103` | fail | fail | yes |
| `104` | pass | pass | no |
| `105` | pass | pass | no |
| `106` | pass | pass | no |
| `108` | fail | fail | yes |
| `109` | pass | pass | no |
| `111` | pass | pass | no |
| `113` | pass | pass | no |
| `115` | fail | fail | yes |
| `116` | pass | pass | no |
| `117` | fail | fail | yes |
| `118` | pass | pass | no |
| `119` | pass | pass | no |
| `120` | pass | pass | no |
| `123` | pass | pass | no |
| `124` | fail | fail | yes |
| `125` | fail | fail | yes |
| `126` | fail | fail | yes |
| `127` | pass | pass | no |
| `128` | pass | pass | no |
| `129` | fail | fail | yes |
| `130` | pass | pass | no |
| `131` | pass | pass | no |
| `132` | pass | pass | no |
| `133` | pass | pass | no |
| `135` | pass | pass | no |
| `137` | fail | fail | yes |
| `138` | fail | fail | yes |
| `139` | pass | pass | no |
| `140` | pass | pass | no |
| `141` | pass | pass | no |
| `142` | pass | pass | no |
| `143` | fail | fail | yes |
| `145` | fail | fail | yes |
| `160` | fail | fail | yes |
| `161` | pass | pass | no |
| `162` | fail | pass | yes |
| `163` | fail | fail | yes |
| `164` | fail | fail | yes |
| `165` | fail | fail | yes |
| `166` | pass | pass | no |
| `167` | pass | pass | no |
| `168` | pass | pass | no |
| `170` | pass | pass | no |
| `171` | pass | pass | no |
| `172` | pass | pass | no |
| `222` | pass | pass | no |
| `223` | fail | fail | yes |
| `224` | pass | pass | no |
| `226` | pass | pass | no |

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

### Task `103`

Write a function to find the Eulerian number a(n, m).

Tests:

```python
assert eulerian_num(3, 1) == 4
assert eulerian_num(4, 1) == 11
assert eulerian_num(5, 3) == 26
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `104`

Write a function to sort each sublist of strings in a given list of lists.

Tests:

```python
assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
assert sort_sublists(([" red ","green" ],["blue "," black"],[" orange","brown"]))==[[' red ', 'green'], [' black', 'blue '], [' orange', 'brown']]
assert sort_sublists((["zilver","gold"], ["magnesium","aluminium"], ["steel", "bronze"]))==[['gold', 'zilver'],['aluminium', 'magnesium'], ['bronze', 'steel']]
```

Baseline: `passed`

Tris final: `passed`

### Task `105`

Write a python function to count true booleans in the given list.

Tests:

```python
assert count([True,False,True]) == 2
assert count([False,False]) == 0
assert count([True,True,True]) == 3
```

Baseline: `passed`

Tris final: `passed`

### Task `106`

Write a function to append the given list to the given tuples.

Tests:

```python
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
assert add_lists([6, 7, 8], (10, 11)) == (10, 11, 6, 7, 8)
assert add_lists([7, 8, 9], (11, 12)) == (11, 12, 7, 8, 9)
```

Baseline: `passed`

Tris final: `passed`

### Task `108`

Write a function to merge three lists into a single sorted list.

Tests:

```python
assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
assert merge_sorted_list([1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12])==[1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 11, 12]
assert merge_sorted_list([18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1],[25, 35, 22, 85, 14, 65, 75, 25, 58],[12, 74, 9, 50, 61, 41])==[1, 2, 3, 4, 7, 8, 9, 9, 9, 10, 12, 14, 14, 18, 22, 25, 25, 35, 41, 50, 58, 61, 65, 74, 75, 85]
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `109`

Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.

Tests:

```python
assert odd_Equivalent("011001",6) == 3
assert odd_Equivalent("11011",5) == 4
assert odd_Equivalent("1010",4) == 2
```

Baseline: `passed`

Tris final: `passed`

### Task `111`

Write a function to find the common elements in given nested lists.

Tests:

```python
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
assert set(common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]]))==set([5,23])
assert set(common_in_nested_lists([[2, 3,4, 1], [4, 5], [6,4, 8],[4, 5], [6, 8,4]]))==set([4])
```

Baseline: `passed`

Tris final: `passed`

### Task `113`

Write a function to check if a string represents an integer or not.

Tests:

```python
assert check_integer("python")==False
assert check_integer("1")==True
assert check_integer("12345")==True
```

Baseline: `passed`

Tris final: `passed`

### Task `115`

Write a function to check whether all dictionaries in a list are empty or not.

Tests:

```python
assert empty_dit([{},{},{}])==True
assert empty_dit([{1,2},{},{}])==False
assert empty_dit({})==True
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `116`

Write a function to convert a given tuple of positive integers into a single integer.

Tests:

```python
assert tuple_to_int((1,2,3))==123
assert tuple_to_int((4,5,6))==456
assert tuple_to_int((5,6,7))==567
```

Baseline: `passed`

Tris final: `passed`

### Task `117`

Write a function to convert all possible convertible elements in a list of lists to floats.

Tests:

```python
assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
assert list_to_float( [("4", "4"), ("2", "27"), ("4.12", "9"), ("7", "11")] ) == [(4.0, 4.0), (2.0, 27.0), (4.12, 9.0), (7.0, 11.0)]
assert list_to_float( [("6", "78"), ("5", "26.45"), ("1.33", "4"), ("82", "13")] ) == [(6.0, 78.0), (5.0, 26.45), (1.33, 4.0), (82.0, 13.0)]
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `118`

Write a function to convert a string to a list of strings split on the space character.

Tests:

```python
assert string_to_list("python programming")==['python','programming']
assert string_to_list("lists tuples strings")==['lists','tuples','strings']
assert string_to_list("write a program")==['write','a','program']
```

Baseline: `passed`

Tris final: `passed`

### Task `119`

Write a python function to find the element that appears only once in a sorted array.

Tests:

```python
assert search([1,1,2,2,3]) == 3
assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
assert search([1,2,2,3,3,4,4]) == 1
```

Baseline: `passed`

Tris final: `passed`

### Task `120`

Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.

Tests:

```python
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
assert max_product_tuple([(10,20), (15,2), (5,10)] )==200
assert max_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==484
```

Baseline: `passed`

Tris final: `passed`

### Task `123`

Write a function to sum all amicable numbers from 1 to a specified number.

Tests:

```python
assert amicable_numbers_sum(999)==504
assert amicable_numbers_sum(9999)==31626
assert amicable_numbers_sum(99)==0
```

Baseline: `passed`

Tris final: `passed`

### Task `124`

Write a function to get the angle of a complex number.

Tests:

```python
assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
assert math.isclose(angle_complex(2,1j), 0.4636476090008061, rel_tol=0.001)
assert math.isclose(angle_complex(0,2j), 1.5707963267948966, rel_tol=0.001)
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `125`

Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.

Tests:

```python
assert find_length("11000010001") == 6
assert find_length("10111") == 1
assert find_length("11011101100101") == 2
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `126`

Write a python function to find the sum of common divisors of two given numbers.

Tests:

```python
assert sum(10,15) == 6
assert sum(100,150) == 93
assert sum(4,6) == 3
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `127`

Write a function to multiply two integers.

Tests:

```python
assert multiply_int(10,20)==200
assert multiply_int(5,10)==50
assert multiply_int(4,8)==32
```

Baseline: `passed`

Tris final: `passed`

### Task `128`

Write a function to find words that are longer than n characters from a given list of words.

Tests:

```python
assert long_words(3,"python is a programming language")==['python','programming','language']
assert long_words(2,"writing a program")==['writing','program']
assert long_words(5,"sorting list")==['sorting']
```

Baseline: `passed`

Tris final: `passed`

### Task `129`

Write a function to calculate whether the matrix is a magic square.

Tests:

```python
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `130`

Write a function to find the item with maximum frequency in a given list.

Tests:

```python
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,18])==8
assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==20
```

Baseline: `passed`

Tris final: `passed`

### Task `131`

Write a python function to reverse only the vowels of a given string (where y is not a vowel).

Tests:

```python
assert reverse_vowels("Python") == "Python"
assert reverse_vowels("USA") == "ASU"
assert reverse_vowels("ab") == "ab"
```

Baseline: `passed`

Tris final: `passed`

### Task `132`

Write a function to convert a tuple to a string.

Tests:

```python
assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")
assert tup_string(('p','y','t','h','o','n'))==("python")
assert tup_string(('p','r','o','g','r','a','m'))==("program")
```

Baseline: `passed`

Tris final: `passed`

### Task `133`

Write a function to calculate the sum of the negative numbers of a given list of numbers.

Tests:

```python
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
assert sum_negativenum([10,15,-14,13,-18,12,-20])==-52
assert sum_negativenum([19, -65, 57, 39, 152,-639, 121, 44, 90, -190])==-894
```

Baseline: `passed`

Tris final: `passed`

### Task `135`

Write a function to find the nth hexagonal number.

Tests:

```python
assert hexagonal_num(10) == 190
assert hexagonal_num(5) == 45
assert hexagonal_num(7) == 91
```

Baseline: `passed`

Tris final: `passed`

### Task `137`

Write a function to find the ratio of zeroes to non-zeroes in an array of integers.

Tests:

```python
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
assert math.isclose(zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]), 0.00, rel_tol=0.001)
assert math.isclose(zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17]), 0.00, rel_tol=0.001)
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `138`

Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.

Tests:

```python
assert is_Sum_Of_Powers_Of_Two(10) == True
assert is_Sum_Of_Powers_Of_Two(7) == False
assert is_Sum_Of_Powers_Of_Two(14) == True
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `139`

Write a function to find the circumference of a circle.

Tests:

```python
assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
assert math.isclose(circle_circumference(5), 31.415000000000003, rel_tol=0.001)
assert math.isclose(circle_circumference(4), 25.132, rel_tol=0.001)
```

Baseline: `passed`

Tris final: `passed`

### Task `140`

Write a function to flatten the list of lists into a single set of numbers.

Tests:

```python
assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
assert set(extract_singly([(1, 2, 3), (4, 2, 3), (7, 8)])) == set([1, 2, 3, 4, 7, 8])
assert set(extract_singly([(7, 8, 9), (10, 11, 12), (10, 11)])) == set([7, 8, 9, 10, 11, 12])
```

Baseline: `passed`

Tris final: `passed`

### Task `141`

Write a function to sort a list of elements.

Tests:

```python
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]
```

Baseline: `passed`

Tris final: `passed`

### Task `142`

Write a function to count number items that are identical in the same position of three given lists.

Tests:

```python
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==4
assert count_samepair([1,2,3,4,2,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==5
```

Baseline: `passed`

Tris final: `passed`

### Task `143`

Write a function to find number of lists present in the given tuple.

Tests:

```python
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
assert find_lists(([1, 2], [3, 4], [5, 6]))  == 3
assert find_lists(([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 1
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `145`

Write a python function to find the maximum difference between any two elements in a given array.

Tests:

```python
assert max_Abs_Diff((2,1,5,3)) == 4
assert max_Abs_Diff((9,3,2,5,1)) == 8
assert max_Abs_Diff((3,2,1)) == 2
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `160`

Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.

Tests:

```python
assert find_solution(2, 3, 7) == (2, 1)
assert find_solution(4, 2, 7) == None
assert find_solution(1, 13, 17) == (4, 1)
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `161`

Write a function to remove all elements from a given list present in another list.

Tests:

```python
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7]) == [2, 4, 6, 8, 9, 10]
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 7]) == [1, 2, 3, 4, 6, 8, 9, 10]
```

Baseline: `passed`

Tris final: `passed`

### Task `162`

Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).

Tests:

```python
assert sum_series(6) == 12
assert sum_series(10) == 30
assert sum_series(9) == 25
```

Baseline: `test_failure`

Tris final: `passed`

### Task `163`

Write a function to calculate the area of a regular polygon given the length and number of its sides.

Tests:

```python
assert math.isclose(area_polygon(4, 20), 400., rel_tol=0.001)
assert math.isclose(area_polygon(10, 15), 1731.197, rel_tol=0.001)
assert math.isclose(area_polygon(9, 7), 302.909, rel_tol=0.001)
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `164`

Write a function to determine if the sum of the divisors of two integers are the same.

Tests:

```python
assert are_equivalent(36, 57) == False
assert are_equivalent(2, 4) == False
assert are_equivalent(23, 47) == True
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `165`

Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).

Tests:

```python
assert count_char_position("xbcefg") == 2
assert count_char_position("ABcED") == 3
assert count_char_position("AbgdeF") == 5
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `166`

Write a function that counts the number of pairs of integers in a list that xor to an even number.

Tests:

```python
assert find_even_pair([5, 4, 7, 2, 1]) == 4
assert find_even_pair([7, 2, 8, 1, 0, 5, 11]) == 9
assert find_even_pair([1, 2, 3]) == 1
```

Baseline: `passed`

Tris final: `passed`

### Task `167`

Write a python function to find the smallest power of 2 greater than or equal to n.

Tests:

```python
assert next_power_of_2(0) == 1
assert next_power_of_2(5) == 8
assert next_power_of_2(17) == 32
```

Baseline: `passed`

Tris final: `passed`

### Task `168`

Write a function to count the number of occurrences of a number in a given list.

Tests:

```python
assert frequency([1,2,3], 4) == 0
assert frequency([1,2,2,3,3,3,4], 3) == 3
assert frequency([0,1,2,3,1,2], 1) == 2
```

Baseline: `passed`

Tris final: `passed`

### Task `170`

Write a function to find the sum of numbers in a list within a range specified by two indices.

Tests:

```python
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 5, 7) == 16
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 7, 10) == 38
```

Baseline: `passed`

Tris final: `passed`

### Task `171`

Write a function to find the perimeter of a regular pentagon from the length of its sides.

Tests:

```python
assert perimeter_pentagon(5) == 25
assert perimeter_pentagon(10) == 50
assert perimeter_pentagon(15) == 75
```

Baseline: `passed`

Tris final: `passed`

### Task `172`

Write a function to count the number of occurence of the string 'std' in a given string.

Tests:

```python
assert count_occurance("letstdlenstdporstd") == 3
assert count_occurance("truststdsolensporsd") == 1
assert count_occurance("makestdsostdworthit") == 2
```

Baseline: `passed`

Tris final: `passed`

### Task `222`

Write a function to check if all the elements in tuple have same data type or not.

Tests:

```python
assert check_type((5, 6, 7, 3, 5, 6) ) == True
assert check_type((1, 2, "4") ) == False
assert check_type((3, 2, 1, 4, 5) ) == True
```

Baseline: `passed`

Tris final: `passed`

### Task `223`

Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)

Tests:

```python
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
```

Baseline: `test_failure`

Tris final: `test_failure`

### Task `224`

Write a python function to count the number of set bits (binary digits with value 1) in a given number.

Tests:

```python
assert count_Set_Bits(2) == 1
assert count_Set_Bits(4) == 1
assert count_Set_Bits(6) == 2
```

Baseline: `passed`

Tris final: `passed`

### Task `226`

Write a python function to remove the characters which have odd index values of a given string.

Tests:

```python
assert odd_values_string('abcdef') == 'ace'
assert odd_values_string('python') == 'pto'
assert odd_values_string('data') == 'dt'
```

Baseline: `passed`

Tris final: `passed`

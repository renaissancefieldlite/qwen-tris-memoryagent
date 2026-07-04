# HumanEval-Instruct Reflexion-Adjacent Slice - qwen_tris_humaneval_reflexion_slice_20260704T062754Z

## Boundary

Small local public HumanEval-instruct slice. This is not an official
leaderboard run. It compares baseline one-shot code generation against
the same generated code after a Qwen Tris architecture-on repair pass
on failing rows only.

## Setup

- Dataset: `openai/openai_humaneval`
- Split: `test`
- Model: `qwen2.5:3b`
- Offset: `0`
- Limit: `20`

## Result

- Baseline one-shot: `14/20`
- Qwen Tris architecture-on repair route: `14/20`
- Delta: `+0` tasks

## Rows

| Task | Entry point | Baseline | Tris architecture-on | Repair used |
|---|---|---:|---:|---:|
| `HumanEval/0` | `has_close_elements` | pass | pass | no |
| `HumanEval/1` | `separate_paren_groups` | fail | fail | yes |
| `HumanEval/2` | `truncate_number` | fail | fail | yes |
| `HumanEval/3` | `below_zero` | pass | pass | no |
| `HumanEval/4` | `mean_absolute_deviation` | fail | fail | yes |
| `HumanEval/5` | `intersperse` | pass | pass | no |
| `HumanEval/6` | `parse_nested_parens` | pass | pass | no |
| `HumanEval/7` | `filter_by_substring` | pass | pass | no |
| `HumanEval/8` | `sum_product` | pass | pass | no |
| `HumanEval/9` | `rolling_max` | pass | pass | no |
| `HumanEval/10` | `make_palindrome` | fail | fail | yes |
| `HumanEval/11` | `string_xor` | pass | pass | no |
| `HumanEval/12` | `longest` | pass | pass | no |
| `HumanEval/13` | `greatest_common_divisor` | pass | pass | no |
| `HumanEval/14` | `all_prefixes` | fail | fail | yes |
| `HumanEval/15` | `string_sequence` | pass | pass | no |
| `HumanEval/16` | `count_distinct_characters` | pass | pass | no |
| `HumanEval/17` | `parse_music` | fail | fail | yes |
| `HumanEval/18` | `how_many_times` | pass | pass | no |
| `HumanEval/19` | `sort_numbers` | pass | pass | no |

## Failure/Repair Notes

### `HumanEval/1`

Baseline: `test_failure`

Tris final: `test_failure`

### `HumanEval/2`

Baseline: `test_failure`

Tris final: `test_failure`

### `HumanEval/4`

Baseline: `test_failure`

Tris final: `test_failure`

### `HumanEval/10`

Baseline: `test_failure`

Tris final: `test_failure`

### `HumanEval/14`

Baseline: `test_failure`

Tris final: `test_failure`

### `HumanEval/17`

Baseline: `test_failure`

Tris final: `test_failure`

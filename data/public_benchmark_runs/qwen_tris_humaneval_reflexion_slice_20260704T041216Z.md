# HumanEval-Instruct Reflexion-Adjacent Slice - qwen_tris_humaneval_reflexion_slice_20260704T041216Z

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
- Limit: `10`

## Result

- Baseline one-shot: `7/10`
- Qwen Tris architecture-on repair route: `7/10`
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

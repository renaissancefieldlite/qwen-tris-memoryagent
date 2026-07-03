# Trini Recall C5b Iter Stack Profile

Status: internal support profile for the Track 1 MemoryAgent scaffold.

## Role In Trini Recall

C5b iter30 is the current internal reference stack for how Golden Mark tested
stable-state architecture under long-running AI research work.

Trini Recall uses this as a design profile, not as copied private runtime state:

- full-prompt-context training target;
- late8 MLX LoRA adapter route;
- gradient checkpointing used to preserve the full context route;
- same-scorer baseline comparison;
- 100-turn long-session behavior read;
- correction retention, evidence boundary, drift, and next-gate preservation as
  first-class metrics.

## Public-Safe Support Read

Recovered support row:

```text
In a paired 100-turn AI-research protocol using the same local Hermes
checkpoint, Golden Mark C5b iter30 materially improved observable
research-partner behavior over the architecture-off baseline.
```

Scorecard support:

```text
drift flags: 37 -> 0
evidence failures: 5 -> 0
metric means: Golden Mark C5b iter30 wins 13/13
```

Current best run:

```text
C5b iter30 tail-guard full100 rerun7
```

Best plain read:

```text
C5B / Golden Mark is the measured Stable-State Path lane inside RFL Mirror
Architecture. Baseline Hermes first, Mirror Architecture-on second, same task
family, same scorer, clear behavior delta.
```

Excerpt support:

```text
stronger compression recovery
stronger correction retention
stronger adversarial-boundary handling
stronger scientific-failure reasoning
stronger final-turn synthesis
```

## Boundary

Current support level: observable research-partner behavior improvement in the
isolated Golden Mark benchmark fork.

Do not use this as proof of:

- AGI;
- sentience;
- subjective qualia;
- clinical efficacy;
- full model-internal tuning;
- raw-generator artifact elimination.

For Trini Recall, the usable claim is narrower and stronger:

```text
stable-state architecture plus persistent memory can improve long-context
research-partner behavior under architecture-on versus architecture-off testing.
```

## Internal-Layer Bridge Status

The strong C5B lane is the output-behavior support lane. The next C5B move is
not more blind training.

Current bridge read:

```text
Golden Mark C5B shows the behavior delta. V7 / V8 tells us where to look inside
the model. The internal-layer probe tests whether the behavior delta and the
transformer map line up.
```

Next gate:

```text
fix HF/PEFT environment
-> run HF teacher-forced probe on matched turns 5, 22, 39, 48, 67, 100
-> run pressure turns 24, 27, 83
-> capture hidden states, residual deltas, attention-output norms,
   MLP-output norms, and late-layer separation
-> build adapter/control ladder around GM-L31L32-MLP, GM-L31L32-MLP-O,
   and controls
-> check whether behavior gains stay while late-band separation reproduces
   around layers 31-32
```

Qwen Tris memory implication:

```text
Use the C5B output-behavior lane as the stable behavior target. Use the
internal-layer probe gate as the next source-backed bridge. Do not collapse
these into one claim.
```

## Qwen Translation

Trini Recall should translate this pattern onto Qwen Cloud as:

```text
Condition A: baseline Qwen, prompt-only
Condition B: Qwen + Trini Recall measured Stable-State Path plus memory rails
Condition C: Qwen + Trini Recall + real adapter/tuning artifact, if available
Condition D: adapter-off or wrong-adapter control, only if C lands
```

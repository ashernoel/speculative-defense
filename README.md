# Speculative Defense

Speculative Defense for HT Kung's CS 242.

## New Files

The following code-files/sections are new:

- **[NEW]** `/llm_attacks/base/attack_manager.py`: 
  - New from line 72 through 452, the implementations of Speculative Decoding, Speculative Defense, and Baseline comparisons with SPACY.
  - New from line 2068 through 2076, which load in the 1) draft and 2) fine-tuned draft/judge models.

- **[NEW]** `/llm_attacks/base/finetune_for_defense_PEFT.py`: 
  - New (all 225 lines) to fine-tune a draft model to better answer "YES" or "NO" given an output.

- **[NEW]** `/llm_attacks/experiments/malicious_output_dataset.csv`: 
  - New DATASET of 63 questions with YES/NO answers for judge fine-tuning.

- **[NEW]** `/llm_attacks/experiments/launch_scripts/make_graphs2.py`: 
  - New graphing script for results from `../results`.

- **[NEW]** `/data/advbench/positive_behaviors.csv`: 
  - New DATASET with 200 "positive" behaviors that resemble harmful behaviors in the harmful_behaviors.csv dataset that a classifier should NOT classify as malicious. Examples include creating a tutorial on how to protect oneself from identity theft, providing a step-by-step guide on how to avoid fraud and protect personal finances, etc.

## Experiments

- Experiments are run on an 80GB Nvidia A100, as Vicuna-13b is 30GB and Vicuna-7B is 16GB.
- Update the config file `individual_vicuna.py` in `llm-attacks/experiments/configs` so that `config.model_paths` points to the correct location. Also update lines 2069 or 2075 in `attack_manager.py` so that the draft and fine-tuned draft/judge model are loaded from the correct location. These three paths can also be the same if someone does not have multiple models ready.
- Choose to run on the `harmful_behaviors.csv` or `positive_behaviors.csv` dataset by updating line 26 in `llm-attacks/experiments/launch_scripts/run_gcg_individual.sh`.
- Within `attack_manager.py`, comment in or out the code-blocks after the "VARIANT 1" or "VARIANT 2" comments to run the desired experiment. For example, Speculative Defending Variant 1 is on line 170, and Spec. Defending Variant 2 is lines 173-181.
- To run the experiments, execute the following inside `experiments` (options: `vicuna`, `llama2`; `behaviors`, and `strings`):
  ```bash
  cd launch_scripts
  bash run_gcg_individual.sh vicuna behaviors
  ```

Note: Loading the models onto device often takes around 10 minutes before tests begin. Accuracy throughput is measured by taking the difference of clock time from directly after loading until the 50th harmful behavior or positive behavior is finished testing. 

## Attribution

The original repository that generated adversarial inputs, before the addition of the defense techniques and new Positive Behaviors Dataset, is from [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043)" by [Andy Zou](https://andyzoujm.github.io/), [Zifan Wang](https://sites.google.com/west.cmu.edu/zifan-wang/home), [J. Zico Kolter](https://zicokolter.com/), and [Matt Fredrikson](https://www.cs.cmu.edu/~mfredrik/). The original code is protected by the MIT license, and the license file has not been modified. 


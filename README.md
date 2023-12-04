# Speculative Defense

Implementation of Speculative Defense for HT Kung's CS 242.

## Attribution

The original code, before the addition of the defense techniques and new Positive Behaviors Dataset, was from [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043)" by [Andy Zou](https://andyzoujm.github.io/), [Zifan Wang](https://sites.google.com/west.cmu.edu/zifan-wang/home), [J. Zico Kolter](https://zicokolter.com/), and [Matt Fredrikson](https://www.cs.cmu.edu/~mfredrik/). The original code is protected by the MIT license, and the license file has not been modified. 

## Experiments 

- To run individual experiments with harmful behaviors and/or strings, run the following inside `experiments` (options: `vicuna`, `llama2`; `behaviors`, and `strings`):

```bash
cd launch_scripts
bash run_gcg_individual.sh vicuna behaviors
```


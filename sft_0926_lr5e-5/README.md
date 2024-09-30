---
base_model: /root/epfs/qwen/Qwen2.5-32B-Instruct
library_name: peft
license: other
tags:
- llama-factory
- lora
- generated_from_trainer
model-index:
- name: sft_0926_lr5e-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sft_0926_lr5e-5

This model is a fine-tuned version of [/root/epfs/qwen/Qwen2.5-32B-Instruct](https://huggingface.co//root/epfs/qwen/Qwen2.5-32B-Instruct) on the soulchat_best dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8227

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 2
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 2.0

### Training results



### Framework versions

- PEFT 0.12.0
- Transformers 4.43.4
- Pytorch 2.1.2
- Datasets 2.18.0
- Tokenizers 0.19.1
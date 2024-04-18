# SEACrowd experiments

Experiment repo for datasets in SEA languages, SEA regions, or SEA cultures.

## How to start

Want to add a new eval script following NLU? For example, NLG and VL.

**0. Create a new branch and don't forget to `pip install -r requirements.txt`.**

**1. Add the subset names to `NLG_TASK_LIST` / `VL_TASK_LIST` in [evaluation/data_utils.py](https://github.com/SEACrowd/seacrowd-experiments/blob/main/evaluation/data_utils.py).**

For `NLG_TASK_LIST`, I've already put the subsets to be included, but most of them are still commented. You can take a look at the [`holy/pypi` branch at the `seacrowd-datahub` repo](https://github.com/SEACrowd/seacrowd-datahub/tree/holy/pypi) to see which subsets are available and uncomment those ones.

For `VL_TASK_LIST`, you can get the subset list from [here](https://docs.google.com/spreadsheets/d/1CEk8HTHDAEvr32uTNsgGPaKW6K31aDGhPsAVwaJGxvg/edit?usp=sharing).

**2. Implement `load_vl_datasets()`  in [evaluation/data_utils.py](https://github.com/SEACrowd/seacrowd-experiments/blob/main/evaluation/data_utils.py).**

For VL, you can take a look at the existing `load_nlu_datasets()` and implement `load_vl_datasets()` for the VL tasks. We expect it to return a dict of subset names (key) and a tuple of dataset and task (value).

For NLG, you can skip this step since we already have `load_nlg_datasets()`.

**3. Add the prompt templates for the NLG and VL tasks in [evaluation/prompt_utils.py](https://github.com/SEACrowd/seacrowd-experiments/blob/main/evaluation/prompt_utils.py).**

Originally, we use 5 prompt templates per task for NLU, but I think 3 should be sufficient for NLG and VL.

We use this format `[UPPERCASE_NAME]` (except `LABEL_CHOICE`) to be replaced with something from the specific data instance from the dataset in `to_prompt(...)` in [evaluation/main_nlg_prompt_batch.py](https://github.com/SEACrowd/seacrowd-experiments/blob/main/evaluation/main_nlg_prompt_batch.py) and evaluation/main_vl_prompt_batch.py (has to be created).
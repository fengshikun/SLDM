# Straight-Line Diffusion Model for Efficient 3D Molecular Generation

This is the official implementation of the paper **Straight-Line Diffusion Model for Efficient 3D Molecular Generation
**

---

## Download

### Pretrained Models

#### Download
- **Link:** [Baidu Netdisk](https://pan.baidu.com/s/14GnrxCEmJh6TDv4X9ChitQ)  
- **Extract Code:** **drys**  

#### Unconditional Generation Models
- **atom_type_pred_k8_str_schedule_sigma_min_0.05**: Model for QM9  
- **geom_drugs_k3_str_schedule_sigma_min_0.05**: Model for GEOM-Drugs  

#### Conditional Generation Models  

**Classifiers:**  
- `exp_class_alpha`  
- `exp_class_cv`  
- `exp_class_gap`  
- `exp_class_homo`  
- `exp_class_lumo`  

**Generators:**  
- `exp_cond_alpha_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume`  
- `exp_cond_Cv_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume`  
- `exp_cond_gap_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume`  
- `exp_cond_homo_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume`  
- `exp_cond_lumo_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume`  


### Training Data (TODO)

You can refer to the **EDM repo** for training data, or wait for us to update the processed dataset.

---

## Training and Testing

### QM9

Training

```
CUDA_VISIBLE_DEVICES=0 python -u  main_qm9.py --n_epochs 3000 --exp_name atom_type_pred_k8_str_schedule_sigma_min_0.05 --n_stability_samples 1000 --diffusion_noise_schedule polynomial_2 --diffusion_noise_precision 1e-5 --diffusion_steps 1000 --diffusion_loss_type l2 --batch_size 64 --nf 256 --n_layers 9 --lr 1e-4 --normalize_factors [1,4,10] --test_epochs 20 --ema_decay 0.9999 --property_pred 0 --prediction_threshold_t 10 --model DGAP --sep_noisy_node 1  --str_schedule 1 --atom_type_pred 1 --branch_layers_num 8 --use_prop_pred 0 --sigma_min 0.05  > atom_type_pred_k8_str_schedule_sigma_min_0.05.log 2>&1 &
```

Testing

```
CUDA_VISIBLE_DEVICES=0 python -u eval_analyze.py --model_path /mnt/nfs-ssd/data/fengshikun/str_schedule/e3_diffusion_for_molecules/outputs/geom_drugs_k3_str_schedule_sigma_min_0.05 --n_samples 10_000 --save_to_xyz 0 --checkpoint_epoch 32 --temp_index 0.5 > geom_drugs_k3_str_schedule_sigma_min_0.05_epoch32_temp_index_0.5.log 2>&1 &
```

### GEOM-Drugs

Training

```
CUDA_VISIBLE_DEVICES=0,1,2,3 python  main_geom_drugs.py --n_epochs 3000 --exp_name geom_drugs_k3_str_schedule_sigma_min_0.05 --n_stability_samples 500 --diffusion_noise_schedule polynomial_2 --diffusion_noise_precision 1e-5 --diffusion_steps 1000 --diffusion_loss_type l2 --batch_size 32 --nf 256 --n_layers 4 --lr 1e-4 --normalize_factors [1,4,10] --test_epochs 1 --ema_decay 0.9999 --prediction_threshold_t 10 --model DGAP --sep_noisy_node 1 --str_schedule 1  --use_prop_pred 0 --sigma_min 0.05   --atom_type_pred 1 --branch_layers_num 3 --normalization_factor 1 > geom_drugs_k3_str_schedule_sigma_min_0.05.log 2>&1 &
```

Testing

```
CUDA_VISIBLE_DEVICES=0 python -u eval_analyze.py --model_path /mnt/nfs-ssd/data/fengshikun/str_schedule/e3_diffusion_for_molecules/outputs/geom_drugs_k3_str_schedule_sigma_min_0.05 --n_samples 10_000 --save_to_xyz 0 --checkpoint_epoch 32 --temp_index 0.5 --sample_steps 50 > geom_drugs_k3_str_schedule_sigma_min_0.05_epoch32_steps50_temp_index_0.5.log 2>&1 &

```
### Conditional generation on QM9


Training (lumo as example)

```
CUDA_VISIBLE_DEVICES=0 python -u main_qm9.py --exp_name exp_cond_lumo_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume --model egnn_dynamics --lr 1e-4 --nf 192 --n_layers 9 --save_model True --diffusion_steps 1000 --sin_embedding False --n_epochs 3000 --n_stability_samples 500 --diffusion_noise_schedule polynomial_2 --diffusion_noise_precision 1e-5 --dequantization deterministic --include_charges False --diffusion_loss_type l2 --batch_size 64 --normalize_factors [1,8,1] --conditioning lumo --dataset qm9_second_half --property_pred 0 --prediction_threshold_t 10 --model DGAP --sep_noisy_node 1 --str_schedule 1 --atom_type_pred 1 --branch_layers_num 8 --use_prop_pred 0 --sigma_min 0.1 > exp_cond_lumo_atom_type_pred_k8_str_schedule_sigma_min_0.1.log 2>&1 &
```


Testing (lumo as example)

```
CUDA_VISIBLE_DEVICES=7 python -u eval_conditional_qm9.py --generators_path /mnt/nfs-ssd/data/fengshikun/str_schedule/e3_diffusion_for_molecules/outputs/exp_cond_homo_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume --classifiers_path /mnt/nfs-ssd/data/luyan/e3_diffusion_for_molecules-bfn_schedule/qm9/property_prediction/outputs/exp_class_homo  --property homo --iterations 100 --batch_size 100 --task edm --test_epoch 2990 --temp_index 3 --sample_steps 50  > exp_cond_homo_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume_cond_test_temp_index3_sample_steps_50.log 2>&1
```


The codebase is modified based on EDM: [e3_diffusion_for_molecules](https://github.com/ehoogeboom/e3_diffusion_for_molecules).




### Cite  
If you find our work or code useful, please consider citing our paper:  

```bibtex
@article{ni2025straight,
  title={Straight-Line Diffusion Model for Efficient 3D Molecular Generation},
  author={Ni, Yuyan and Feng, Shikun and Chi, Haohan and Zheng, Bowen and Gao, Huan-ang and Ma, Wei-Ying and Ma, Zhi-Ming and Lan, Yanyan},
  journal={arXiv preprint arXiv:2503.02918},
  year={2025}
}
```
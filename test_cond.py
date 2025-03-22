import os


test_dirs = [
    ['/mnt/nfs-ssd/data/fengshikun/str_schedule/e3_diffusion_for_molecules/outputs/exp_cond_lumo_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume', 
     'lumo', '2990'],
    [
        '/mnt/nfs-ssd/data/fengshikun/str_schedule/e3_diffusion_for_molecules/outputs/exp_cond_homo_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume',
        'homo', '2990'
    ]
]


test_dirs = [
    ['/mnt/nfs-ssd/data/fengshikun/str_schedule/e3_diffusion_for_molecules/outputs/exp_cond_gap_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume', 'gap', '2990'],
    ['/mnt/nfs-ssd/data/fengshikun/str_schedule/e3_diffusion_for_molecules/outputs/exp_cond_alpha_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume', 'alpha', '2990']
]


test_dirs = [
    ['/mnt/nfs-ssd/data/fengshikun/str_schedule/e3_diffusion_for_molecules/outputs/exp_cond_Cv_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume', 'Cv', '2990'],
]

test_dirs = [
    ['/mnt/nfs-ssd/data/fengshikun/str_schedule/e3_diffusion_for_molecules/outputs/exp_cond_mu_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume', 'mu', '2990'],
]


test_dirs = [
    ['/mnt/nfs-ssd/data/fengshikun/str_schedule/e3_diffusion_for_molecules/outputs/exp_cond_lumo_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume', 
     'lumo', '2990'],
    [
        '/mnt/nfs-ssd/data/fengshikun/str_schedule/e3_diffusion_for_molecules/outputs/exp_cond_homo_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume',
        'homo', '2990'
    ],
    ['/mnt/nfs-ssd/data/fengshikun/str_schedule/e3_diffusion_for_molecules/outputs/exp_cond_gap_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume', 'gap', '2990'],
    ['/mnt/nfs-ssd/data/fengshikun/str_schedule/e3_diffusion_for_molecules/outputs/exp_cond_alpha_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume', 'alpha', '2990'],
    ['/mnt/nfs-ssd/data/fengshikun/str_schedule/e3_diffusion_for_molecules/outputs/exp_cond_Cv_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume', 'Cv', '2990'],
    
]

test_dirs = [
    [
        '/mnt/nfs-ssd/data/fengshikun/str_schedule/e3_diffusion_for_molecules/outputs/exp_cond_homo_atom_type_pred_k8_str_schedule_sigma_min_0.1_resume_resume',
        'homo', '2990'
    ],
]

classifier_dict = {
    'lumo': '/mnt/nfs-ssd/data/fengshikun/Data09/SKData/e3_diffusion_for_molecules/outputs/exp_class_lumo',
    'homo': '/mnt/nfs-ssd/data/luyan/e3_diffusion_for_molecules-bfn_schedule/qm9/property_prediction/outputs/exp_class_homo',
    'gap': '/mnt/nfs-ssd/data/luyan/e3_diffusion_for_molecules-bfn_schedule/qm9/property_prediction/outputs/exp_class_gap',
    'alpha': '/mnt/nfs-ssd/data/luyan/e3_diffusion_for_molecules-bfn_schedule/qm9/property_prediction/outputs/exp_class_alpha',
    'Cv': '/mnt/nfs-ssd/data/luyan/e3_diffusion_for_molecules-bfn_schedule/qm9/property_prediction/outputs/exp_class_cv',
    'mu': '/mnt/nfs-ssd/data/luyan/e3_diffusion_for_molecules-bfn_schedule/qm9/property_prediction/outputs/exp_class_mu',
}

test_cmd = 'CUDA_VISIBLE_DEVICES=2 python -u eval_conditional_qm9.py --generators_path {} --classifiers_path {}  --property {} --iterations 100 --batch_size 100 --task edm --test_epoch {}   > {}_cond_test.log 2>&1 &'


test_cmd2 = 'CUDA_VISIBLE_DEVICES=3 python -u eval_conditional_qm9.py --generators_path {} --classifiers_path {}  --property {} --iterations 100 --batch_size 100 --task edm --test_epoch {} --temp_index 3   > {}_cond_test_temp_index3.log 2>&1 &'


test_cmd3 = 'CUDA_VISIBLE_DEVICES=5 python -u eval_conditional_qm9.py --generators_path {} --classifiers_path {}  --property {} --iterations 100 --batch_size 100 --task edm --test_epoch {} --temp_index 2   > {}_cond_test_temp_index2.log 2>&1 &'

test_cmd4 = 'CUDA_VISIBLE_DEVICES=4 python -u eval_conditional_qm9.py --generators_path {} --classifiers_path {}  --property {} --iterations 100 --batch_size 100 --task edm --test_epoch {} --temp_index 1   > {}_cond_test_temp_index1.log 2>&1 &'

test_cmd5 = 'CUDA_VISIBLE_DEVICES=5 python -u eval_conditional_qm9.py --generators_path {} --classifiers_path {}  --property {} --iterations 100 --batch_size 100 --task edm --test_epoch {} --temp_index 0.3   > {}_cond_test_temp_index0.3.log 2>&1 &'

test_cmd6 = 'CUDA_VISIBLE_DEVICES=7 python -u eval_conditional_qm9.py --generators_path {} --classifiers_path {}  --property {} --iterations 100 --batch_size 100 --task edm --test_epoch {} --temp_index 3 --sample_steps {}  > {}_cond_test_temp_index3_sample_steps_{}.log 2>&1'


for test_dir in test_dirs:
    cla_path = classifier_dict[test_dir[1]]
    task_name = os.path.basename(test_dir[0])
    # exe_cmd = test_cmd.format(test_dir[0], cla_path, test_dir[1], test_dir[2], task_name)
    # exe_cmd2 = test_cmd2.format(test_dir[0], cla_path, test_dir[1], test_dir[2], task_name)
    # print(exe_cmd)
    # os.system(exe_cmd)
    # print(exe_cmd2)
    # os.system(exe_cmd2)
    
    # sample_steps = [500, 200, 100, 50]
    # for step in sample_steps:
    #     exe_cmd = test_cmd6.format(test_dir[0], cla_path, test_dir[1], test_dir[2], step, task_name, step)
    #     print(exe_cmd)
    #     os.system(exe_cmd)
    
    
    sample_steps = [500]
    for step in sample_steps:
        for i in range(10):
            exe_cmd = test_cmd6.format(test_dir[0], cla_path, test_dir[1], test_dir[2], step, task_name, f'{step}_{i}')
            print(exe_cmd)
            os.system(exe_cmd)
    
    # for test_cmd in [test_cmd3, test_cmd4, test_cmd5]:
    #     exe_cmd = test_cmd.format(test_dir[0], cla_path, test_dir[1], test_dir[2], task_name)
    #     print(exe_cmd)
    #     os.system(exe_cmd)
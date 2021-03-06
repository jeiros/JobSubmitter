=======================
Example JSON input file
=======================

Here's an input file to get you started:

.. code:: json

    {
        "scheduler": "pbs",
        "HPC_job": "True",
        "pbs_settings": {
            "walltime": "72:0:0",
            "nnodes": 1,
            "ncpus": 1,
            "ngpus": 1,
            "mem":"1000mb",
            "host":"cx1-51-6-1",
            "queue":"gpgpu",
            "gpu_type":"K80"
        },
        "simulation_details": {
            "system_name": "protein1",
            "inpcrd_file": "protein1.inpcrd",
            "topology_file": "protein1.prmtop",
            "start_rst": "Heated_eq.rst",
            "input_file": "Production_cmds.in",
            "start_time": 0,
            "final_time": 500,
            "job_length": 50,
            "job_directory": "/work/username/protein1",
            "cuda_version": "7.5.18",
            "binary_location": "/path/to/AMBERHOME/bin/pmemd.cuda_SPFP",
            "pre_simulation_cmd": [
                "/path/to/AMBERHOME/bin/pmemd.cuda_SPFP -O -i premin.in -o premin.out -c ${inpcrd} -p ${prmtop} -r premin.rst -ref ${inpcrd}",
                "/path/to/AMBERHOME/bin/pmemd.cuda_SPFP -O -i sandermin1.in -o sandermin1.out -c premin.rst -p ${prmtop} -r sandermin1.rst",
                "/path/to/AMBERHOME/bin/pmemd.cuda_SPFP -O -i 02_Heat.in -o 02_Heat.out -c sandermin1.rst -p ${prmtop} -r 02_Heat.rst -ref sandermin1.rst -x 02_Heat.nc",
                "/path/to/AMBERHOME/bin/pmemd.cuda_SPFP -O -i 03_Heat2.in -o 03_Heat2.out -c 02_Heat.rst -p ${prmtop} -r Heated_eq.rst -ref 02_Heat.rst -x 03_Heat2.nc"
            ],
            "pre_simulation_type": "gpu"
        },
        "local_machine": {
            "user": "username",
            "hostname": "hostname",
            "destination" : "/Users/username/protein1"
        },
        "master_node": {
            "user_m": "username",
            "hostname_m": "master_node-hostname",
            "job_directory_m": "/home/username/protein1"
        }
    }

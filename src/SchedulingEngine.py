class SchedulingEngine:
    def __init__(self, json):
        self.pbs_headers = ""

        # PBS settings
        self.queue_type = json['pbs_settings']['queue']
        self.walltime = json['pbs_settings']['walltime']
        self.mail = json['pbs_settings']['email']
        self.nnodes = json['pbs_settings']['nnodes']
        self.ncpus = json['pbs_settings']['ncpus']
        self.ngpus = json['pbs_settings']['ngpus']
        self.memory = json['pbs_settings']['mem']
        self.gpu_type = json['pbs_settings']['gpu_type']
        self.host = json['pbs_settings']['host']

        # Simulation details
        self.system_name = json['simulation_details']['system_name']
        self.inpcrd_file = json['simulation_details']['inpcrd_file']
        self.topology_file = json['simulation_details']['topology_file']
        self.start_time = json['simulation_details']['start_time']
        self.final_time = json['simulation_details']['final_time']
        self.job_length = json['simulation_details']['job_length']
        self.job_directory = json['simulation_details']['job_directory']
        self.start_rst = json['simulation_details']['start_rst']
        self.pre_simulation_cmd = json['simulation_details']['pre_simulation_cmd']

        # Local machine details
        self.user = json['local_machine']['user']
        self.hostname = json['local_machine']['hostname']
        self.destination = json['local_machine']['destination']

class PBSEngine(SchedulingEngine):
    def __init__(self):
        pass

    def generate_headers(self):
        self.pbs_headers = "#PBS -lselect=%s:" % self.nnodes
        self.pbs_headers += "ncpus=%s:" % self.ncpus
        self.pbs_headers += "ngpus=%s:" % self.ngpus
        self.pbs_headers += "mem=%s:" % self.memory

        if self.queue_type == 'gpgpu':
            self.pbs_headers += "gpu_type=%s\n" % self.gpu_type
        elif self.queue_type == 'pqigould':
            self.pbs_headers += "host=%s\n" % self.host
        else:
            sys.exit("Supported queues are 'pgigould' or 'gpgpu' only.")

        self.pbs_headers += "#PBS -lwalltime=%s\n" % self.walltime
        self.pbs_headers += "#PBS -q %s\n" % self.queue_type
        self.pbs_headers += "#PBS -M %s\n" % self.mail
        self.pbs_headers += "#PBS -m abe\n\n"

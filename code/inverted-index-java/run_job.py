import subprocess


def exec_job(version: str = 'v1', test_dir: str = 'test1'):
    # Run Hadoop job

    jar_localisation = 'code/inverted-index-java/target'

    subprocess.run([
        "hadoop", "jar", f"{jar_localisation}/inverted-index-java-1.0.jar",
        "it.unipi.adrien.koumgang.Main", version,
        f"/user/input/{test_dir}", f"/user/output/java/{version}/{test_dir}",
        "-Dmapreduce.task.profile=true",
        "-Dmapreduce.task.profile.params=-agentlib:hprof=cpu=samples,heap=sites,depth=6"
    ])

    # Copy results
    subprocess.run(["hdfs", "dfs", "-get", f"/user/output/java/{version}/{test_dir}/*", f"./output/java/{version}/{test_dir}"])

    # Fetch profiling data (simplified)
    app_id = subprocess.getoutput("yarn application -list -appStates FINISHED | awk '/Main/ {print $1}' | head -n 1")
    if app_id:
        subprocess.run(f"yarn logs -applicationId {app_id} | grep 'Profiler output' | awk '{{print $NF}}' | xargs -I {{}} cp {{}}/*.hprof ./hadoop-profiler/java/{version}/{test_dir}", shell=True)



if __name__ == '__main__':
    version_list = ['v1', 'v2']

    test_dir_list = ['test1', 'test2']

    for v in version_list:
        for t_d in test_dir_list:
            exec_job(version=v, test_dir=t_d)


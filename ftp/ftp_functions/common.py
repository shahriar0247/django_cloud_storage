import subprocess


def shell(cmd):
    hi = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    output = hi.stderr.read().decode("utf-8")
    output = output + hi.stdout.read().decode("utf-8")
    return output
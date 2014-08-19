
import subprocess

def d_call():
    #subprocess.Popen('echo "helloworld"')
    subprocess.call(['sleep','3'])
    subprocess.call(['echo', '"helloworld"'])
    subprocess.call(['echo', '"helloworld2"'])
    subprocess.call(['echo', '"helloworld3"'])
    subprocess.call(['echo', '"helloworld4"'])

    # execute in order.

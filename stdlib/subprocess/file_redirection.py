import subprocess

if __name == '__main__':
    main()
def main():
    with open('out.txt', 'w+') as f:
        cmd = ['/bin/ls', '/']
        p = subprocess.Popen(cmd, stdout=f)
        p.communicate()

        # Read from the file
        f.seek(0)
        for line in f:
            print(line.strip())

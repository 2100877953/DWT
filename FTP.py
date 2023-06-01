import os
import paramiko

class SSHConnection(object):

    def __init__(self, host, port, username, pwd):
        self.host = host
        self.port = port

        self.username = username
        self.pwd = pwd
        self.__k = None

    def connect(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.pwd)
        self.__transport = transport

    def close(self):
        self.__transport.close()

    def upload(self, local_path, target_path):
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        sftp.put(local_path, target_path)

    def download(self, remote_path, local_path):
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        sftp.get(remote_path, local_path)

    def cmd(self, command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        result = stdout.read()
        print(str(result, encoding='utf-8'))
        return result


if __name__ == '__main__':

    ssh = SSHConnection(host='10.16.93.138', port=22, username='comm', pwd='sustecheee2022')
    ssh.connect()
    local_path = './Data/'
    if not os.path.exists('./Data/'):
        ssh.cmd('mkdir -p ./Data/')
    # ssh.cmd('mkdir -p /home/target/')
    target_path = '/home/comm/desktop/huzeyang/wka/Data/'
    for filename in os.listdir(local_path):
        print(filename)
        ssh.upload(local_path + filename, target_path + filename)
    ssh.close()
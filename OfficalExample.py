import os
import re
import subprocess
import shutil

# 切换到当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

# 执行命令
def runCommand(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

# 写到一半突然意识到，直接放foundry项目即可，不用这么麻烦来着，但是写都写了，当一个单独部署官方的Example脚本吧
def deployContracts(private):
    # 初始化Foundry项目
    if os.path.exists('foundry-move-evm') and os.path.isdir('foundry-move-evm'):
        #os.rmdir('foundry-move-evm')
        shutil.rmtree('foundry-move-evm', ignore_errors=True)
        print("[x] 目录 foundry-move-evm 存在，删除处理..")
    try:
        command1 = 'mkdir foundry-move-evm'
        cmd1_log = runCommand(command1) 
        os.chdir(current_dir+'/foundry-move-evm')
        command2 = 'forge init --no-git'
        cmd2_log = runCommand(command2)
    except Exception  as e:
        print("[x] 初始化项目失败！错误信息{}".format(e))

    # 复制Solidity代码到文件夹
    try:
        os.chdir(current_dir)
        script_dir = current_dir + '/foundry-move-evm/'+'script'
        src_dir = current_dir + '/foundry-move-evm/'+'src'
        for filename in os.listdir(current_dir+'/SOLIDITY/01-MovementExample'):
            if '.s.' in filename:
                src_file = os.path.join(current_dir+'/SOLIDITY/01-MovementExample', filename)
                # 复制到目标目录中
                shutil.copy(src_file, script_dir)
                print(f"[√] 复制代码 {filename} 到 {script_dir}")
            elif '.s.' not in filename and '.sol' in filename:
                src_file = os.path.join(current_dir+'/SOLIDITY/01-MovementExample', filename)
                # 复制到目标目录中
                shutil.copy(src_file, src_dir)
                print(f"[√] 复制代码 {filename} 到 {src_dir}")
        # 创建私钥文件
        with open(current_dir + '/foundry-move-evm/.env', 'w') as f:
            f.write(f"PRIVATE_KEY={private}\n")
        print(f"[√] .env 文件已创建并写入私钥信息")
    except Exception  as e:
        print("[x] 尝试复制Solidity源码失败！错误信息{}".format(e))

    # 部署合约
    try:
        os.chdir(current_dir+"/foundry-move-evm/")
        command3 = 'forge script CounterScript --broadcast --chain-id 336 --rpc-url https://mevm.devnet.m1.movementlabs.xyz/v1 --legacy'
        cmd3_log = runCommand(command3)
        print(cmd3_log)
        contract_address = re.search(r'Contract Address: (.+)',cmd3_log).group(1)
        print(f'[√] 合约部署成功，地址为{contract_address}')

        # 修改脚本合约内容        
        with open(current_dir+"/foundry-move-evm/script/Interact.s.sol", 'r') as file:
            file_content = file.read()
        file_content = file_content.replace("0x000000000", contract_address)
        with open(current_dir+"/foundry-move-evm/script/Interact.s.sol", 'w') as file:
            file.write(file_content)

        # 合约交互
        command4 = 'forge script InteractScript --broadcast --chain-id 336 --rpc-url https://mevm.devnet.m1.movementlabs.xyz'
        cmd4_log = runCommand(command4)
        print('[√] 合约交互成功！')
        print(cmd4_log)
    except Exception as e:
        print(f'[x] 错误{e}')


if __name__ == '__main__':
    with open('seeds.txt') as f:
        file = f.readlines()
    PRIVATE_KEY = []
    for x in file:
        line = x.rstrip()
        PRIVATE_KEY.append(line.split(':')[1])
    
    for p in PRIVATE_KEY:
        deployContracts(p)
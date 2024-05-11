import os
import random
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

# ERC20代币
def deployErc20(private):
    curr_dir = current_dir + '/SOLIDITY/02/'
    print(f'[-] 尝试部署ERC20合约...')
    # 创建私钥文件
    with open(curr_dir+'.env', 'w') as f:
        f.write(f"PRIVATE_KEY={private}\n")
    print(f"[√] .env 文件已创建并写入私钥信息")

    # 部署合约
    try:
        os.chdir(curr_dir)
        command1 = 'forge script CounterScript --broadcast --chain-id 336 --rpc-url https://mevm.devnet.m1.movementlabs.xyz/v1 --legacy'
        cmd1_log = runCommand(command1) 
        print(cmd1_log)
        print(f'[√] ERC20 部署成功！')
    except Exception as e:
        print(f'[x] 部署失败！ {e}')

# Faucet
def deployFaucet(private):
    curr_dir = current_dir + '/SOLIDITY/03/'
    print(f'[-] 尝试部署Faucet合约...')
    # 创建私钥文件
    with open(curr_dir + '.env', 'w') as f:
        f.write(f"PRIVATE_KEY={private}\n")
    print(f"[√] .env 文件已创建并写入私钥信息")

    # 部署合约
    try:
        os.chdir(curr_dir)
        command1 = 'forge script CounterScript --broadcast --chain-id 336 --rpc-url https://mevm.devnet.m1.movementlabs.xyz/v1 --legacy'
        cmd1_log = runCommand(command1) 
        print(cmd1_log)
        print(f'[√] Faucet 部署成功！')
    except Exception as e:
        print(f'[x] 部署失败！ {e}')

# Airdrop
def deployAirdrop(private):
    curr_dir = current_dir + '/SOLIDITY/04/'
    print(f'[-] 尝试部署Airdrop合约...')
    # 创建私钥文件
    with open(curr_dir + '.env', 'w') as f:
        f.write(f"PRIVATE_KEY={private}\n")
    print(f"[√] .env 文件已创建并写入私钥信息")

    # 部署合约
    try:
        os.chdir(curr_dir)
        command1 = 'forge script CounterScript --broadcast --chain-id 336 --rpc-url https://mevm.devnet.m1.movementlabs.xyz/v1 --legacy'
        cmd1_log = runCommand(command1) 
        print(cmd1_log)
        print(f'[√] Airdrop 部署成功！')
    except Exception as e:
        print(f'[x] 部署失败！ {e}')

# ERC721
def deployERC721(private):
    curr_dir = current_dir + '/SOLIDITY/05/'
    print(f'[-] 尝试部署ERC721合约...')
    # 创建私钥文件
    with open(curr_dir + '.env', 'w') as f:
        f.write(f"PRIVATE_KEY={private}\n")
    print(f"[√] .env 文件已创建并写入私钥信息")

    # 部署合约
    try:
        os.chdir(curr_dir)
        command1 = 'forge script CounterScript --broadcast --chain-id 336 --rpc-url https://mevm.devnet.m1.movementlabs.xyz/v1 --legacy'
        cmd1_log = runCommand(command1) 
        print(cmd1_log)
        print(f'[√] ERC721 部署成功！')
    except Exception as e:
        print(f'[x] 部署失败！ {e}')

# MerkleTree
def deployMerkleTree(private):
    curr_dir = current_dir + '/SOLIDITY/06/'
    print(f'[-] 尝试部署MerkleTree合约...')
    # 创建私钥文件
    with open(curr_dir + '.env', 'w') as f:
        f.write(f"PRIVATE_KEY={private}\n")
    print(f"[√] .env 文件已创建并写入私钥信息")

    # 部署合约
    try:
        os.chdir(curr_dir)
        command1 = 'forge script CounterScript --broadcast --chain-id 336 --rpc-url https://mevm.devnet.m1.movementlabs.xyz/v1 --legacy'
        cmd1_log = runCommand(command1) 
        print(cmd1_log)
        print(f'[√] MerkleTree 部署成功！')
    except Exception as e:
        print(f'[x] 部署失败！ {e}')

# Signature
def deploySignature(private):
    curr_dir = current_dir + '/SOLIDITY/07/'
    print(f'[-] 尝试部署Signature合约...')
    # 创建私钥文件
    with open(curr_dir + '.env', 'w') as f:
        f.write(f"PRIVATE_KEY={private}\n")
    print(f"[√] .env 文件已创建并写入私钥信息")

    # 部署合约
    try:
        os.chdir(curr_dir)
        command1 = 'forge script CounterScript --broadcast --chain-id 336 --rpc-url https://mevm.devnet.m1.movementlabs.xyz/v1 --legacy'
        cmd1_log = runCommand(command1) 
        print(cmd1_log)
        print(f'[√] Signature 部署成功！')
    except Exception as e:
        print(f'[x] 部署失败！ {e}')

# NFTSwap
def deployNFTSwap(private):
    curr_dir = current_dir + '/SOLIDITY/08/'
    print(f'[-] 尝试部署NFTSwap合约...')
    # 创建私钥文件
    with open(curr_dir + '.env', 'w') as f:
        f.write(f"PRIVATE_KEY={private}\n")
    print(f"[√] .env 文件已创建并写入私钥信息")

    # 部署合约
    try:
        os.chdir(curr_dir)
        command1 = 'forge script CounterScript --broadcast --chain-id 336 --rpc-url https://mevm.devnet.m1.movementlabs.xyz/v1 --legacy'
        cmd1_log = runCommand(command1) 
        print(cmd1_log)
        print(f'[√] NFTSwap 部署成功！')
    except Exception as e:
        print(f'[x] 部署失败！ {e}')

# ERC1155
def deployERC1155(private):
    curr_dir = current_dir + '/SOLIDITY/09/'
    print(f'[-] 尝试部署ERC1155合约...')
    # 创建私钥文件
    with open(curr_dir + '.env', 'w') as f:
        f.write(f"PRIVATE_KEY={private}\n")
    print(f"[√] .env 文件已创建并写入私钥信息")

    # 部署合约
    try:
        os.chdir(curr_dir)
        command1 = 'forge script CounterScript --broadcast --chain-id 336 --rpc-url https://mevm.devnet.m1.movementlabs.xyz/v1 --legacy'
        cmd1_log = runCommand(command1) 
        print(cmd1_log)
        print(f'[√] ERC1155 部署成功！')
    except Exception as e:
        print(f'[x] 部署失败！ {e}')

# TokenVesting
def deployTokenVesting(private):
    curr_dir = current_dir + '/SOLIDITY/10/'
    print(f'[-] 尝试部署TokenVesting合约...')
    # 创建私钥文件
    with open(curr_dir + '.env', 'w') as f:
        f.write(f"PRIVATE_KEY={private}\n")
    print(f"[√] .env 文件已创建并写入私钥信息")

    # 部署合约
    try:
        os.chdir(curr_dir)
        command1 = 'forge script CounterScript --broadcast --chain-id 336 --rpc-url https://mevm.devnet.m1.movementlabs.xyz/v1 --legacy'
        cmd1_log = runCommand(command1) 
        print(cmd1_log)
        print(f'[√] TokenVesting 部署成功！')
    except Exception as e:
        print(f'[x] 部署失败！ {e}')


if __name__ == '__main__':
    funcs = [deployErc20, deployFaucet ,deployAirdrop,deployERC721,deployMerkleTree,deploySignature,deployNFTSwap,deployERC1155,deployTokenVesting]
    
    with open('seeds.txt') as f:
        file = f.readlines()
    PRIVATE_KEY = []
    for x in file:
        line = x.rstrip()
        PRIVATE_KEY.append(line.split(':')[1])
    
    for p in PRIVATE_KEY:
        random.choice(funcs)(p)
        #deployErc20(p)
        #deployFaucet(p)
        #deployAirdrop(p)
        #deployMerkleTree(p)
        #deploySignature(p)
        #deployNFTSwap(p)
        #deployERC1155(p)
        #deployTokenVesting(p)
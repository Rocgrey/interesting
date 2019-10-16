### 1、首先在自己电脑上安装git并产生本机秘钥
> ssh-keygen -t rsa -C "xxx@xx.com"
```
Generating public/private rsa key pair.
Enter file in which to save the key (xxxxxx): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in xxxxxx.
Your public key has been saved in xxxxxx.
The key fingerprint is:
SHA256:xxxxxxxx xxx@xxx.com
The key's randomart image is:
+---[RSA 2048]----+
|                 |
|           . .   |
|          . o . o|
|         o .   +.|
|      . S =     =|
|       + % +   + |
| +. . ooB = o .  |
|o+* .*o..* . .   |
|.E*B=o+oo..      |
+----[SHA256]-----+
```
### 2、找到秘钥的位置，将密钥的内容复制下来
### 3、登录github>setting>add ssh key,将复制的Your public key 秘钥复制进去
### 4、在个人电脑上开始脸接github,
> ssh -T  git@github.com
### 出现如下表示连接成功：
```
Warning: Permanently added the RSA host key for IP address 'xxx.xxx.xxx.xxx' to the list of known hosts.
Hi xxx! You've successfully authenticated, but GitHub does not provide shell access.
```
### 5、配置账户，邮箱
> git config --global user.name "用户名"
> git config --global user.email "邮箱"
### 6、最后就可以
```
git clone xxx.git
git add XXX.txt
git commit -m "***"
git push 
```

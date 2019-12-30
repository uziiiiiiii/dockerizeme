- 安装VirtualBox 6.0.14（非最新版，目前Vagrant暂不支持6.1.x）
- 安装Vagrant 2.2.6 (最新版)

- 开启VT-x/AMD-V 硬件加速，在BIOS中进行设置
[https://jingyan.baidu.com/article/09ea3ede7a9dd7c0aede39fb.html](https://jingyan.baidu.com/article/09ea3ede7a9dd7c0aede39fb.html)

- 设置 —— 查找“启用或关闭Windows功能”：
	
	- 禁用 Hyper-V;
	- 禁用 Windows沙盒;
	- 启用 虚拟机平台;

- 令需启用 windows hypervisor platform, 但其一般不会在上述设置中显示，按下述操作：（引用自[https://blog.csdn.net/oldfish__/article/details/88641864](https://blog.csdn.net/oldfish__/article/details/88641864)）
	
	1. 创建.cmd文件，输入以下内容：

		pushd "%~dp0"

		dir /b %SystemRoot%\servicing\Packages*HypervisorPlatform*.mum >hypervisorplatform.txt

		for /f %%i in ('findstr /i . hypervisorplatform.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages%%i"

		del hypervisorplatform.txt

		Dism /online /enable-feature /featurename:HypervisorPlatform /LimitAccess /ALL

		pause

	2. 以管理员身份运行该.cmd文件。

- 重新启动以更新上述配置。

- 以管理员身份运行cmd或PowerShell，进入dockerizeme目录, 运行`vagrant up --provider=virtualbox`
	
	再运行`vagrant ssh`进行虚拟机的使用。
	
	使用命令行指令`exit`退出虚拟机，执行`vagrant halt`关闭虚拟机，下次启动时执行`vagrant up`即可。


- Windows系统下文件的换行符为'\r\n'，而ubuntu下的换行符为'\n'，这就导致每一行的末尾多出一个字符'\r'，从而报错。
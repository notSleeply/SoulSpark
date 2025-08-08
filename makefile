# PyScript-DayDayUp Makefile

# 可自定义的配置项
PYTHON = python
PYTHONW = pythonw
PYINSTALLER = pyinstaller
APP_NAME = DayDayUp
APP_FILE = src/main.pyw

# 默认目标
all: build

# 运行主程序
run:
	$(PYTHONW) $(APP_FILE)

# 安装依赖
deps:
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) -m pip install pyinstaller

# 生成可执行文件
build:
	$(PYINSTALLER) --noconsole --onefile --icon=icon.ico --name=$(APP_NAME) $(APP_FILE)

# 生成绿色版可执行文件（包含程序和资源）
build-portable:
	$(PYINSTALLER) --noconsole --onedir --icon=icon.ico --name=$(APP_NAME) $(APP_FILE)
	copy Bible.txt dist\$(APP_NAME)\
	copy icon.ico dist\$(APP_NAME)\

# 清理生成的文件
clean:
	if exist build rmdir /s /q build
	if exist dist rmdir /s /q dist
	if exist $(APP_NAME).spec del $(APP_NAME).spec

# 帮助信息
help:
	@echo 可用的命令:
	@echo   make run          - 运行主程序
	@echo   make deps         - 安装依赖
	@echo   make build        - 生成单文件可执行程序
	@echo   make build-portable - 生成便携版（文件夹）
	@echo   make clean        - 清理构建文件
	@echo   make help         - 显示帮助信息
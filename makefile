# SoulSpark Makefile

# 可自定义的配置项
UV = uv
PYTHON = uv run python
PYTHONW = uv run pythonw
PYINSTALLER = uv run pyinstaller
APP_NAME = SoulSpark
APP_FILE = main.pyw

# 默认目标
all: build

# Python 运行环境
python:
	$(PYTHON) $(APP_FILE)

# 运行主程序
run:
	$(PYTHONW) $(APP_FILE)

# 同步依赖
deps:
	$(UV) sync

# 安装 pyinstaller (如果需要)
install-pyinstaller:
	$(UV) add --dev pyinstaller

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
	-rmdir /s /q build 2>nul
	-rmdir /s /q dist 2>nul
	-cmd /c del $(APP_NAME).spec 2>nul

# 强制重新构建
rebuild: clean
	$(PYINSTALLER) --noconsole --onefile --icon=icon.ico --name=$(APP_NAME)  $(APP_FILE)

# 帮助信息
help:
	@echo 可用的命令:
	@echo   make run          - 运行主程序
	@echo   make deps         - 同步依赖
	@echo   make install-pyinstaller - 安装 pyinstaller
	@echo   make build        - 生成单文件可执行程序
	@echo   make build-portable - 生成便携版（文件夹）
	@echo   make rebuild      - 清理并重新构建
	@echo   make clean        - 清理构建文件
	@echo   make help         - 显示帮助信息
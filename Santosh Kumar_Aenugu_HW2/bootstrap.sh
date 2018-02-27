readonly CIFAR_DIR="cifar-2class-py2"
readonly LOGS_DIR="logs"
readonly JOBS_DIR="jobs"
readonly FIGURES_DIR="figures"
readonly VIRTUALENV_DIR="venv"
readonly REQUIREMENTS_FILE="requirements.txt"

readonly SCRIPT_NAME=$0
usage() {
	echo "usage: $SCRIPT_NAME /path/to/cifar-2class-py2.zip"
	echo ""
	echo "Setting up environment variables:"
	echo -e "\t- Setting up VENV"
	echo -e "\t- Installing dependencies in python"
	echo -e "\t- Extract dataset"
}
if [ "$#" -ne 1 ]; then
	echo "Enter correct no. of arguments."
	usage
	exit 1
fi

readonly DATASET_FILE=$1

reset_environment() {
	rm -rf $CIFAR_DIR
	rm -rf $VIRTUALENV_DIR
}

create_virtualenv() {
	virtualenv --no-site-packages $VIRTUALENV_DIR
}

save_dependencies_list() {
	local $file=$0
	rm -f $file
	pip freeze > $file
}

install_dependencies() {
	pip install argparse
	pip install numpy
	pip install scipy
	pip install ipython
	pip install sklearn
	pip install matplotlib
}

install_dependencies_from_requirements() {
	pip install -r $REQUIREMENTS_FILE
}

setup_dataset() {
	unzip $DATASET_FILE
	rm -rf __MACOSX
}

create_dirs() {
	mkdir -p $LOGS_DIR
	mkdir -p $JOBS_DIR
	mkdir -p $FIGURES_DIR
}

main() {
	reset_environment

	echo
	echo "[${SCRIPT_NAME}]  VENV creating "
	create_virtualenv

	echo
	echo "[${SCRIPT_NAME}] dependencies INSTALL"

	source $VIRTUALENV_DIR/bin/activate
	install_dependencies
	save_dependencies_list $REQUIREMENTS_FILE
	deactivate

	echo
	echo "[${SCRIPT_NAME}] Extracting dataset..."
	setup_dataset
	create_dirs

	echo
	echo "[${SCRIPT_NAME}] Done."
}
main

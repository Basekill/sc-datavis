# Install dependencies
micromamba env create -f environment.yml

# Activate the environment
micromamba activate sc_datavis

# Setup pre-commit and pre-push hooks
pre-commit install -t pre-commit
pre-commit install -t pre-push

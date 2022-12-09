# PIP-NN-PyTorch-Tutorial

A Tutorial of PIP-NN, implemented in PyTorch

## Introduction

This tutorial contains 4 parts, and each part is a seperated jupyter notebook file.

- `01-rawdata-load-and-split.ipynb` how to get train set and valid set
- `02-generate-pip.ipynb` how to generate PIP from the structure of a molecule
- `03-train-pip-nn.ipynb` let's train a network
- `04-evaluate-pip-nn.ipynb` invoke and evaluate trained network

## Auxiliary Codes

- `MZMol.py` tools to process `xyz` files
- `PIP_Dataset.py` dataset class to storage PIP and energy
- `PIP_NN.py` PIP-NN in PyTorch
- `basis_1_1_1_4.f90` Fortran codes to generate PIP

## Usage

First, you need to install packages according to requirements section.

Run

```perl
$ perl build.pl 4 1 1 1
```

to generate a Python module for PIP.

Then you can play with the notebooks.

## Requirements

- `gfortran`
- `perl`
- `pytorch`
- `numpy`
- `pandas`
- `scipy`
- `matplotlib`
- `sklearn`
- `openbabel`

## References

- Zhang L, Zhang S, Owens A, et al. VIB5 database with accurate ab initio quantum chemical molecular potential energy surfaces[J]. Scientific Data, 2022, 9(1): 1-10.
- Nandi A, Qu C, Bowman J M. Using gradients in permutationally invariant polynomial potential fitting: A demonstration for CH4 using as few as 100 configurations[J]. Journal of Chemical Theory and Computation, 2019, 15(5): 2826-2835.

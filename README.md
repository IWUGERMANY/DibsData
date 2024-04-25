# DibsData

This module contains data for simulating buildings. The data contained in this module is used by another module called `dibs_computing_core`
to perform the simulation. Make sure that the `dibs_computing_core` module is installed in your project and configured correctly to
utilize the full functionality of this module.

## Installation
To install the package, use the following command:

```bash
pip install dibs_data
```

To use the full DIBS [model](https://iwugermany.github.io/dibs/overview) it is recomended to install the [DibsCLI](https://github.com/IWUGERMANY/DibsCLI) bundling the DibsComputingCore, [DibsDataSourceCSV](https://github.com/IWUGERMANY/DibsDataSourceCSV) and the [DibsData](https://github.com/IWUGERMANY/DibsData). To install the DIBS Command Line Interface (DibsCLI) use the following command:

```bash
pip install dibs_cli
```


## Usage
To Import the module use the following command:

 ```python
   import dibs_data
   ```
## Further information
For a detailed installation guide and further information on DIBS see the [wiki](https://github.com/IWUGERMANY/DibsCLI/wiki) and the [DIBS Project Page](https://iwugermany.github.io/dibs/).

## How to cite
Please cite the Dynamic ISO Building Simulator (DIBS) as defined [here](https://iwugermany.github.io/dibs/contri).

## Legacy
The current Dynamic ISO Building Simulator (DIBS) is a PyPI package implementation of the initial [DIBS implementation](https://github.com/IWUGERMANY/DIBS---Dynamic-ISO-Building-Simulator) by Julian Bischof, Simon Knoll and Michael Hörner.


## License
This program is licensed under the [MIT License](LICENSE). See the license file for more information.

## Acknowledgement
The Dynamic ISO Building Simulator has been developed in context of the 'ENOB:DataNWG Forschungsdatenbank Nichtwohngebäude' (www.datanwg.de) project and the project 'FlexGeber - Demonstration of flexibility options in the building sector and their integration with the energy system in Germany' at Institut Wohnen und Umwelt (IWU), Darmstadt. The preparation of the publication as a [Python package on Pypi](https://pypi.org/project/dibs-computing-core/) was undertaken within the [EnOB:LezBAU](https://www.lezbau.de/) project, where the DIBS model provides the basis for the calculation of the operational energy within the LezBAU web tool.
<p float="left">
  <img src="https://github.com/IWUGERMANY/DibsComputingCore/blob/main/src/img/IWU_Logo.PNG" width="15%" /> 
</p>  

<b>ENOB:DataNWG<b>
<b>Funding code:</b>  Fkz.: 03ET1315  
<b>Project duration:</b>  01.12.2015 until 31.05.2021

<b>FlexGeber<b>
<b>Funding code:</b>  Fkz.: 03EGB0001  
<b>Project duration:</b>  01.10.2017 until 31.07.2022

<b>ENOB:LezBAU<b>
<b>Funding code:</b>  Fkz.: 03EN1074A
</br><b>Project duration:</b>  01.01.2023 until 31.12.2025
  
<b>All funded by:</b> 
<p float="left">
  <img src="https://github.com/IWUGERMANY/DibsComputingCore/blob/main/src/img/BMWi_Logo.png" width="30%" /> 
</p> 
in accordance with the parliamentary resolution of the German Parliament.

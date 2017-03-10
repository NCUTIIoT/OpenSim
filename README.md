# OpenSim

## Install

```
git clone https://github.com/NCUTIIoT/OpenSim.git
cd OpenSim
git submodule init
git submodule update
```

## Run

```
cdto openwsn-sw\software\openvisualizer

scons runweb --sim --pathTopo=topology_data_2motes.json --markov=markov2.json
```

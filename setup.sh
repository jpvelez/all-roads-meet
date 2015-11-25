if [[ $OSTYPE == 'linux-gnu' ]]; then
   curl https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-2.4.0-Linux-x86_64.sh > anaconda
   bash anaconda
fi
conda create --name all-roads-meet python=2.7
source activate all-roads-meet
if [[ $OSTYPE == 'darwin14' ]]; then
   brew install protobuf # not working
elif [[ $OSTYPE == 'linux-gnu' ]]; then
   sudo aptitude install build-essential python-devel protobuf-compiler libprotobuf-dev
fi
pip install imposm.parser # Needs python 2.7

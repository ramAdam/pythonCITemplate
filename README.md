# PythonCITemplate
Continuous testing template for python projects. See "run.txt" to see, how to run it

 
# run in project directory from command line
python -m unittest discover -v

#running individual module from command line
python -m unittest tests.unit.test_animals

#for continuous testing, type the commmand below in terminal
watch -n 10 ./watcher.sh

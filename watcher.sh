# This is a comment!

#find tests/ -iname "*.py" -not -name "__*.py" 
#python test_runner.py

if md5sum -c checksum.chk; then 
	python test_runner.py	
else
	echo "command Failed"
	python test_runner.py
	find tests/ -iname "*.py" -not -name "__*.py" -exec md5sum {} \; > \
	checksum.chk	
fi

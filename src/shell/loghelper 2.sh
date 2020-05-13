#!/bin/bash
#--------------------------------------------
# author：Joy
# func：for unzip file and find str
# date：12/7 2018
# cd /Users/joybar/Documents/Doc/test
# ./loghelper.sh -help
# eg1： ./loghelper.sh testlog.zip position
#--------------------------------------------

exit_script(){
    exit 1
}

helpCmd(){
   cmd=$1
   deviderLineStart="---------help start---------"
   deviderLineEnd="---------help end---------"
   hlep="-help"
   if [ "$cmd" == "$hlep" ];then
   	echo $deviderLineStart
   	echo "uasge: ./loghelper.sh [args...]"
   	echo "for exsample"
   	echo "./loghelper.sh testlog.zip position "
   	echo "the parameter specification"
	printf "%-30s %-30s \n" firstParams fsecondParams
	printf "%-30s %-30s \n" 'the path of the log.zip file' 'the Filter parameters'
	echo $deviderLineEnd
	exit_script 
	fi
	#echo "this is not help commond"	
}

isZipFile(){
	fileName=$1
	echo "the fileName：$fileName";
	flieSuffix=${fileName##*.}
	echo "the flieSuffix：$flieSuffix";
	zipName="zip"
	if [ "$flieSuffix" != "$zipName" ];then
	echo "this file is not a zip file"
	exit_script 
	fi
	echo "this file is a zip file"	
}

mkdir(){
	fileName=$1
	fliePrefix=${fileName%%.*}
	echo "the fliePrefix：$fliePrefix";
	command mkdir $fliePrefix

}
unzipFile(){
	fileName=$1
	fliePrefix=${fileName%%.*}
	#echo "the fliePrefix：$fliePrefix";
	command unzip -o   $fileName -d $fliePrefix	
	#command gunzip -r  $fileName
}

loopDir(){
	fileName=$1
	fliePrefix=${fileName%%.*}

	echo "the fliePrefix----------：$fliePrefix";
	command cd $fliePrefix
	for file in ./*
	do
	    if test -f $file
	    then
	        echo $file 是文件

	    fi
	    if test -d $file
	    then
	        echo $file 是目录
	        subDir=${file##/*}
	        echo "the subDir----------：$subDir";
	        command cd $subDir
	        command cd ls
	        command ls *.zip | xargs -n1 unzip -o -P infected
	        echo "解压完毕";
	        command rm -f *.zip
	        command ls
	        command mv * ../
	        command cd ..

	    fi
	done
	}
unzipSubFile(){
	fileName=$1
	fliePrefix=${fileName%%.*}
	echo "unzipSubFile the fliePrefix----------：$fliePrefix";
	#command cd $fliePrefix
	command ls *.zip | xargs -n1 unzip -o -P infected
	command rm -f *.zip
	echo "解压完毕";
	
}

finsStrByKey(){
	key=$1
	echo "开始查找 $1";
	command ls
	alreadyLogFile=${key}".log"
	echo "输出目标文件 $alreadyLogFile";
	command rm -f $alreadyLogFile
	#command find . |xargs grep -r -a -i  $key
	#command find -type f -name '*.log'|xargs grep $key 
	#command find . -type f |xargs grep -i $key 
	#command find . -type f |xargs grep -i $key | tee ${key}".log"
	#command find *.log -type f |xargs grep -i $key | tee ${key}".log"
	#command find . |xargs grep -r -a -i $key | tee ${key}".log"
	command find .| xargs grep -ri $key  | tee ${key}".log"
	#grep -i "login" -A 1  *.log | grep -v  -e  "login" >2.txt
}

mergeAllFile(){
    command rm -f merge.log
	command cat ./ *.log > merge.log
}

echo $start_line
echo "first parameter：$1";
firstParam=$1
helpCmd $firstParam
isZipFile $firstParam
mkdir $firstParam
unzipFile $firstParam
loopDir $firstParam
unzipSubFile $firstParam
key=$2
finsStrByKey $key
mergeAllFile
exit_script
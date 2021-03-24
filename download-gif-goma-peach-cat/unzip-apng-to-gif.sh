#!/bin/sh
cd ./result
for fileName in *.zip
do
    folderName=${fileName%.*}
    echo '===>>> Unzip' $fileName to $folderName ...
    unzip -u $fileName -d $folderName
    rm $fileName
    # echo $folderName/animation@2x
    cd $folderName/animation@2x
    # pwd
    for pngFile in *.png
    do  
        gifFileName=${pngFile%@*}.gif
        # echo $pngFile
        # echo $gifFileName
        apng2gif $pngFile $gifFileName > /dev/null
        mv $gifFileName ../../gif
    done
    cd ..
    cd ..
    rm -r $folderName
done
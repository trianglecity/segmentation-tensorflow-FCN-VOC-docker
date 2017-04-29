
##
##  Mini FCN.tensorflow using VisualObjectClass (VOC) dataset on Docker
##

Source code is taken from https://github.com/shekkizh/FCN.tensorflow.


NOTICE 1: VOC color annotations are converted to gray-scale annotations (0~255)

NOTICE 2: NUM_OF_CLASSESS = 255 

NOTICE 3: a very small set of VOC data is used

NOTICE 4: MITSceneParsing.pickle ( is reduced and) contains 200 images for training and 100 images for validation.


[1] download (or git clone ) this source code folder.

[2] cd downloaded-source-code-folder

[3] sudo make BIND_DIR=. shell

[4] wait... wait ... then a bash shell (root@5106c7adb44a:/#) will be ready.

[5]  root@5106c7adb44a:/# cd /home/deeplearning/

[6]  root@5106c7adb44a:/home/deeplearning# ldd --version

[7]  root@5106c7adb44a:/home/deeplearning# git clone https://github.com/tensorflow/tensorflow.git

[8]  root@5106c7adb44a:/home/deeplearning# cd tensorflow/

[9]  root@5106c7adb44a:/home/deeplearning/tensorflow# ./configure
	
	
	Please specify the location of python. [Default is /usr/bin/python]: 
	Please specify optimization flags to use during compilation when bazel option "--config=opt" is specified [Default is -march=native]: 
	Do you wish to use jemalloc as the malloc implementation? [Y/n] y
	jemalloc enabled
	Do you wish to build TensorFlow with Google Cloud Platform support? [y/N] n
	No Google Cloud Platform support will be enabled for TensorFlow
	Do you wish to build TensorFlow with Hadoop File System support? [y/N] n
	No Hadoop File System support will be enabled for TensorFlow
	Do you wish to build TensorFlow with the XLA just-in-time compiler (experimental)? [y/N] n
	No XLA JIT support will be enabled for TensorFlow
	Do you wish to build TensorFlow with VERBS support? [y/N] y
	VERBS support will be enabled for TensorFlow
	Found possible Python library paths:
	  /usr/local/lib/python2.7/dist-packages
	  /usr/lib/python2.7/dist-packages
	Please input the desired Python library path to use.  Default is [/usr/local/lib/python2.7/dist-packages]
	
	Using python library path: /usr/local/lib/python2.7/dist-packages
	Do you wish to build TensorFlow with OpenCL support? [y/N] n
	No OpenCL support will be enabled for TensorFlow
	Do you wish to build TensorFlow with CUDA support? [y/N] n
	No CUDA support will be enabled for TensorFlow
	Extracting Bazel installation...
	...........
	INFO: Starting clean (this may take a while). Consider using --async if the clean takes more than several minutes.
	Configuration finished
	
	
[10]  root@5106c7adb44a:/home/deeplearning/tensorflow# gcc -v

	
	gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4) 
	

[11]  root@5106c7adb44a:/home/deeplearning/tensorflow# bazel build --config=opt //tensorflow/tools/pip_package:build_pip_package 

	Target //tensorflow/tools/pip_package:build_pip_package up-to-date:
  	bazel-bin/tensorflow/tools/pip_package/build_pip_package
	INFO: Elapsed time: 433.238s, Critical Path: 432.46s

[12] root@5106c7adb44a:/home/deeplearning/tensorflow# bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg

	Output wheel file is in: /tmp/tensorflow_pkg


[13] root@5106c7adb44a:/home/deeplearning/tensorflow# cd /tmp/tensorflow_pkg/
[14] root@5106c7adb44a:/tmp/tensorflow_pkg# ls (copy the .whl file name)

		tensorflow-1.1.0-cp27-cp27mu-linux_x86_64.whl

[15] root@55bfc5c6b528:/tmp/tensorflow_pkg# pip install ./tensorflow-1.1.0-cp27-cp27mu-linux_x86_64.whl 

[16] root@5106c7adb44a:/tmp/tensorflow_pkg# cd /home/deeplearning/work

[17] root@5106c7adb44a:/home/deeplearning/work# python -c 'import tensorflow as tf; print(tf.__version__)'

	1.1.0-rc2

[18] root@5106c7adb44a:/home/deeplearning/work# wget https://github.com/tensorflow/models/archive/master.zip -O models.zip

[19] root@5106c7adb44a:/home/deeplearning/work# unzip ./models.zip

[20] root@5106c7adb44a:/home/deeplearning/work# export PYTHONPATH=$PYTHONPATH:$PWD/models-master/slim

[21] root@55bfc5c6b528:/home/deeplearning/work# cd Model_zoo/

[22] root@55bfc5c6b528:/home/deeplearning/work/Model_zoo# wget http://www.vlfeat.org/matconvnet/models/beta16/imagenet-vgg-verydeep-19.mat

[23] root@55bfc5c6b528:/home/deeplearning/work/Model_zoo# cd ..

[24] root@55bfc5c6b528:/home/deeplearning/work# cd VisualObjectClass.tensorflow/

[25] root@55bfc5c6b528:/home/deeplearning/work/VisualObjectClass.tensorflow# python ./FCN_VOC.py


	... inference  >> setting up vgg initialized conv layers ...
	... main >> Setting up summary op...
	... main >> Setting up image reader...
	Pickling ...
	76
	72
	... main >> Setting up dataset reader
	Initializing Batch Dataset Reader...
	{'resize': True, 'resize_size': 224}
	(76, 224, 224, 3)
	(76, 224, 224, 1)
	Initializing Batch Dataset Reader...
	{'resize': True, 'resize_size': 224}
	(72, 224, 224, 3)
	(72, 224, 224, 1)
	... main >> Setting up Saver...
	
	Step: 0, Train_loss:379.332
	 ---> Validation_loss: 403.025
	
	Step: 2, Train_loss:232.221
	
	Step: 4, Train_loss:111.811
	 ---> Validation_loss: 152.694
	
	Step: 6, Train_loss:76.4678
	
	Step: 8, Train_loss:49.828
	 ---> Validation_loss: 56.8813
	
	Step: 10, Train_loss:37.5722
	
	Step: 12, Train_loss:17.5501
	 ---> Validation_loss: 31.3623
	
	Step: 14, Train_loss:19.9523
	
	Step: 16, Train_loss:11.3688
	 ---> Validation_loss: 14.0233
	
	Step: 18, Train_loss:9.13387
	
	...
	...
	Step: 92, Train_loss:0.805693
	 ---> Validation_loss: 1.48793
	
	Step: 94, Train_loss:2.64639
	
	Step: 96, Train_loss:1.85886
	 ---> Validation_loss: 1.06966
	
	Step: 98, Train_loss:1.96469


[26] root@55bfc5c6b528:/home/deeplearning/work/VisualObjectClass.tensorflow# cd ..

[27] root@55bfc5c6b528:/home/deeplearning/work# cd FCN.tensorflow/

[28] root@55bfc5c6b528:/home/deeplearning/work/FCN.tensorflow# python ./FCN.py


	... inference  >> setting up vgg initialized conv layers ...
	Setting up summary op...
	Setting up image reader...
	Pickling ...
	200
	100
	Setting up dataset reader
	Initializing Batch Dataset Reader...
	{'resize': True, 'resize_size': 224}
	(200, 224, 224, 3)
	(200, 224, 224, 1)
	Initializing Batch Dataset Reader...
	{'resize': True, 'resize_size': 224}
	(100, 224, 224, 3)
	(100, 224, 224, 1)
	Setting up Saver...
	
	Step: 0, Train_loss:371.731
	2017-04-29 01:43:51.134592 ---> Validation_loss: 443.908
	
	Step: 2, Train_loss:145.27
	
	Step: 4, Train_loss:95.4019
	2017-04-29 01:44:14.311602 ---> Validation_loss: 143.643
	itr = 5
	itr = 6
	Step: 6, Train_loss:76.9678
	
	Step: 8, Train_loss:41.3895
	2017-04-29 01:44:44.750389 ---> Validation_loss: 93.1703
	
	Step: 10, Train_loss:44.4673
	
	Step: 12, Train_loss:20.1637
	2017-04-29 01:45:16.592646 ---> Validation_loss: 54.7973
	
	Step: 14, Train_loss:16.8914
	
	Step: 16, Train_loss:11.0603
	2017-04-29 01:45:52.160125 ---> Validation_loss: 12.2637
	
	Step: 18, Train_loss:9.23559


[29 cleanup] root@55bfc5c6b528:/home/deeplearning/work/FCN.tensorflow# rm -rf ./logs/*

[30 cleanup] root@55bfc5c6b528:/home/deeplearning/work/FCN.tensorflow# cd ..
 
[31 cleanup] root@55bfc5c6b528:/home/deeplearning/work# cd VisualObjectClass.tensorflow/

[32 cleanup] root@55bfc5c6b528:/home/deeplearning/work/VisualObjectClass.tensorflow# rm ./logs/*

[33 cleanup] root@55bfc5c6b528:/home/deeplearning/work/VisualObjectClass.tensorflow# cd ..

[34 cleanup] root@55bfc5c6b528:/home/deeplearning/work# rm ./Model_zoo/imagenet-vgg-verydeep-19.mat

[35 cleanup] root@55bfc5c6b528:/home/deeplearning/work# rm -rf ./models-master/

[36 cleanup] root@55bfc5c6b528:/home/deeplearning/work# rm ./models.zip

[37 cleanup] root@55bfc5c6b528:/home/deeplearning/work# rm  -rf ./tensorflow

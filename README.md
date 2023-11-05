# turtlbot3

## what I did : 何をやったか


ROSを用い、Turtlebot3のGazeboと繋げて、標準Worldの中で障害物にぶつからずに動き続ける制御プログラムを制作.
　・ROSのバージョンはmelodicもしくはnoeticとする
　・move_baseを利用する

 Create a control program that uses ROS and connects to Gazebo of Turtlebot3 to keep moving in a standard world without hitting any obstacles.
　The version of ROS should be melodic or noetic.
　C++ or Python must be used.



 ## iMPLEMENT : 実行
 
https://github.com/hamasakir66/turtlbot3/assets/64732352/9011138c-4263-4a96-8836-903e7054257d


## Explain to code : コードの概要 

実装したアルゴリズムとしては、
ゴールとなる目標地点を8 か所用意して、そこをランダムで選択して、ゴールを目指す。ここで、ロボットが停止したことをsubscribe した時に、次なる、ゴールを再度8 個の中からランダムで選択、移動するというコードを実装した。

また、ロボットが止まったときに、スタックの可能性を考慮しており、スタックした場合は、リカバリー戦略として、0.2 m/s で 3秒間、後進して、さらに新たなゴール位置を定義して、スタック回避を図った。


## Explain to implement code ：コードの実行方法

現在のディレクトリの構成図は、同一ディレクトリに、4つのパッケージがある。
<br>
<br>My_turtle 
<br>　- launch 
<br>　　- turtle1.launch
<br>　- scripts
<br>　　- stuck.py
<br>turtlebot3
<br>turtlebot3_gazebo_plugin
<br>turtlebot3_simulations
<br>
<br>となっており、主に、turtle1.launchで実行できるようなコードを実装した。メインコードは、stuck.pyであるので、launch ファイルが実行できない場合は、rosrunでpython　ファイルを実行させることもできる。

まず、前提条件として、ROS1, melodic使用、また、gazeboとturtlebot3、Rvizを使用しているので、その環境設定は必要である。
また、turtle1.launchにて、絶対パスを使用しており、この絶対パスを変更する必要がある。

設定が終わったら、ターミナルで、
<br>
```
(適切なディレクトリに移動)
<br> source devel/setup.bash
<br> export TURTLEBOT3_MODEL=burger
<br> roslaunch my_turtle turtle1.launch
```
<br>
<br>これにて、実行ができる。

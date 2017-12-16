## test

### 1. 文件类型判断

标志 | 代表意义
---- | ----
-e | 该『档名』是否存在？(常用)
-f | 该『档名』是否存在且为档案(file)？(常用)
-d | 该『档名』是否存在且为目录(directory)？(常用)
-b | 该『档名』是否存在且为一个block device 装置？
-c | 该『档名』是否存在且为一个character device 装置？
-S | 该『档名』是否存在且为一个Socket 档案？
-p | 该『档名』是否存在且为一个FIFO (pipe) 档案？
-L | 该『档名』是否存在且为一个连结档？

### 2. 文件权限判断

标志 | 代表意义
---- | ----
-r | 侦测该档名是否存在且具有『可读』的权限？
-w | 侦测该档名是否存在且具有『可写』的权限？
-x | 侦测该档名是否存在且具有『可执行』的权限？
-u | 侦测该档名是否存在且具有『SUID』的属性？
-g | 侦测该档名是否存在且具有『SGID』的属性？
-k | 侦测该档名是否存在且具有『Sticky bit』的属性？
-s | 侦测该档名是否存在且为『非空白档案』

### 3. 两个文件之间比较

标志 | 代表意义
---- | ----
-nt | (newer than)判断file1 是否比file2 新
-ot | (older than)判断file1 是否比file2 旧
-ef | 判断file1 与file2 是否为同一档案，可用在判断hard link 的判定上。主要意义在判定，两个档案是否均指向同一个inode 哩！

### 4.两个整数之间的判断

标志 | 代表意义
---- | ----
-eq | 两数值相等(equal)
-ne | 两数值不等(not equal)
-gt | n1 大于n2 (greater than)
-lt | n1 小于n2 (less than)
-ge | n1 大于等于n2 (greater than or equal)
-le | n1 小于等于n2 (less than or equal)

### 5.字符串判断

标志 | 代表意义
---- | ----
test -z string | 判定字串是否为0 ？若string 为空字串，则为true
test -n string | 判定字串是否非为0 ？若string为空字串，则为false。注： -n亦可省略
test str1 == str2 | 判定str1 是否等于str2 ，若相等，则回传true
test str1 != str2 | 判定str1 是否不等于str2 ，若相等，则回传false

### 6.多重条件判断

标志 | 代表意义
---- | ----
-a | (and)两状况同时成立！例如test -r file -a -x file，则file 同时具有r 与 x 权限时，才回传true。
-o | (or)两状况任何一个成立！例如test -r file -o -x file，则file 具有r 或 x 权限时，就可回传true。
! | 反相状态，如test ! -x file ，当file 不具有x 时，回传true

## shell参数

特殊变量 | 意义
---- | ----
$# | 代表后接的参数『个数』，以上表为例这里显示为『 4 』；
"$@" | 代表『 "$1" "$2" "$3" "$4" 』之意，每个变数是独立的(用双引号括起来)；
"$*" | 代表『 "$1 c $2 c $3 c $4" 』，其中c为分隔字元，预设为空白键，所以本例中代表『 "$1 $2 $3 $4" 』之意。
shift | 变量的迁移，后边接数字，从开头移除指定个数参数

## 判断

```bash
if [ condition ];then
    command
elif [ condition ]; then
    command
else
    command
fi
```

## case …… esac

```bash
case $var in
    "第一个变量内容" )
        command
        ;;
    "第二个变量内容" )
        command
        ;;
    * ) # 万用符，不符合以上的其它结果
        command
        ;;
esac

```

## fuction函数
> 参数同文件调用参数，从${1}开始

### 1. 定义

```bash
function xxxx() {
    command
}
```

### 2.调用

```bash
xxxx
```

## loop循环
```bash
while [ condition ]
do
    command
done
```

```bash
until [ condition ]
do
    command
done
```

## for...do...done 固定循环
```bash
for var in con1 con2 con3
do
    command
done
```
数值处理
```bash
for ((i=1;i<=${nu};i=i+1))
do
    command
done
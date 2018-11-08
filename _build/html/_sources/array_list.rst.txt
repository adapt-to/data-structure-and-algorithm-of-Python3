===============
2. 数组和列表
===============

数组和列表在内存空间都是线性存储的，是一种线性结构

线性结构具有的特点：
 1. 内存连续
 2. 下标访问

因为在 *python* 中list比array常用得多， *python*虽然内置了array，但是很少使用，即使使用array，
很多人也会采用numpy库中的array

*python* 中 *list* 相对于 *array* 的优势在于：
 1. *list* 中可以存储各类型的元素，还能够嵌套其他数据结构，而在 *array* 中元素的类型必须一致
 2. *list* 可以动态扩容，当预设的列表元素的容量不够时，*python* 会动态分配新的内存给它，但 *array* 有从一开始就固定的长度
 3. 还有一些其他待补充的优势

正是因为这些好处以及python追求简洁优雅的代码风格，所以 *list* 相较之下更受欢迎

--------------------------------------------------------------------

数组
======================

python内置的数组类型和其他语言（比如C）中的数组没有区别，\
通过下面这种方式可以引入python内置的array库
::

    >>> from array import array
    >>> ar = array('u','abcdef')
    >>> ar[0]
    'a'
    >>> ar[1]
    'b'
    >>> type(ar)
    <class 'array.array'>
    >>> type(ar[0])
    <class 'str'>
    >>> help(array)
    Help on class array in module array:

    class array(builtins.object)
    |  array(typecode [, initializer]) -> array
    |
    |  Return a new array whose items are restricted by typecode, and
    |  initialized from the optional initializer value, which must be a list,
    |  string or iterable over elements of the appropriate type.
    |
    |  Arrays represent basic values and behave very much like lists, except
    |  the type of objects stored in them is constrained. The type is specified
    |  at object creation time by using a type code, which is a single character.
    |  The following type codes are defined:
    |
    |      Type code   C Type             Minimum size in bytes
    |      'b'         signed integer     1
    |      'B'         unsigned integer   1
    |      'u'         Unicode character  2 (see note)
    |      'h'         signed integer     2
    |      'H'         unsigned integer   2
    |      'i'         signed integer     2
    |      'I'         unsigned integer   2
    |      'l'         signed integer     4
    |      'L'         unsigned integer   4
    |      'q'         signed integer     8 (see note)
    |      'Q'         unsigned integer   8 (see note)
    |      'f'         floating point     4
    |      'd'         floating point     8

    #############################
    ######################后续省略

通过上述代码可以看到，构建一个数组，首先要给出数组元素的类型，然后依次给出数组元素。
通过在shell模式输入 ``help(array)`` 能看到对于array中的类型声明的对应关系。

--------------------------------------------------------------------

列表
==========================

下表中记录的常见的列表操作以及对应的时间复杂度，一方面回忆列表的常用方法，另一方面分析列表的操作效率


================ ========================= ==========================================================================
对列表的操作              时间复杂度                详解  
---------------- ------------------------- --------------------------------------------------------------------------
__init__         O(1)                       底层的实现是通过建立PyListObj的对象初始化一个列表,初始化函数的执行效率是O(1)的                 
---------------- ------------------------- --------------------------------------------------------------------------
append           O(1)                       因为append是每次都在列表尾部加入，所以复杂的为O(1)
---------------- ------------------------- --------------------------------------------------------------------------
insert           O(n)                      由于insert方法是在指定索引位置插入，list需要遍历整个列表找到指定位置，\
                                           然后将插入位置后的元素全部向后挪一位并插入元素,故时间复杂度为O(n)
---------------- ------------------------- --------------------------------------------------------------------------
pop              O(1)                      pop和append正好相反，是删除list尾部的元素并返回该元素，\
                                           所以pop的时间复杂度和append一致
---------------- ------------------------- --------------------------------------------------------------------------
remove           O(n)                      由于remove需要遍历整个list找到需要删除的元素，然后执行删除。\
                                           并将删除位置处后面的元素全面向前挪一位，故时间复杂度为O(n)
================ ========================= ==========================================================================

--------------------------------------------------------------------

用List实现Array
=============================================

如何使用list实现自己的array，首先先来看一下python内置的array中有什么方法

>>> from array import array
>>> dir(array)
['__add__', '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', \
'__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', \
'__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', \
'append', 'buffer_info', 'byteswap', 'count', 'extend', 'frombytes', 'fromfile', 'fromlist', 'fromstring', 'fromunicode', 'index', 'insert', 'itemsize', 'pop', \
'remove', 'reverse', 'tobytes', 'tofile', 'tolist', 'tostring', 'tounicode', 'typecode']

上面是python内置的很多方法，具体方法详解请参考 `array — 数值的有效数组 <https://www.rddoc.com/doc/Python/3.6.0/zh/library/array/#array.array>`_ \
自己实现的话就挑一些常用的方法实现，代码如下::

 #coding:utf-8

 class Array():
     def __init__(self, maxsize=20): # 指定数组的长度，默认为20
         self.maxsize = maxsize
         self._items = [None] * maxsize

     def __len__(self): # 查看数组长度
         return len(self._items)

     def __getitem__(self, index):
         if index >= self.maxsize: # 索引从0开始
             raise Exception('out of the index')
         return self._items[index]
    
     def __setitem__(self, index, item):
         if index >= self.maxsize: # 索引从0开始
             raise Exception('out of the index')
         self._items[index] = item
     
     def clear(self):
         for i,value in enumerate(self._items):
             self._items[i] = None

     def __iter__(self):
         for item in self._items:
             yield item

     def append(self,item): # 尾部添加
         self._items += [item]

 # 测试ADT
 ar = Array(10)
 for i in range(5):
     ar[i] = i
 
 assert len(ar) == 10
 assert ar[4] == 4
 
 ar.append(1)
 assert len(ar) == 11
 assert ar[10] == 1

 ar.clear()

 assert ar[4] is None  # 这里不要用 == ，用is会更好 

如果还想实现其他的方法，可以先在python中测试一下内置array的方法具体作用，然后自己实现该方法时就知道该如何用代码实现。
或参考关于内置 ``array`` 库的官方文档中对于方法的介绍。

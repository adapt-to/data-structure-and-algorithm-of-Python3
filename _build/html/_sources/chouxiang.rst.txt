============================
1. 抽象数据类型和面向对象编程
============================

抽象数据类型
===========================

理解之前先看看什么是抽象数据类型，请看下图：

 .. image:: ./chouxiang_1.png
  :width: 300px

首先实例化了一个list对象l，然后通过IDE的联想，我们能看到在l这个对象中有很多方法。
你还可以通过下面的方式将其打印出来


>>> l = list() # 实例化对象l
>>> print(dir(l)) # 打印l中的方法
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', \
'__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', \
'__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

一个list对象中间竟然会包含这么多方法。这里的l对象就是一个抽象的数据类型(ADT)

代码实现
============================

如何用python代码，自己实现一个抽象数据类型呢？

其实你别看上面这么多方法，其实它是有迹可循的。

.. image:: ./chouxiang_2.png
 :width: 200px

上图的结构是构建ADT必备的框架，其中：
 * **data** 是指 *class* 里面必要的基础属性，例如 *array* 中的数组长度
 * **method** 则是指 *class* 具备的一些方法，例如上述的 *list* 对象中就有 *append*、*len*、*clear* 等方法
 * 一个 *class* 应该具备哪些 *data* 和 *method* 需要根据实际的问题实际考虑

.. note::
 TIPS：
  上述所说的方法，你也可以称为函数，在python中方法和函数没有特别统一的区分。但如果是在某个对象中的函数，我们还是习惯于将它称为这个对象的方法
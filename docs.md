# Documentation for JNN

Every non-constant in this notation is a number.
That is where the third part of the acronym comes from.

## How to represent

The simplest JNN expression is just a number.
`5.0`
Every non-number expression looks like this:
~~~
{
    "type":"...",
    "val":...
}
~~~
The type can be one of the following:

`const`<br/>
`sum`<br/>
`product`<br/>
`reciprocal`<br/>
`floor`<br/>
`ceil`<br/>
`switch`<br/>
`compare`<br/>
`variable`

Always a string, *never an expression*.
Each one will be explained in detail later. (though it's probably unnecessary)
The `val` type, however, is usually an expression (or list of expressions). The only exception is `variable`, in which it's a string.

## Types

`const`:
The value of this expression is exactly what `val` is.
Completely useless.
Ex:
~~~
{
    "type":"const",
    "val":5.0
}
~~~
 &#124;<br/>
 v
~~~
5.0
~~~
`sum`:
Sums the items in `val` which are evaluated beforehand.
`val` is a list.
Ex:
~~~
{
    "type":"sum",
    "val":[
        7.0,
        {
            "type":"const",
            "val":3.0
        },
        4
    ]
}
~~~
 &#124;<br/>
 v
~~~
14.0
~~~
`product`:
Same as `sum` except instead of adding them, it multiplies them.
If you changed the type in the previous example from `sum` to `product`, you would get:
~~~
84.0
~~~
`reciprocal`:
Performs the reciprocal.
Can be used with `product` to perform divison.
~~~
{
    "type":"product",
    "val":[
        10
        {
            "type":"reciprocal",
            "val":2
        }
    ]
}
~~~
 &#124;<br/>
 v
~~~
5.0
~~~
`floor`:
Gives the floor.
~~~
{
    "type":"floor",
    "val":3.5
}
~~~
 &#124;<br/>
 v
~~~
3
~~~
`ceiling`:
Self-explanatory.
`switch`:
Gives the val[1]+2th item in the list. If not there, gives val[2]
~~~
{
    "type":"switch",
    "val":[
        2,   <-- selector
        4,
        7,
        8,
        9
    ]
}
~~~
 &#124;<br/>
 v
~~~
8
~~~
and
~~~
{
    "type":"switch",
    "val":[
        7000,
        4,
        7,
        8,
        9
    ]
}
~~~
 &#124;<br/>
 v
~~~
4
~~~
`variable`:
This one is special. `val` *is not an expression*. It is instead a string.
This is the only way to access things outside the expression, and for it to not be a constant value.
The evaluator should have a parameter for variables.
Suppose:
~~~
vars={"v":5}
~~~
Then:
~~~
{
    "type":"sum",
    "val":[
        3,
        {
            "type":"variable",
            "val":"v"           <-- Notice how this is not an expression
        }
    ]
}
~~~
 &#124;<br/>
 v
~~~
8
~~~

#

version 1.1:
Added floor, ceil, switch, and comp



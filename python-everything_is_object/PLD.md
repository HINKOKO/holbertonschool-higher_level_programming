- **ex18 - WHY**
def assign(n, v):
	n = v

l1 = [1, 2]
l2 =[3, 4]
assign(l1 , l2)
print(l1)
still [1, 2] !!

- **ex26 - WHY**
a and b two empty tuples:
a = ()
b = ()
and a is b is True ! whereas two same tuples:
a = (1, 2)
b = (1, 2)
a is b is False !

- **ex27 - BECAUSE**
We re-declare an variable "a" to be equal
to an previously existing list a = [1,2] and we add
 an element to this a list:
>>> a = [1,2]
>>> id(a)
140577824553024
>>> a = a + [3]
>>> id(a)
140577824552896

You know what? It works even if you had added [0]
>>> a = [1,2]
>>> id(a)
140389766740032
>>> a = a + [0]
>>> id(a)
140389766740160
''' it has changed ! '''

- **ex28 - BECAUSE**
In this one we use the operator ``+=`` so we **conserve**
our list declared as "a"
>>> a = [1,2]
>>> id(a)
140389766740160
>>> a += [12]
>>> id(a)
140389766740160
>>> 
It doesn't change, because we didn't "redeclare" a, we used ``a += ...``

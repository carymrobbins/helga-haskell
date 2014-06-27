helga-haskell
=============

Evaluate Haskell expressions using helga!

Installation
------------
`pip install helga-haskell`

Usage
-----
```haskell
<crobbins>  :t liftM
<helga>     liftM :: Monad m => (a1 -> r) -> m a1 -> m r
<crobbins>  > [x*2 | x <- [1,2,3]]
<helga>     [2,4,6]
<crobbins>  > foobar
<helga>     ERROR: Not in scope: `foobar'
```

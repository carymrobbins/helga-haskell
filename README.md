helga-haskell
=============

Evaluate Haskell expressions using helga!

```haskell
<crobbins>  :t liftM
<helga>     liftM :: Monad m => (a1 -> r) -> m a1 -> m r
<crobbins>  > [x*2 | x <- [1,2,3]]
<helga>     [2,4,6]
```

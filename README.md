Argue
=====

Usage
-----

Set options, bounds, and conditions for your functions and methods!

Instead of having to write bounds checks within a function and clutter up the 
function itself, set the bounds in a simple decorator and keep your logic clean:

        import argue
        
        @argue.bounds(first=(0, 5), second=(6, 10))
        def limited_add(first, second):
            return first + second
            
Replaces:

        def limited_add(first, second):
            if 0 > first or first > 5:
                raise ValueError(...)
            elif 6 > second or second > 10:
                raise ValueError(...)
            else:
                return first + second

Set the available options for a given input:

        import argue
        
        @argue.options(length=('short', 'long'))
        def select(length):
            return f"This took a {length} time"
            
Replaces:

        def select(length):
            if length not in ('short', 'long'):
                raise ValueError(...)
            else:
                return f"This took a {length} time"
                
Finally, set conditions for methods:

        import argue
        
        class ConditionalClass:
            a = False
            
            def do_first(self):
                self.a = True
                
            @argue.conditional(a=True)
            def do_second(self):
                pass
                
`argue` will look up the class attribute `a` for the condition before proceeding with the method.

**Note that `conditional` only works on methods, not functions.**

Installation
------------

        pip install argue

FAQ
---

**Is this a replacement for `typing`?**

No, this does not check types. It's only for limiting input.

**Is this a type-checker?**

No, that would be unPythonic. This allows you and your users to have descriptive and helpful 
error messages when the input is not what it should be.
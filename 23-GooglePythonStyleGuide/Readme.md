- Write code easier to change and easier to extend
- imports
    - see where things come from
    - no wild card imports - pollute global namespace
    - import module -> and the get function from module
    Ex. 
    Wrong
    from my_package.my_module import my_function
    my_function()
    Right
    from my_package import my_module
    my_module.my_func()
- Using main function 
    - not accidently run code, importing or executable module
    - put code under if statement, all variables global namespace -> avoid it. local scope better 
    def main(argv: Sequence[str]):
        #process non flag args
        ...

    if __name__ == '__main__': #executable code 
        app.run(main)  # or main()
- Comprehensions and generator expressions
    - map, filter and lambda
    - avoid complexity here -> ex. nested looping
- Default Argument Values
    - provide reasonable setting for function
    - dangers
        - avoid writing fns with way too many args -> use fn hard , loss of cohesion as do more things with fn
        - watch out if default values are mutable ex list  (Never do) -> python evaluate when module is loaded
        ex. 
            def oops(my_list: list[int]=[]):
                my_list.append(30)
                return my_list
        
        Call -> oops() -> [30]
                oops() -> [30, 30] #reuse list again
- Properties -> control getting or setting attributes that require trivial logic 
    - access like Instance variable
    - should be cheap and simple 
    - Ex.
    @property
    def total_price(self) -> int:
        return self.price * self.quantity

    call using object of class
    l1=LineItem(args)
    l1.total_price    

- Getters and Setters
    - if complex calculation for attribute 
    - if read/write then just use public attribute 
    eX.
    @dataclass
    class Order:
        items: list[LineItem] = field(default_factory=list)
        _payment_status: PaymentStatus = PaymentStatus.PENDING
    
    def get_payment_status(self) -> PaymentStatus:
        return self._payment_status

    def set_payment_status(self, status: PaymentStatus) -> None:
        if self._payment_status = PaymentStatus.PAID:
            raise PaymentStatusError("You cant change the status of already paid order")
        self._payment_status = status

- Lexical Scoping
    - Nested python fns - call variables from outside own scope but not assign values to it
    - resolves at compile time 
    - Ex. Below code errors out -

    def my_func():
        x:int = 3

        def int_func():
            print(x)   #Error here as try to access local var before assigned below
            x=5 

        for _ in range(3):
            int_func()

    def main():
        my_func()

- Exception Handling
    - not do everywhere in code, ignore and another part of code handle it
    - use built in class exception -> outofrange
    - not use assert for exceptions but raise statement for error
    - assert in unit tests
    - not use catch all exceptions
    - minimize code in try / except - error there
    - finally or context manager 















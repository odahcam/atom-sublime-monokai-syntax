var obj = {
    bar: "helo",
    foo: function(arg, baz) {
        var i = 0;

        this.options = arguments;

        return true;
    }
};

obj.foo();

console.log(obj.bar, obj.foo());

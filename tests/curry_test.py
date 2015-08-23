from curry import curry


@curry
def crazy(a, self):
    return a + self.starter


class HasCurryMethods(object):

    def __init__(self, starter):
        self.starter = starter
        self.on_instance = crazy

    @curry
    def curry(self, x, y=0):
        return self.starter * x * y

    on_class = crazy(1)


def test_curry_method_behavior():
    assert HasCurryMethods(2).curry(y=2)(1) == 4
    hpm = HasCurryMethods(2)
    assert hpm.on_instance(2, hpm) == 4
    assert hpm.on_class() == 3


def test_curry_with_kwargs_taking_function():
    @curry
    def kwarg_taking_function(arg, **kwargs):
        kwargs['k'] = arg
        return kwargs

    assert kwarg_taking_function(a=14)(2) == {'k': 2, 'a': 14}


def test_curry_cache_behavior_problems():

    class CurryCacheTest(object):
        def func(self, a=1):
            return 2 + a

        test = curry(func)

        def func(self):
            return 1

    instance = CurryCacheTest()
    assert instance.func() == 1
    assert instance.test() == 3
    assert instance.func() == 1

    # Ensure we are getting new bound instances each time
    assert instance.test is not instance.test
    assert instance.func is not instance.func

    class CurryCacheTest2(object):
        def func(self, a=1):
            return 2 + a

        test = curry(func, cache_name='test')

        @curry(cache_name=True)
        def func(self):
            return 1

    instance = CurryCacheTest2()
    assert instance.func() == 1
    assert instance.test() == 3
    assert instance.func() == 1

    # Ensure we are caching the result of the curry each time
    assert instance.test is instance.test
    assert instance.func is instance.func

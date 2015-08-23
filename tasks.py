from invoke import Collection, task, run

from curry import curry


ns = Collection()


@curry
def ns_task(function, *args, **kwargs):
    return ns.add_task(task(*args, **kwargs)(function))


@ns_task(default=True)
def test(args=''):
    run("py.test {}".format(args))

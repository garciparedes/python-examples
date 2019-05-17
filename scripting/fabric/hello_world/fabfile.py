from fabric import task


@task
def hello(c):
    c.run(f'echo "Hello World!"')

import desci.fetch as desci

with desci.fetch([('hello.py', 'imported')], "ZtAUWvdgKwKkFLhBTg254r6ce2vZTysTg5S3XttT1B0/1/1/!"):
    import imported
    print(str.upper(imported.hello()) + " world!")

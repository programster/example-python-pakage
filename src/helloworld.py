def sayHello(name=None):
    """
    Generate a hello message

    :param str name: optionally specify the name of the person to say hello to.
    :return str: The generated message.
    """
    if name is None:
        response = "Hello world!"
    else:
        response = f"Hello, {name}!"

    return response
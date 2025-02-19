class MinhaClasse:
    """
    A context manager class that prints messages upon entering and exiting a context.
    Methods
    -------
    __enter__():
        Prints "Entrou" when entering the context.
    __exit__(exc_type, exc_value, traceback):
        Prints "Saiu" when exiting the context.
    """

    def __enter__(self):
        print("Entrou")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Saiu")


with MinhaClasse() as mc:
    print("Executou dentro do contexto")

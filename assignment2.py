from pyswip import Prolog

def main():
    prolog = Prolog()
    prolog.assertz("father(michael,john)")
    prolog.assertz("father(michael,gina)")

    for soln in prolog.query("father(X,Y)"):
        print(soln["X"], "is the father of", soln["Y"])

    print("Hello world!")


if __name__ == '__main__':
    main()
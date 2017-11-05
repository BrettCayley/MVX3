class Swaption:

    def Payoff(self):
        return 5

    def Events(self):
        return 5

    # Workflow MC
    # implementor holds model calibrates model with market
    # implementor invokes simulator generates St
    # Contract holds payoff
    #
    # Workflow Analytic
    # implementor holds model to get ie vol
    # contract holds payoff
    #
    # engine(implementor, request, results, diagnostics)
    # set model in env
    # dp in excel dpEvaluate(contract, env, pv)
    # qlx in excel eqmodelresults(modelname, contract, context, modelinputs)
    # MVx in excel eqEvaluate(contract, context)
    # get trade, get marketdata, trade.PV

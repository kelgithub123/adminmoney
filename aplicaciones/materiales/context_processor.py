def importe_total(request):
    #esta variable se accede desde cualqueir lugar
    total=0
    for key, value in request.session["carro"].items():
        total=total+(float(value["precio"])*value(["cantidad"]))
    return {"importe_total":total}
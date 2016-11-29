from django.shortcuts import render

def equal_int(num):
    try:
        if not num:
            return "", "коэффициент не определен"
        elif int(num) == 0:
            return 0, ""
        elif int(num):
            return int(num), ""
    except ValueError:
        return num, "коэффициент не целое число"

def quadratic_results(request):
    a, error_a = equal_int(request.GET.get('a'))
    b, error_b = equal_int(request.GET.get('b'))
    c, error_c = equal_int(request.GET.get('c'))
    dict_html = {
        "a": a, "error_a": error_a,
        "b": b, "error_b": error_b,
        "c": c, "error_c": error_c,
        "diskr": "",
        "info_text": ""
    }
    if isinstance(a, int) and a != 0 and isinstance(b, int) and isinstance(c, int):
        diskr = b * b - 4 * a * c
        dict_html['diskr'] = "Дискриминант: {0}".format(diskr)
        if diskr < 0:
                dict_html["info_text"] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        elif diskr == 0:
            x1 = -b / 2 * a
            dict_html["info_text"]= "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {0}".format(x1)
        else:
            x1 = (-b + diskr ** (1 / 2)) / 2 * a
            x2 = (-b - diskr ** (1 / 2)) / 2 * a
            dict_html["info_text"] = "Квадратное уравнение имеет два действительных корня: х1 = {0}, х2 = {1}".format(x1, x2)
    elif a == 0:
        dict_html["error_a"] = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
        dict_html["diskr"] = ""
    return render(request, 'quadratic/results.html', dict_html)

from django.shortcuts import render

def equal_int(num):
    try:
        if not num:
            return "", "коэффициент не определен"
        elif int(num) == 0:
            return 0, ""
        elif int(num):
            return int(num), ""
    except :
        return num, "коэффициент не целое число"

def quadratic_results(request):
    a, prefix_a = equal_int(request.GET.get('a'))
    b, prefix_b = equal_int(request.GET.get('b'))
    c, prefix_c = equal_int(request.GET.get('c'))
    dict_html = {
        "a": a, "prefix_a": prefix_a or "",
        "b": b, "prefix_b": prefix_b or "",
        "c": c, "prefix_c": prefix_c or "",
        "diskr": "",
        "info_text": ""
    }
    print(a, b, c)
    if isinstance(a, int) and a != 0:
        diskr = b * b - 4 * a * c
        dict_html['diskr'] = "Дискриминант = {0}".format(diskr)
        if diskr < 0:
                dict_html["info_text"] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        elif diskr == 0:
            x1 = -b / 2 * a
            dict_html["info_text"]= "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {0}".format(x1)
        else:
            x1 = (-b + diskr ** (1 / 2)) / 2 * a
            x2 = (-b - diskr ** (1 / 2)) / 2 * a
            dict_html["info_text"] = "Квадратное уравнение имеет два действительных корня: x1 = {0}, x2 = {1}".format(x1, x2)
    elif a == 0:
        dict_html["prefix_a"] = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
        dict_html["diskr"] = ""
    return render(request, 'results.html', dict_html)

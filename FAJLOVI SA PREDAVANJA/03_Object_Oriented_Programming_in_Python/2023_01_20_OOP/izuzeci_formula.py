   #---------------------------------------------#
   #             E X C E P T I O N S             #
   #---------------------------------------------#


def deljenje(a,b):
    return a/b

try:
    print(deljenje(8,0))
except ZeroDivisionError as i:
    print('error:', i)
except ValueError:
    print('greska prilikom konverzije vrednosti')
except TypeError:
    print('TYPE ERROR')
except Exception:
    print('ko zna sta si uradio')
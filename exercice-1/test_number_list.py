def convert_to_integer(input_list: list) -> list:
  """Cette fonction parcourt la liste donnée en entrée et
  convertit tous les éléments qui peuvent l'être en entiers.

  Elle renvoie ensuite une liste en sortie comportant tous les nombres qui ont pu être interprêtés
  """
  output_list = []
  for el in input_list:
    try:
      v = int(el)
    except ValueError:
      print(f"Erreur: {el} ne peut pas être interprêté comme un entier")
      continue
    output_list.append(v)
  return output_list

def test_convert_to_integer():
    assert convert_to_integer([1, 2, 3, 4]) == [1, 2, 3, 4]

test_convert_to_integer()

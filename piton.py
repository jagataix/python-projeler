
integer_ornek = 42
float_ornek = 3.14
string_ornek = "Hello, World!"
boolean_ornek = True
list_ornek = [1, 2, 3, 4, 5]
tuple_ornek = (1, 2, 3)
dictionary_ornek = {"anahtar1": "değer1", "anahtar2": "değer2"}


integer_tipi = type(integer_ornek).__name__
float_tipi = type(float_ornek).__name__
string_tipi = type(string_ornek).__name__
boolean_tipi = type(boolean_ornek).__name__
list_tipi = type(list_ornek).__name__
tuple_tipi = type(tuple_ornek).__name__
dictionary_tipi = type(dictionary_ornek).__name__


print(f"Integer örneği: {integer_ornek}, Veri Tipi: {integer_tipi}")
print(f"Float örneği: {float_ornek}, Veri Tipi: {float_tipi}")
print(f"String örneği: {string_ornek}, Veri Tipi: {string_tipi}")
print(f"Boolean örneği: {boolean_ornek}, Veri Tipi: {boolean_tipi}")
print(f"List örneği: {list_ornek}, Veri Tipi: {list_tipi}")
print(f"Tuple örneği: {tuple_ornek}, Veri Tipi: {tuple_tipi}")
print(f"Dictionary örneği: {dictionary_ornek}, Veri Tipi: {dictionary_tipi}")

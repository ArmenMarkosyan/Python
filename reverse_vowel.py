def reverse_vowels(str):
	vowels = ""
	for char in str:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string

print(reverse_vowels("Armen"))
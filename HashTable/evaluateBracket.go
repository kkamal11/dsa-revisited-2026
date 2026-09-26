package main

func evaluate(s string, knowledge [][]string) string {

	var result string
	var string_key string
	var str string
	var opened bool
	knowledge_map := make(map[string]string, len(knowledge))

	for _, k := range knowledge {
		key, val := k[0], k[1]
		knowledge_map[key] = val
	}

	for _, st := range s {
		str = string(st)

		if str == "(" {
			opened = true

		} else if str == ")" {
			val, exists := knowledge_map[string_key]
			if !exists {
				val = "?"
			}
			result += val
			opened, string_key = false, ""

		} else if opened {
			string_key += str

		} else {
			result += str
		}
	}

	return result
}

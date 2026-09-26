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

func evaluate(s string, knowledge [][]string) string {

	var result []string
	var string_key []string
	var str string
	var opened bool
	knowledge_map := make(map[string]string, len(knowledge))

	for _, k := range knowledge {
		knowledge_map[k[0]] = k[1]
	}

	for _, st := range s {
		str = string(st)

		if str == "(" {
			opened = true

		} else if str == ")" {
			val, exists := knowledge_map[strings.Join(string_key, "")]
			if !exists {
				val = "?"
			}
			result = append(result, val)
			opened, string_key = false, nil

		} else if opened {
			string_key = append(string_key, str)

		} else {
			result = append(result, str)
		}
	}

	return strings.Join(result, "")
}


func evaluate(s string, knowledge [][]string) string {

    var result strings.Builder
    var string_key strings.Builder
    var opened bool
    knowledge_map := make(map[string]string, len(knowledge))

    for _, k := range knowledge{
        knowledge_map[k[0]] = k[1]
    }

    for _, str := range s{

        if str == '('{
            opened = true

        } else if str == ')'{
            val, exists := knowledge_map[string_key.String()]
            if !exists{
                val = "?"
            }
            result.WriteString(val)
            opened = false
            string_key.Reset()

        } else if opened {
            string_key.WriteRune(str)

        } else {
            result.WriteRune(str)
        }
    }

    return result.String()
}
class ObservedPinKt {
    companion object {
        private val possibles = arrayOf("08", "124", "2135", "326", "4157",
                                        "52468", "6359", "748", "80579", "968")
        private var result: MutableList<String> = mutableListOf()

        fun getPINs(observed: String): List<String> {
            result = mutableListOf()
            buildPinStrings("", observed)
            return result
        }

        private fun buildPinStrings(partial: String, remaining: String) {
            // If there are no more digits, add the pin string to the result:
            if (remaining.isEmpty()) {
                result.add(partial)

            } else {
                // Loop through the possible digits and recursively build the remainder of the pin string:
                for (element in possibles[remaining[0] - '0']) {
                    buildPinStrings(partial + element, remaining.substring(1))
                }
            }
        }
    }
}


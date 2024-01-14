package kg.com

import kotlin.math.max

class Day2 {

    fun execute() {
        val arrayOf = arrayListOf<String>()

        val inputStream = Day2::class.java.getResource("/input_day2.txt").openStream()
        inputStream.bufferedReader()
            .forEachLine { arrayOf.add(it) }

        val result = isPossibleTask2(arrayOf.toTypedArray())
        println("total result is $result")
    }

    //12 red cubes, 13 green cubes, and 14 blue
    // "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    fun isPossibleTask1(lines : Array<String>) : Long {

        val finalList = mutableListOf<List<Triple<Int, Int, Int>>>()

        var summa = 0L
        for (line in lines) {
            val gameNSets = line.split(":")
            val game = gameNSets[0].replace("Game ", "")
            val sets = gameNSets[1].split(";")

            val setList = mutableListOf<Triple<Int, Int, Int>>()
            for (set in sets) {
                val balls = set.split(",")
                val colorMap = hashMapOf<String, Int>()
                for (ball in balls) {
                    val numNColor = ball.trim().split(" ")
                    colorMap[numNColor[1].trim()] = Integer.valueOf(numNColor[0].trim())
                }
                val tripleRGB = transformer(colorMap)

                setList.add(tripleRGB)
            }
            if (isListValid(setList)) {
                summa += Integer.valueOf(game.trim())
            }
            finalList.add(setList)
        }
        println(finalList)
        return summa
    }

    private fun isListValid(rgbList: List<Triple<Int, Int, Int>>) : Boolean {
        for (rgb in rgbList) {
            if (!isValid(rgb)) {
                return false
            }
        }
        return true
    }

    private fun isValid(rgb: Triple<Int, Int, Int>):Boolean {
        if(rgb.first <= 12 && rgb.second<= 13 && rgb.third <= 14) {
            return true
        }
        return false
    }

    private fun transformer(map: Map<String, Int>) : Triple<Int, Int, Int> {
        var red = 0
        var green = 0
        var blue = 0
        for( entry in map.entries ) {
            if(entry.key == "red") {
                red = entry.value
            }
            if(entry.key == "green") {
                green = entry.value
            }
            if(entry.key == "blue") {
                blue = entry.value
            }
        }
        return Triple(red, green, blue)
    }

    fun isPossibleTask2(lines : Array<String>) : Long {

        val finalList = mutableListOf<List<Triple<Int, Int, Int>>>()

        var summa = 0L
        for (line in lines) {
            val gameNSets = line.split(":")
            val sets = gameNSets[1].split(";")

            val setList = mutableListOf<Triple<Int, Int, Int>>()
            for (set in sets) {
                val balls = set.split(",")
                val colorMap = hashMapOf<String, Int>()
                for (ball in balls) {
                    val numNColor = ball.trim().split(" ")
                    colorMap[numNColor[1].trim()] = Integer.valueOf(numNColor[0].trim())
                }
                val tripleRGB = transformer(colorMap)

                setList.add(tripleRGB)
            }

            summa += minBallsNeeded(setList)

            finalList.add(setList)
        }
        println(finalList)
        return summa
    }

    private fun minBallsNeeded(rgbList: List<Triple<Int, Int, Int>>) : Long {
        var minRed = 0
        var minGreen = 0
        var minBlue = 0

        for (rgb in rgbList) {
            minRed = max(minRed, rgb.first)
            minGreen = max(minGreen, rgb.second)
            minBlue = max(minBlue, rgb.third)
        }
        return (minRed * minGreen * minBlue * 1L)
    }
}
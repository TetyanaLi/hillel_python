#4. Вывести на консоль своё имя, нарисованное 'звёздочками'


#   *       *        *         *       * *********
#   **      *       * *        **     ** *
#   * *     *      *   *       * *   * * *
#   *  *    *     *     *      *  * *  * *******
#   *   *   *    *       *     *   *   * *
#   *    *  *   ***********    *       * *
#   *     * *  *           *   *       * *
#   *      ** *             *  *       * *
#   *       * *              * *       * **********

#   * доп. Вывод арт-ascii текста модулем art
#       (pip install art). Прочитать можно в репозитории PyPi - search - art.


print('*****  **  *  *  * *\n  *   *  * *  * *  *\n  *   **** ****  ***\n  *   *  * *  *  * *\n  *   *  * *  * *  *')


from art import *


tprint("TANYA", font=randart())

tanya = "TANYA"

tprint("TANYA", font=ascii(''))  # горит желтая лампочка, но прикольно!!!

tprint(ascii(tanya))
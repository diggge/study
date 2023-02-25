from package_1 import module_1
module_1.function1()
from package_1.module_1 import function1
function1()
import package_1.module_1
package_1.module_1.function1()  # тут нужно полное имя модуля
from package_1.subpackage import module_2
module_2.function2()
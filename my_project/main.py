from my_package import calc_utils
from my_package import weather_utils

square_result = calc_utils.square(5)
cube_result = calc_utils.cube(3)
print("Square of 5 =", square_result)
print("Cube of 3 =", cube_result)

(weather_utils).today_weather()
(weather_utils).forecast()

def computepay(hours, rate):
   if hours >= 40:
     return (hours * rate) + ((hours - 40) * (rate * 0.5))
   else:
      return (hours*rate)


print(computepay(45,10))
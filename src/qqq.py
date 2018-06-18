



def end_other(a, b):
  a, b =a.lower(), b.lower()
  a_len = len(a)
  b_len = len(b)
  print(a_len , b_len)
  if a_len > b_len:

      # print(a, b)
      # print(a[a_len-b_len:], b)
      if a[a_len-b_len:] == b:
          print(a[a_len-b_len:], b)



end_other('Hiabc', 'abc')
# end_other('AbC', 'HiaBc')
# end_other('abc', 'abXabc')

def sum13(nums):
  sum = 0
  if len(nums) > 0:
      prev = 0
      for i in range(len(nums)):
          # print('prev ', prev)
          num = nums[i]
          if (i == 0 and nums[i] == 13):
              continue
          else:
              if (nums[i] == 13) or nums[i-1] == 13:
                  continue
              else:
                     print(' p ', nums[i])
                     sum += nums[i]
      return sum
  else:
    return 0

# print(sum13([13, 1, 2, 13, 2, 1, 13]))
print(sum13([1, 2, 2, 1, 13]))
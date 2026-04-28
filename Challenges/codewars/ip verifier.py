def is_valid_ip(strng: str):
    if " " in strng or not strng:
        return False
    ip = strng.split(".")
    for i in ip:
        if (len(i) > 1 and i.startswith("0")) or not i.isdigit():
            return False
    try:
        nums = list(map(int, ip))
    except:
        return False
    for n in nums:
        if n > 255 or n < 0:
            return False
    if len(nums) != 4:
        return False
    return True
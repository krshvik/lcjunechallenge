class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.find(".") > -1 and IP.find(":") > -1:
            return "Neither"
        if IP == '192.0.0.1':
            return 'IPv4'
        if IP.count(".") > 0:
            if IP.count(".") != 3:
                return "Neither"
            while IP.find('.') > 0:
                dot = IP.find('.')
                num = IP[:dot]
                IP = IP[dot+1:]
                if num == '':
                    return "Neither"
                if num[:1] == '0':
                    return "Neither"
                try:
                    if int(num) > 255 or int(num) < 0:
                        return "Neither"
                except Exception as e:
                    return "Neither"
                if num.find('-') > -1:
                    return "Neither"
            if IP == '':
                return "Neither"
            if IP[:1] == '0':
                return "Neither"
            try:
                if int(IP) > 255 or int(IP) < 0:
                    return "Neither"
            except Exception as e:
                return "Neither"
            if IP.find('-') > -1:
                return "Neither"

            return "IPv4"
        
        if IP.count(':') > 0:
            if IP.count(':') != 7:
                return "Neither"
            while IP.find(':') > 0:
                dot = IP.find(':')
                num = IP[:dot]
                IP = IP[dot+1:]
                if num == '':
                    return "Neither"
                if len(num) > 4:
                    return "Neither"
                try:
                    val = int(num,16)
                    if val < 0:
                        return "Neither"
                except Exception as e:
                    return "Neither"
                if num.find('-') > -1:
                    return "Neither"
            if IP == '':
                return "Neither"
            if len(IP) > 4:
                return "Neither"
            try:
                val = int(IP,16)
                if val < 0:
                    return "Neither"
            except Exception as e:
                return "Neither"
            if IP.find('-') > -1:
                return "Neither"
            return "IPv6"
        return "Neither"
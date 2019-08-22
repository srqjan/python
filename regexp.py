import re

"""
.   any single charakter
+   one or more time repeated
*   zero or more times repeated
^   begining of the line (string - matching pattern)
$   end of the line ( matching pattern )
\s  whitespace
\d  digit (number )
\S  non-whitespace


usage:  re.search (r"regexp" , text_file)

"""

line = "10.1.1.1"
ipadd = line

re.search(r"...", ipadd)   # match 10.   ( samo tri tacke - tri caractera 1 0 . )
re.search(r".+", ipadd)      # match 10.1.1.1  ( celu ip adresu ) isto je i sa (r".+", ipadd)
re.search(r"\d\d", ipadd).group(0)    # matcj 10 ( two digits /d/d )

ip = "    192.168.1.5"
re.search(r"\s+\S+", ip)   # '    192.168.1.5'  match whitespace i nonwhitespace , ceo string

#GROUP Jako vazno
text = "Cisco IOS software, C880 Software , Version 15.4(2)T1, Release"

#Group 0  .group(0) matchuje ceo string , sve sto se match-uje "^C.*$
re.search(r"^C.*$, text").group(0)  #match='Cisco IOS software, C880 Software , Version 15.4

#Group 1 (2,3,4 ... ) matchuje samo ono sto je u zagradi () i sluzi da se EXTRAKTUJE NESTO iz stringa

sw = re.search(r"^C.*, Version (\S+),.*$", text ).group(1)  #  '15.4(2)T1' extract and assign to variable sw jer se to match-uje u zagradi

# Extractovanje dva patterna
re.search(r"^Cisco (.*), Version (\S+),.*$", text ).group(1) # 'IOS software, C880 Software ' ( prva zagrada )
re.search(r"^Cisco (.*), Version (\S+),.*$", text ).group(2) # '15.4(2)T1'   ( sada je ovo druga zagrada )

# EXTRACT I STAVI U DICTIONARY VALUE , KEY SAM IMENUJES  (?P<dict_key_name> regexp_match )  regexp_match je value
 os = re.search(r"^Cisco (.*), Version (?P<dict_key>\S+),.*$", text ).groupdict()  # os = {'dict_key': '15.4(2)T1'}
# type(os) <class 'dict'>   # os je dictionary

#ili
match = re.search(r"^Cisco (.*), Version (?P<dict_key>\S+),.*$", text )
#>>> match.groupdict()    # result {'dict_key': '15.4(2)T1'}

#Greedy and non greedy

text1 = "Cisco IOS software, C880 Software , Version 15.4(2)T1, Release"

#ako zelimo match do nekog karaktera , prvi zarez npr (match Cisco IOS software ) moramo da stavimo znak ? jer po default-u
# python ce match-ovati string do kraja jer imamo vise zareza u okviru text1

# >>> re.search(r"^Cisco (.*)," , text1)   # bez ? znaka ,hocemo match do prvog , matchuje sve # match='Cisco IOS software, C880 Software , Version 15.4

#>>> re.search(r"^Cisco (.*?)," , text1)  @ sa ? znakom matchuje minimalni broj ponavlajnja # match='Cisco IOS software,'
# match se radi lefto to right kao sto citamo

# ako nemamo ,
#re.search(r"^Cisco (.*?)" , text1)     # match='Cisco '   ( match minimum characters )

# MATCH U OKVIRU VELIKOG STRINGA , Multiline string !!!! 

# regex match-uje pocetak string-a ^ prvi red (line ) prvi character , $ matchuje kraj stringa ,posledni red (line )
# ako je ono sto zelimo match-ovati u nekoj liniju u sredini ,moramo reci regex-u da radi search line by line
# to se postize sa flags=re.M

re.search(r"^String_in_line_n (.*)$" , text1, flags=re.M)  # ide line by line i trazi nas pattern

#  search .*   matchuje samo prvu liniju , ne prelazi u sledecu , da bi to promenili use flags=re.DOTALL
re.search(r"^Cisco.*", text , flags=re.DOTALL)  # za multiline string

## REPLACE PATERN with regexp re.sub

re.split(r"---------.*$", '############', text1, flags=re.M)   # menjamo ----- with #####


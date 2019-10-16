import re


"""
.   - any single charakter except new line 
+   - 1 or More  one or more time repeated
*   - 0 or More zero or more times repeated
?   - 0 or One 
{3} - exact number 
{3,9}  - range of numbers ( Minimum , Maximum )
^   - begining of the line (string - matching pattern)
$   - end of the line ( matching pattern )
[]  - Matches character in brackets 
[^] - Matches charackters NOT in brackets 
\s  - whitespace
\S  - NOT whitespace ( TAB , space , newline )
\d  - digit (number 0-9)
\D  - NOT a Digit (0-9)
\w  - Word character (a-z , A-Z ,0-9, _ )
\W  - NOT a Word character 
\b  - Word Boundary 
\B  - Not a Word Boundary 



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
re.search(r"^C.*$", text).group(0)  #match='Cisco IOS software, C880 Software , Version 15.4

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

#re.split(r"---------.*$", '############', text1, flags=re.M)   # menjamo ----- with #####

# primer
text = 'vrf definition POLICE'
pattern = r'vrf\s+definition\s+(?P<vrf_name>\S+)'   # name to capture group (?P<vrf_name>\S+) - (<vrf_name> dict key ,value is match)
match = re.search(pattern, text)       # nadji pattern u  textu
if match:
    print (match.groupdict())        # {'vrf_name': 'POLICE'}


# Corey Shaver video regex odlicno https://www.youtube.com/watch?v=K8L6KVGG-7o&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=30

pat1 = re.compile(r'\d{3}.\d{3}.\d{4}')   # 3 ,4 broj digita \3{3} = \d\d\d


pat2 = re.compile(r'https?://(www\.)?')  # ?     posle nekog znaka kaze da je on opcionalan ( 0 or 1 ) match http i https , www ili empty
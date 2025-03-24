class PositiveCounter:

    m: dict[str, int]

    def __init__ (self) -> None:
        self.m = {}

    def __str__ (self) -> str:
        return str(self.m)

    def __len__ (self) -> int:
        return len(self.m)

    def add (self, char: str) -> None:
        char = char[0]
        if char not in self.m:
            self.m[char] = 1
        else: self.m[char] += 1

    def subtract (self, char: str) -> None:
        char = char[0]
        if char not in self.m: return
        self.m[char] -= 1
        if self.m[char] <= 0:
            del self.m[char]

class TuningTrouble:

    signal: str
    counter: PositiveCounter

    def __init__ (self, s: str) -> None:
        self.signal, self.counter = s, PositiveCounter()

    def after_start_packet (self, size=4) -> int:
        for index in range(size):
            self.counter.add(self.signal[index])

        left, right = 0, size - 1
        while len(self.counter) != size:
            self.counter.subtract(self.signal[left])
            left += 1
            right += 1
            self.counter.add(self.signal[right])

        return right + 1

example = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"    
puzzle = "nfddjzjjjmrjjfttzctzzhqzqbbvhhcfcpcqpcqpccsmsvsswbwzwfffnvfvpfvffhnnrgngzgrrhvhfhvvmjvjcccvppqdppbnbjjzlzflfccjjtctqccrhrnhnqhqwwjssjjhpjjcqqdgghddhfdfbffdpfdfzdddthhrcrbrqrbqqbcbnnwbbzcbzccmqqwllrljjjpqpdpsddmbmccwwgngmmzzzpbpspnprnppprmmwfwffrrpsrrchrrrrdqdfddnvnjnppqmqhhpshhjmhjhzjhhhzllbpbnnngdgzgmmjvvprrhqrhqhpqhqqrnqnddvjvvftfggfcgfffgrghhbmbzzjczzcscrccgbbjbqjbjsbsqbqttbqbfqqqrzrmzrmmcwcmwmrwmwnmnfnjjbdjbbslltjjmgmrmllhbhsbsmsqmqllvjjrvjrjcrrtztjzjbjsbbrjjvbjjgqjjpjsszpszsnznllvmlmfmppbvbzvvddtbtrbttchthjthjhnjnqnqrrllnflnnljnnzjjswjwllpmmpnnqnrrndnnbwwmcmcmbbhjjbbfpfvpvttcvvhshqqznzqqdndldmllpgptgptpbblzlddgqqdmmvpvvrccfvvjrvjjgpggqcggjbgbqqcgqccgppffjppzczmzdmmqppwcwlcwwhccfpcphcctvtzthtzhhnmnvmnnvqnqnpnqqwqsqdsszwzbwwgcwcrrtprrfhhcmcqcdcvdcccnpptgpgwpprsprsrdrtdrtrntrtprtppstsccbwwvnvpnvpnptpqttzbzcznzhzhddfbflfcchvchhplhlwhhlhglhhwqqzlqzlzvlvtlvtvrttglttslslclslqssslclbbrjrpjjcscfsfppjlplhplptlltlflglffdttmffrggfjjmllbnlnbnznqnfffmhhnmmsgmsmfsszggpnnhmhnnpwnndqqlmqmnmtnmtnttvtztlzlnzzsdsnssvhsszcscffcpczpcpffpwfwnwhnntnssptthccbnndppgjgpjpssbnnpgnpppjtjqqzfqqrrbmmbdddzjzvzwzssnpsnspnpvnpppjppvsvffmpffbcffslfsfmsmmqzzmttnsnqsqcsqsbqbcclqqphpttvrtrlrhrthhlppscsrsjjvljlmlwlslblqqqgdsbrzwzjzwcjrwbpfmjtmdgjvbcfvtvmsfjtjcmtlzmsjlnmhcswcmjndggdsmqfmmdngjpvrsbhrchldnhdhfdlwccnfmgbwfzppgzzcvblvsmqbfghrgdwlzdcvpqthgbdlwbrfpsvlgpdqznftswgwvchjfrblbdsqjmzchfhlrjhpbrdgvgrrmhrnrdbrdsfsgzvqfdtnvddbtcjwphrhgpqlzjssrgzjcncjnbrzvhgbwpgtfnqhpspmgptzcgvjqgzpmwtjtzldqnclmplwdpzcppgcbrsnlzfgmlnljjhfzrftnhdfnqchgdqrfcjszvbmdrghwzmjnwgnrlptljzqrwsmcfwvbcjgsfdjhnqgzzztmcgmndbtdwvqmzlfcmhfgpqztwgjdccncdccpgbcvhfzbhhbjhgjpdzcmrwgtvrmzdwjtmlzllmgplpqjwwwvbrzgmvpcvwchcwfgbjtzrfctgvfrpphbnsbjlswrztqmchtzfstzdgdwwvhpdhztbmsrbqmndpgvnwwdtgzcddvmvbjstqmjvtzlzgrhzhvplwnpphctvtlvnpmwfzmqcvrnfmmgtsgbcjpffrvbpqpszfpjsjtzqmcnzhnjnpwtvgfqntnhhjhmbvmlvmqgggrnfmmmsvfsqffbvwtzlfhlbjqhrltzwfstvjqhbbblqdbcmgtjgmzdtpslbzsgnmpzsswjlwdpzpmmvmpntbhnqlwrcrfbghzhwlhhpjqztjjrrfscrtwtnlqlqmdbmbfnvngvvthhghgsvqlqvgvmtjmjtwpcznzqhhfpqqfphcdrtzjjhsffslthzwpmsnltnjmfgpsjgqzdwrtgnhflhrnjwqftpnqgptgvgjptzhhtqhtddsfhppmmqcrsnlnrswpjhqgzbpwzfzptzqzzwltlrmjwjrwdgvvzhshqqrhtzmvqpfljlvpmrzbqpscpvsfdbdbcbdwwhpmldlrgpwslzhtbpgtzscfhjlgwcgbhcbftpftvpggvcdvndqnfvfqbwrjtdcbwpsbqpzmwdhjpmjhjmlcdphrjbgsnmcmvfnrggfvttclmbvsfjpnbndbblnbdfqzmsldlswdrtzqsqppjshtlrtccthmmpjgddbbgfgthnzdffbtrpchzgbvqvjcsnpgbrzrczzmzrmhjrlvvgmsqddjsqmcqfmwnhznbczzjlpmhnfwjtrfgffsjdlwgdwwlvdpdlvszphntrvttczgnwffsdsvjmqbthgcgfjgznrfnbplbvgsjbsglhnrjpbldhmznqgqpvldvhcpmmwzfjdjdbnprtrrnwsszjhmngvmtsrqdqdsprwhjpsqwqbsdtpptwlbfbsvdgrplrvpnfbzwrdsdbvhpgwcnqvwdcswdmdltchnngpmlqvchbnrpzcnfhvlzbwbnmssbhpvvmpcwvrwzpfpssndwwfnrslpjwhwrfsswmgtszrhczcrclpldpwpghgptmzzjjjtvjcnncjpfbcvldbnlnqtsqdswcsrqcfgvwbwdvbdwwzndfvcstjbfngtqqwsbpdjdgqdlsnwgcvmmhrqcqvdbqdqczzwzlfgffbwzbfdnpvprzmqclllsdvctwjfgqbchhmsntlvnlspwtnhgshwrvzccfmfrscqwrvdccwqnrccctjrvvnqbrphrfvfrfldbbthhrdzvdmfbctsmvgwmvpdslgbcpqqdvpsjcdvmctwghdsjtmhhvdswbcvtmsnsztfghnnfhflmmnmdqpvpdplllzgqgnsjwsrgzfwhrwhcscvrgcrgjdghqjfbswtgjsvnpqznrvbdbrplwdmbqhtbcfccnpwqlsdstnpcfpbfgqrzmcqhflmcfvbbnwrrblnfslsrwpwlbvqfhgpdwzmgvftssrvdmhnmwdfqmsvqbltlmmwmjrrhgpgznqbwhcqgphvzqmntbbdhhpnlbbffjgmcdntgwmtblwlzrcdcdbtrllrdnznrrsglnwhtwbrfdrpvgqwsgzwghbtsfwqlchgsnvfmvnzntlsnlwrnjjltrpmhwnzmhrqdlvvzbfgwlwgdsgcjcjfvhbcjgzlqtsljvzcvlppqdszvdbsmgddrtmvbcpbpppcpvhzfsjrmtcpzljbhpnjjmcdwslrhslccpljrtvcscbcltpshpnrqvtdfzbbfqtpbvznvrbflwvbvrhqpzltsdrnqccsfgzzftvjfqslcnmfvwtpdbjhtzwrgvntgnfvqtdrjdgglvrnqfzsbhnvhcdbctthdrjnvwlcsjtmphpvlqjngwjnngmqqnslrrsdfpfbvsvcwjtfmwtbpnnghtvvwlphbnsgflvsfdcqrctvjfjrwqjdmbbcclwvlstbgbfqjgbpbqfwdbpmnvqnfpbhrfhwltmcszpwnvtvhrvpcqhzdppjwttlhgsnvmsrwrnwvgzpbwljjjsjzctftzftvmsstpjnzvmmrgbbpmfmfrszwjdgzfhpvsfdqbbhgvfvqrrtqwlwzwwsnnmmvmlwjzvgrwhmffzwrqwbcdtbtzpspbnqgprdqtzrpmgvnmbsnjnvtzgmhqqtrvltbsrwjlssncdppgpmzqzbzvbpjpfwmvgsbhffzpbctmqvfwhsgdjtwqhrhmgnqpvmpjzhppvcbrpwmdshzcrwzdzcjmhfvjgtbznsmdjphlssmlmbhtmnsqnjfsjwhjvgztnwhmnztqppchngdnhzwpsvqqpzdwgbhcbzvmbnqmghbhgvrqhtfzhgvqdbpvdrjsqrdnhqhrwdlczvtnzwfrqhnffwdvtrnqsmmcjtrhmgbwcmnzbbvdsrlbbtwslhghwprpglpq"

assert TuningTrouble(example).after_start_packet() == 7
print("Part 1:", TuningTrouble(puzzle).after_start_packet())

assert TuningTrouble(example).after_start_packet(size=14) == 19
print("Part 2:", TuningTrouble(puzzle).after_start_packet(size=14))
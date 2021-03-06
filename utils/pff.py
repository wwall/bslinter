from dataclasses import dataclass
import ripper

"""
Парсер отчета замера производительности.
"""

@dataclass
class Row:
    thread_uuid: str
    module_uuid: str
    module_type: str
    module_name: str
    line_number: int
    source_code: str
    usage_count: int
    seconds_sum: float
    seconds_net: float
    percent_sum: float
    percent_net: float
    client_side: bool
    server_side: bool
    server_call: bool

def parse(src):
    result = []
    tree, _ = ripper.parse(src)
    table = tree[4]
    count = int(table[1])
    for i in range(2, count*13, 13):
        result.append(
            Row(
                thread_uuid=table[i],
                module_uuid=table[i+1][1],
                module_type=table[i+1][2],
                module_name=table[i+2],
                line_number=int(table[i+3]),
                source_code=table[i+4],
                usage_count=int(table[i+5]),
                seconds_sum=float(table[i+6]),
                seconds_net=float(table[i+7]),
                percent_sum=float(table[i+8]),
                percent_net=float(table[i+9]),
                client_side=bool(int(table[i+10])),
                server_side=bool(int(table[i+11])),
                server_call=bool(int(table[i+12])),
            )
        )
    return result
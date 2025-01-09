# 블록리스트 관리 파일

BLOCKLIST = set()

def add_to_blocklist(jwi):
    BLOCKLIST.add(jwi)
    
def remove_from_blocklist(jwi):
    BLOCKLIST.discard(jwi)
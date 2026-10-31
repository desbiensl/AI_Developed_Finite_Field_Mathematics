"""Verify a recursive Lucas certificate using only Python's standard library."""
from pathlib import Path
import json
from math import gcd, prod

def verify(path: Path) -> int:
    records = json.loads(path.read_text())
    proved, active = set(), set()
    def check(q: int) -> None:
        if q in proved:
            return
        if q in active:
            raise ValueError('Cyclic certificate dependency')
        active.add(q)
        r = records[str(q)]
        assert int(r['prime']) == q
        if q == 2:
            assert r.get('base') is True
        else:
            assert q > 2 and q % 2
            factors = [(int(t), int(e)) for t, e in r['factors']]
            assert all(e > 0 for _, e in factors)
            assert len({t for t, _ in factors}) == len(factors)
            assert prod(t**e for t, e in factors) == q - 1
            for t, _ in factors:
                assert 1 < t < q
                check(t)
            w = int(r['witness'])
            assert pow(w, q - 1, q) == 1
            assert all(gcd(pow(w, (q-1)//t, q)-1, q) == 1 for t, _ in factors)
        active.remove(q)
        proved.add(q)
    for q in map(int, records):
        check(q)
    return len(proved)

if __name__ == '__main__':
    count = verify(Path(__file__).with_name('prime_certificate.json'))
    print(f'PASS: {count} recursive Lucas primality certificates; standard library only.')
